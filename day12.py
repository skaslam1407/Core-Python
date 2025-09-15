
'''What is pickle?

pickle is a Python module used for serialization and deserialization of Python objects.

Serialization (pickling): Converting a Python object → byte stream.

Deserialization (unpickling): Converting a byte stream → original Python object.

This allows you to save Python objects to a file or database and reload them later.'''


import pickle

# Data to be pickled
data = {"name": "Sekh", "age": 28, "skills": ["Python", "Django", "API"]}

# --- Pickling: Save to file ---
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# --- Unpickling: Load back ---
with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)



import pickle

numbers = [1, 2, 3, 4, 5]

# Convert object → bytes
pickled_data = pickle.dumps(numbers)

# Convert bytes → object
original_data = pickle.loads(pickled_data)

print(pickled_data)     # b'\x80\x04...'
print(original_data)    # [1, 2, 3, 4, 5]


import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"Person({self.name}, {self.age})"

p = Person("Sekh", 28)

# Pickle object
with open("person.pkl", "wb") as f:
    pickle.dump(p, f)

# Load object back
with open("person.pkl", "rb") as f:
    loaded_p = pickle.load(f)

print(loaded_p)   # Person(Sekh, 28)



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"

b = Book("Python Basics", "Sekh")

print(repr(b))   # Book('Python Basics', 'Sekh')   (developer view)
print(str(b))    # 'Python Basics' by Sekh        (user-friendly view)

