from functools import reduce

def filter_with_reduce(predicate, sequence):
    return reduce(lambda acc, x: acc + [x] if predicate(x) else acc, sequence, [])

# Testing filter_with_reduce
print(filter_with_reduce(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
# [2, 4, 6]
print(filter_with_reduce(lambda x: x > 3, [1, 2, 3, 4, 5, 6]))
# [4, 5, 6]
