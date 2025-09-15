#zip() takes two or more iterables and returns an iterator of tuples.

#Each tuple contains elements from the iterables at the same position (index).

#The length of the result is equal to the shortest iterable.

l1 = [ 4,5,6,7,8]
l2 = [ 1,2,3,9,10]

for x,y in zip(l1,l2):
    print(x,y)
    print(type(x),type(y))


names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

zipped = zip(names, ages)
print(list(zipped))
# [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

#Unzipping (Reverse of Zip)

pairs = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
names, ages = zip(*pairs)

print(names)  # ('Alice', 'Bob', 'Charlie')
print(ages)   # (25, 30, 35)

print(type(names), type(ages))

#Combining More Than Two Iterables

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NY", "LA", "Chicago"]

print(list(zip(names, ages, cities)))
# [('Alice', 25, 'NY'), ('Bob', 30, 'LA'), ('Charlie', 35, 'Chicago')]


questions = ["Name", "Age", "City"]
answers = ["Alice", 25, "NY"]

for q, a in zip(questions, answers):
    print(f"{q}: {a}")

#Creating a dictionary from two lists

keys = ["name", "age", "city"]
values = ["Alice", 25, "NY"]

ss  = zip(keys, values)

for s in ss:
    print(s)

print(type(ss))

person = dict(zip(keys, values))
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'NY'}


dd = list([('name', 'Alice'), ('age', 25), ('city', 'NY')])
print(dd)
d = dict(dd)
print(d)


#Creating a dictionary from two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "NY"]

person = dict(zip(keys, values))
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'NY'}



