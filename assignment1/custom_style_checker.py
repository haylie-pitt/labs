import ast
import os

class FileParser:
    """A class to handle reading Python source files."""

    def __init__(self, file_path):
        """Initialize with the path to the Python file."""
        self.file_path = file_path
        self.lines = []

    def read_file(self):
        """Read the file and store its lines."""
        with open(self.file_path, 'r') as file:
            self.lines = file.readlines()

    def get_total_lines(self):
        """Return the total number of lines in the file."""
        return len(self.lines)

class CodeInspector:
    """A class to inspect code elements in the Python file."""

    def __init__(self, file_path):
        """Initialize with the path to the Python file and parse it."""
        self.file_path = file_path
        self.imports = []
        self.classes = []
        self.functions = []
        self.docstrings = {}
        self.type_annotation_issues = []
        self.naming_issues = {
            "classes": [],
            "functions": []
        }
        self.parse_file()

    def parse_file(self):
        """Parse the Python file and gather information."""
        with open(self.file_path, 'r') as file:
            node = ast.parse(file.read())
            for elem in node.body:
                if isinstance(elem, ast.Import) or isinstance(elem, ast.ImportFrom):
                    self.imports.append(elem)
                elif isinstance(elem, ast.ClassDef):
                    self.classes.append(elem)
                    self.check_naming_convention(elem.name)
                    self.extract_docstring(elem)
                elif isinstance(elem, ast.FunctionDef):
                    self.functions.append(elem)
                    self.check_naming_convention(elem.name)
                    self.extract_docstring(elem)
                    self.check_type_annotations(elem)

    def extract_docstring(self, elem):
        """Extract the docstring from classes, functions, or methods."""
        docstring = ast.get_docstring(elem)
        if docstring:
            self.docstrings[elem.name] = docstring
        else:
            self.docstrings[elem.name] = f"{elem.name}: DocString not found."

    def check_type_annotations(self, func):
        """Check if the function has type annotations."""
        if not func.returns and not all(arg.annotation for arg in func.args):
            self.type_annotation_issues.append(func.name)

    def check_naming_convention(self, name):
        """Check if names follow the specified naming convention."""
        if not name[0].isupper():  # Classes should use CamelCase
            self.naming_issues['classes'].append(name)
        if not name.islower() or '_' not in name:  # Functions should use snake_case
            self.naming_issues['functions'].append(name)

class ReportGenerator:
    """A class to generate the style report."""
    
    def __init__(self, file_path):
        """Initialize with the path to the Python file."""
        self.file_path = file_path
        self.report_content = ""

    def generate_report(self, inspector):
        """Create the report content based on the inspector's findings."""
        file_name = os.path.basename(self.file_path)
        self.report_content += f"Style Report for: {file_name}\n\n"
        self.report_content += f"Total lines of code: {inspector.get_total_lines()}\n\n"

        self.report_content += "Imports:\n"
        for imp in inspector.imports:
            self.report_content += f"  - {ast.dump(imp)}\n"
        self.report_content += "\n"

        self.report_content += "Classes:\n"
        for cls in inspector.classes:
            self.report_content += f"  - {cls.name}\n"
        self.report_content += "\n"

        self.report_content += "Functions:\n"
        for func in inspector.functions:
            self.report_content += f"  - {func.name}\n"
        self.report_content += "\n"

        self.report_content += "DocStrings:\n"
        for name, doc in inspector.docstrings.items():
            self.report_content += f"{name}:\n{doc}\n\n"

        # Type Annotation Check
        if inspector.type_annotation_issues:
            self.report_content += "Functions without type annotations:\n"
            for name in inspector.type_annotation_issues:
                self.report_content += f"  - {name}\n"
        else:
            self.report_content += "All functions have type annotations.\n"
        self.report_content += "\n"

        # Naming Convention Check
        if inspector.naming_issues['classes']:
            self.report_content += "Classes not adhering to CamelCase:\n"
            for name in inspector.naming_issues['classes']:
                self.report_content += f"  - {name}\n"
        else:
            self.report_content += "All classes adhere to CamelCase.\n"
        self.report_content += "\n"

        if inspector.naming_issues['functions']:
            self.report_content += "Functions not adhering to snake_case:\n"
            for name in inspector.naming_issues['functions']:
                self.report_content += f"  - {name}\n"
        else:
            self.report_content += "All functions adhere to snake_case.\n"

    def write_report(self):
        """Write the report to a text file."""
        report_file_name = f"style_report_{os.path.basename(self.file_path)}.txt"
        with open(report_file_name, 'w') as report_file:
            report_file.write(self.report_content)

class StyleChecker:
    """Main class to run the style checker."""

    def __init__(self, file_path):
        """Initialize with the Python file path."""
        self.file_path = file_path
        self.file_parser = FileParser(file_path)
        self.inspector = CodeInspector(file_path)
        self.report_generator = ReportGenerator(file_path)

    def analyze(self):
        """Run the analysis and generate the report."""
        self.file_parser.read_file()  # Read the file
        total_lines = self.file_parser.get_total_lines()  # Get total lines
        self.report_generator.generate_report(self.inspector)  # Generate report
        self.report_generator.write_report()  # Write report to file

if __name__ == "__main__":
    #'sample_script.py' -- path of the Python file I want to check
    checker = StyleChecker('sample_script.py')
    checker.analyze()  # Start the analysis
