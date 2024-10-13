frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)
print(frozen) # AttributeError: 'frozenset' object has no attribute 'add'