#A closure is a function that:

#Is defined inside another function (nested function)

#References variables from the enclosing (outer) function

#Remembers those variables even after the outer function has finished execution



# x = 10
# print(id(x))
# def change():
#     #x = 20   # local variable (does NOT affect global x)
#     print(id(x))
#     print("Inside:", x)

# change()
# print("Outside:", x)  # Still 10

# x = 10
# print(id(x))
# def change():
#     global x
#     x = 10   # modifies global variable
#     print(id(x))
#     print("Inside:", x)

# change()
# print(id(x))
# print("Outside:", x)  # 20

# x = 10

# def change():
#     globals()['x'] = 50

# change()
# print(x)  # 50

# def outer_function(msg):   # enclosing function
#     def inner_function():  # nested function
#         print(msg)         # uses variable from outer scope
#     return inner_function  # return function itself

# closure = outer_function("Hello Closure!")
# closure()  # Output: Hello Closure!


def power(exponent):
    def calc(base):
        print(base)
        return base ** exponent  # remembers "exponent"
    return calc

square = power(2)   # function for squaring
cube = power(3)     # function for cubing

#print(square(5))  # 25
#print(cube(2))    # 8

# print(square.__closure__)

# print(square.__closure__[0].cell_contents)  # 2
# print(cube.__closure__[0].cell_contents)    # 3

#A closure is a function that remembers variables from its enclosing scope, 
#even if the outer function has finished execution.

# def my_decorator(func):
#     def wrapper():
#         print("Before the function runs...")
#         func()
#         print("After the function runs...")
#     return wrapper

# @my_decorator   # same as: hello = my_decorator(hello)
# def hello():
#     print("Hello, World!")

# hello()


'''What is a Decorator?

A decorator is a function that takes another function as an argument, adds some functionality, and returns a new function (without changing the original function’s code).

Commonly used in logging, authentication, timing, caching, validation, etc.'''


# def my_decorator(func):
#     def wrapper(*args, **kwargs):   # accepts any arguments
#         print(f"Calling {func.__name__} with {args} {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper

# @my_decorator
# def add(a, b):
#     return a + b

# print(add(3, 4))


'''What is a Factory Function?

A factory function is a function that returns another function (or object) that is customized based on the arguments passed to the outer function.
It "manufactures" functions with specific behaviors.'''


# def multiplier(n):
#     def multiply(x):
#         return x * n   # remembers 'n' from outer function
#     return multiply

# double = multiplier(2)   # creates a function that doubles
# triple = multiplier(3)   # creates a function that triples

# print(double(5))  # 10
# print(triple(5))  # 15


# def greeter(lang):
#     def greet(name):
#         if lang == "en":
#             return f"Hello, {name}"
#         elif lang == "es":
#             return f"Hola, {name}"
#         elif lang == "fr":
#             return f"Bonjour, {name}"
#         else:
#             return f"Hi, {name}"
#     return greet

# english_greet = greeter("en")
# spanish_greet = greeter("es")

# print(english_greet("Sekh"))  # Hello, Sekh
# print(spanish_greet("Sekh"))  # Hola, Sekh


'''What is a Callback Function in Python?

A callback function is a function that you pass as an argument to another function, and that other function will call it back (execute it) at some point.

Callbacks are often used in event handling, asynchronous code, sorting, and functional programming.

In short: Functions passed into functions.'''

def greet(name):
    print(f"Hello, {name}!")

def process_user(callback):
    user = "Sekh"
    callback(user)   # calling the function passed in

process_user(greet)


def compute(x, y, callback):
    result = x + y
    return callback(result)

# passing a lambda as callback
print(compute(5, 3, lambda r: r * 2))   # 16


import time

def download_file(callback):
    print("Downloading file...")
    time.sleep(2)
    print("Download complete")
    callback("file.txt")   # callback after task is done

def on_complete(filename):
    print(f"Processing {filename}...")

download_file(on_complete)
