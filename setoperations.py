# Task 1:
def make_set(data):
      # Create an empty list to store unique elements
    unique_data = []
    # Loop through each element in the data
    for item in data:
        # If the item is not already in unique_data, add it
        if item not in unique_data:
            unique_data.append(item)
    return unique_data

# Task 2:
def is_set(data):
    # Return False if data is None
    if data is None:
        return False
    # Use make_set to remove duplicates and check if the original list equals the unique list
    return len(data) == len(make_set(data))

# Task 3:
def union(setA, setB):
    # If either set is not a valid set, return an empty list
    if not is_set(setA) or not is_set(setB):
        return []
    # Combine the two lists, then use make_set to remove duplicates
    combined = setA + setB
    return make_set(combined)

#Task 4:
def intersection(setA, setB):
    # If either set is not a valid set, return an empty list
    if not is_set(setA) or not is_set(setB):
        return []
    # Create an empty list to store the intersection
    intersected = []
    # Loop through setA and check if elements exist in setB
    for item in setA:
        if item in setB:
            intersected.append(item)
    return intersected



