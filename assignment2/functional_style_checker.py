import os
import ast
from typing import List, Dict, Optional


# Helper Functions
def read_file(file_path: str) -> str:
    """Reads the content of the given Python file."""
    with open(file_path, 'r') as file:
        return file.read()


def get_imports(file_content: str) -> List[str]:
    """Extracts and returns a list of imports from the file content."""
    tree = ast.parse(file_content)
    imports = [node.names[0].name for node in ast.walk(tree) if isinstance(node, ast.Import)]
    imports += [node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]
    return imports


def get_classes_and_functions(file_content: str) -> (List[str], List[str]):
    """Extracts and returns a list of classes and standalone functions in the file."""
    tree = ast.parse(file_content)
    classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    # Standalone functions are defined at the module level (not within a class)
    functions = [
        node.name for node in tree.body if isinstance(node, ast.FunctionDef)
    ]
    return classes, functions


def get_docstrings(file_content: str) -> Dict[str, Dict[str, str]]:
    """Extracts docstrings for classes, their methods, and standalone functions."""
    tree = ast.parse(file_content)
    docstrings = {}

    for node in tree.body:  # Only consider top-level nodes
        if isinstance(node, ast.ClassDef):
            # Add class-level docstring
            docstrings[node.name] = {"__class_doc__": ast.get_docstring(node) or "DocString not found"}
            # Process methods within the class
            for child in node.body:
                if isinstance(child, ast.FunctionDef):
                    docstrings[node.name][child.name] = ast.get_docstring(child) or "DocString not found"
        elif isinstance(node, ast.FunctionDef):
            # Standalone function docstrings
            docstrings[node.name] = ast.get_docstring(node) or "DocString not found"

    return docstrings


def check_type_annotations(functions: List[str], file_content: str) -> List[str]:
    """
    Checks if the provided functions have type annotations for arguments and return values.
    Returns a list of functions missing annotations.
    """
    tree = ast.parse(file_content)
    functions_without_annotations = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in functions:
            # Check function arguments for annotations
            for arg in node.args.args:
                if arg.annotation is None:
                    functions_without_annotations.append(node.name)
            # Check return type annotation
            if node.returns is None:
                functions_without_annotations.append(node.name)

    return functions_without_annotations


def check_naming_conventions(classes: List[str], functions: List[str]) -> (List[str], List[str]):
    """Checks if the naming conventions are followed."""
    non_compliant_classes = [cls for cls in classes if not cls[0].isupper()]
    non_compliant_functions = [func for func in functions if not func.islower()]
    
    return non_compliant_classes, non_compliant_functions


# Main Logic
def generate_report(file_path: str) -> None:
    """
    Generates a style report for the given Python file.

    The report includes file structure, imports, classes, functions, docstrings, type annotations,
    and naming convention compliance. The report is saved as a text file.
    """
    file_content = read_file(file_path)
    file_name = os.path.basename(file_path)

    # File Structure
    total_lines = len(file_content.splitlines())
    imports = get_imports(file_content)
    classes, functions = get_classes_and_functions(file_content)

    # Doc Strings
    docstrings = get_docstrings(file_content)

    # Type Annotation Check
    functions_without_annotations = check_type_annotations(functions, file_content)

    # Naming Convention Check
    non_compliant_classes, non_compliant_functions = check_naming_conventions(classes, functions)

    # Writing the report
    report_filename = f"style_report_{file_name}"
    with open(report_filename, 'w') as report_file:
        report_file.write(f"File structure:\n")
        report_file.write(f"Total lines of code: {total_lines}\n")
        report_file.write(f"Imports:\n")
        for imp in imports:
            report_file.write(f"  - {imp}\n")

        report_file.write(f"\nClasses:\n")
        if classes:
            for cls in classes:
                report_file.write(f"  - {cls}\n")
        else:
            report_file.write("  None\n")

        report_file.write(f"\nFunctions:\n")
        if functions:
            for func in functions:
                report_file.write(f"  - {func}\n")
        else:
            report_file.write("  None\n")

        report_file.write(f"\nDoc Strings:\n")
        for name, content in docstrings.items():
            if isinstance(content, dict):  # Class with methods
                report_file.write(f"\nClass: {name}\n")
                report_file.write(f"  Class DocString: {content['__class_doc__']}\n")
                report_file.write("  Methods:\n")
                for method, doc in content.items():
                    if method != "__class_doc__":
                        report_file.write(f"    - {method}: {doc}\n")
            else:  # Standalone function
                report_file.write(f"\nFunction: {name}\n")
                report_file.write(f"  DocString: {content}\n")

        # Type Annotation Check
        report_file.write(f"\nType Annotation Check:\n")
        if functions_without_annotations:
            for func in functions_without_annotations:
                report_file.write(f"{func}: Type annotation not found\n")
        else:
            report_file.write("All functions have type annotations.\n")

        # Naming Convention Check
        report_file.write(f"\nNaming Convention Check:\n")
        if non_compliant_classes:
            for cls in non_compliant_classes:
                report_file.write(f"Class {cls} does not follow CamelCase\n")
        if non_compliant_functions:
            for func in non_compliant_functions:
                report_file.write(f"Function {func} does not follow snake_case\n")
        if not non_compliant_classes and not non_compliant_functions:
            report_file.write("All names adhere to the specified naming conventions.\n")

    print(f"Report generated: {report_filename}")


if __name__ == "__main__":
    file_path = input("Enter the Python file path: ")
    generate_report(file_path)
