def zipmap(key_list, value_list, override=False):
    if not override and len(key_list) != len(set(key_list)):
        return {}
    
    zipped = zip(key_list, value_list + [None] * (len(key_list) - len(value_list)))
    
    if override:
        return dict(zipped)
    else:
        return {k: v for k, v in zipped if key_list.count(k) == 1}

# Testing zipmap
print(zipmap(['a', 'b', 'c'], [1, 2, 3]))  # {'a': 1, 'b': 2, 'c': 3}
print(zipmap(['a', 'b', 'a'], [1, 2, 3], False))  # {}
print(zipmap(['a', 'b', 'a'], [1, 2, 3], True))  # {'a': 3, 'b': 2}
print(zipmap(['a', 'b', 'c', 'd'], [1, 2]))  # {'a': 1, 'b': 2, 'c': None, 'd': None}
