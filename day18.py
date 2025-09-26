
'''
When we say “recursively copies all nested objects”, it means that if your
 object contains other objects inside it (lists, dicts, sets, etc.), a deep copy doesn’t 
just copy the outer shell — it also makes fresh copies of everything inside, at every level.
'''

'''
A shallow copy creates a new object, 
but does not recursively copy nested objects. Instead, it just copies references to them.
'''

'''
A deep copy creates a new object and
 recursively copies all nested objects, so they are fully independent.
'''

import copy

ll = [[1, 2, 3], [4, 5, 6]]

# ll1 = copy.copy(ll)

# ll1[0][0] = 10

# print(ll)
# print(ll1)


ll2 = copy.deepcopy(ll)

ll2[0][0] = 20

print(ll)
print(ll2)