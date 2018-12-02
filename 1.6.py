# 在字典中将键映射到多个值上
# multidict

# list
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

# set
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

f = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
print(d == e)
print(d == f)

from collections import defaultdict
h = defaultdict(list)
h['a'].append(1)
h['a'].append(2)
h['b'].append(4)

i = defaultdict(set)
i['a'].add(2)
i['a'].add(1)
i['b'].add(4)

print(h)
print(i)

'''
False
True
defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})
defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {4}})
'''

# A regular dictionary
j = {}
j.setdefault('a', []).append(2)
j.setdefault('a', []).append(1)
j.setdefault('b', []).append(4)
print(j)
'''
{'a': [2, 1], 'b': [4]}
'''

# bad
pairs = ((1, 2), (3, 4))
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

# good
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)


