#In Python, dictionaries (dict) are one of the most powerful and commonly used data structures. They store data as key–value pairs and support a wide range of operations.
# # Empty dictionary
# d = {}

# # With values
# d = {"name": "Sekh", "role": "Developer"}

# # Using dict() constructor
# d = dict(name="Sekh", role="Developer")


# # Distionary data type

# dist = { "Name": "Zara", "Age": 7, "Class": "First" 
#         , "Name": "Manni" }

# #print("dist['Name']: ", dist['Name'])
# l = len(dist)
# print("Length of the dictionary: ", l)

# for key in dist:
#     print(key, ":", dist[key])


# for key in dist.keys():
#     print(key)

# print("=============================")    

# for value in dist.values():
#     print(value)

# for key, value in dist.items():
#     print(key, "=>", value)

# for x in range(len(dist)):
#     print(x)    




# # Empty dictionary
# d = {}

# # With values
# d = {"name": "Sekh", "role": "Developer"}

# # Using dict() constructor
# d = dict(name="Sekh", role="Developer")

# print(d)

# Adding elements to a dictionary

#d = {"name": "Sekh", "role": "Developer"}

# print(d['role'])

# print(d.get("role"))

# print(d.get("age",25))


# print(d)


# Adding & Updating Items

# d['name'] = "John"  # Update
# d['salary'] = 5000  # Add

# d = dict(city="kolkata", country="India") # Using dict() constructor

# print(d)

d = {"name": "Sekh", "role": "Developer","age":30}

#print("Sekh" in d)

#d.pop("name")          # Remove by key
#d.popitem()           # Remove last inserted item (Python 3.7+)
#del d["role"]         # Delete by key
#d.clear()             # Remove all items
          
#print(d)

#Iterating Over a Dictionary

# for key in d:                 # Iterate over keys
#     print(key, d[key])

# for key, value in d.items():  # Iterate over key–value pairs
#     print(key, value)

# for value in d.values():      # Iterate over values
#     print(value)


#Dictionary Comprehension

# y = {x*2 for x in range(10)}

# print(y)


# squares = {x: x**2 for x in range(5)}
# print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#Copying & Merging
# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3}

# #copy_d1 = d1.copy()       # Shallow copy
# #d1.update(d2)             # Merge d2 into d1
# merged = {**d1, **d2}     # Merge with unpacking (Python 3.5+)

# print(merged)


d = {"a": 1, "b": 3, "c": 2}

print(len(d))     # Number of items → 3
print(max(d))     # Max key → 'c'
print(min(d))     # Min key → 'a'
print(sorted(d))  # Sorted list of keys → ['a', 'b', 'c']
