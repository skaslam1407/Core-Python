#A tuple is an ordered, immutable collection of items.

#Similar to a list, but cannot be changed (immutable).

#Elements can be of different data types.

#Defined using parentheses ().

tp = (7,8,9,10)

#print(tp)

# Examples
t1 = (1, 2, 3)
t2 = ("apple", 3.14, True)
t3 = ()             # Empty tuple
t4 = ('sss',)           # Single element tuple (comma required!)

#print(type(t4))

t = (10, 20, 30, 40)

print(t[0])    # 10 (first element)
print(t[-1])   # 40 (last element)
print(t[1:2])  # (20, 30) (slicing)

t1 = (1,2)
t2 = (3,4)

t3 = t1 + t2
print(t3)

t4 = t1 * 3
print(t4)


t = (1, 2, 3, 4)
print(2 in t)           # True
print(5 not in t) # True

for item in t:
    print(item)


t = (1, 2, 3)
# t[0] = 100  ❌ Error (not allowed)

# But if tuple contains a mutable object (like list), that object can be changed
t = (1, [2, 3], 4)
t[1][0] = 99
print(t)  # (1, [99, 3], 4)


#Tuples have only two built-in methods:


t = (1, 2, 2, 5, 4)

print(t.count(2))  # 2 (number of occurrences)
print(t.index(5))  # 3 (first index of value)


l1 = [1, 2, 3]
l2 = [4, 5, 6]

l3 = l1 + l2

print(l3)
print(type(l3))


d1 = {1: 'a', 2: 'b'}
d2 = {3: 'c', 4: 'd'}
d3 = {**d1, **d2}

print(d3)
print(type(d3))


s1 = {4, 5, 6}
s2 = {7, 8, 9}
s3 = s1.union(s2)

print(s3)
print(type(s3))
s4 = s1 | s2
print(s4)       

print(type(s4))

t = (5, 10, 15, 20)

print(len(t))     # 4
print(max(t))     # 20
print(min(t))     # 5
print(sum(t))     # 50
print(sorted(t))  # [5, 10, 15, 20] (returns list)
print(reversed(t)) # <reversed object> (iterator)
print(tuple(reversed(t))) # (20, 15, 10, 5)CLS


# Packing
t = ("Sekh", "Developer", 28)

# Unpacking
name, role, age = t
print(name)  # Sekh
print(role)  # Developer
print(age)   # 28


nested = (1, (2, 3), (4, 5))
print(nested[1][0])  # 2

