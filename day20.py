# def mydecorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before function call")
#         rv = func(*args, **kwargs)
#         print("After function call")
#         return rv
#     return wrapper

# @mydecorator
# def display(name, age):
#     print(f"Name: {name}, Age: {age}")

# display("Sekh", 40)

# def mydecorator():
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             print("Before function call")
#             rv = func(*args, **kwargs)
#             print("After function call")
#             return rv
#         return inner
#     return wrapper

# @mydecorator()
# def display(name, age):
#     print(f"Name: {name}, Age: {age}")

# display("Sekh", 30)

'''
Normally, a function uses return to send a value back and then it ends.
But if you use yield, the function becomes a generator function — it can pause and resume.
'''

# Generator Function
def mygenerator():
    yield 1
    yield 2
    yield 3


g = mygenerator()

# for x in g:
#     print(x)

# print(next(g))  # First value → 1
# print(next(g))  # Second value → 2
# print(next(g))  # Third value → 3


def fibonacci():
    a, b = 0, 1
    while True:  # infinite generator
        yield a
        a, b = b, a + b

# # Usage
# fib = fibonacci()
# print(fib)
# for i in fib:
#     print(i)
#     if i > 10:
#         break
# for _ in range(5):
#     print(next(fib))

import itertools

fib = fibonacci()
first_10 = list(itertools.islice(fib, 5))
print(first_10)











