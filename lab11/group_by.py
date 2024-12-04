from collections import defaultdict

def group_by(f, target_list):
    grouped = defaultdict(list)
    for item in target_list:
        grouped[f(item)].append(item)
    return dict(grouped)

# Testing group_by
print(group_by(len, ["hi", "dog", "me", "bad", "good"]))
# {2: ['hi', 'me'], 3: ['dog', 'bad'], 4: ['good']}
print(group_by(lambda x: x % 2, [1, 2, 3, 4, 5, 6]))
# {1: [1, 3, 5], 0: [2, 4, 6]}
