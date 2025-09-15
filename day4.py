#A list is an ordered, mutable, and indexed collection of items.

#Allows duplicate values and elements of different data types.

#Defined using square brackets [].



l = [1, 2, 3, 4, 5]

from_list = list("abc")   # ['a', 'b', 'c']

print(from_list)


l.append(6)   # Adds 6 to the end of the list
print(l)

l.extend([7, 8, 9])  # Extends list by appending elements from the iterable
print(l)

l.insert(2,'hello')
print(l)   # Inserts 10 at index 3


l = [10, 20, 30, 40]
l.remove(20)          # Remove first occurrence of value
print(l)            # Remove all elements


#l2 = l.copy()         # Shallow copy
l3 = list(l)          # Another way
print(l3)

ll = list([4,5,8,9,6,7,3,2,1])
print(ll)
print(type(ll))

s = {2}
print(type(s))   # set

t = (2,)
print(type(t))   # int

l = [1]
print(type(l))   # list

d = {1: 'a'}
print(type(d))   # dict