def sum(a,b):
    return a+b

def multiply(a,b):
    return a*b

def divide(a,b):    
    if b == 0:
        return "Error: Division by zero"
    return a/b
def subtract(a,b):
    return a-b

def power(a,b):
    return a**b

def modulus(a,b):
    return a%b

def floor_divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a//b

def average(a,b):
    return (a+b)/2

def max_num(a,b):
    return max(a,b)
def min_num(a,b):
    return min(a,b)
def absolute(a):
    return abs(a)

def square(a):
    return a**2
def cube(a):
    return a**3
def square_root(a):
    if a < 0:
        return "Error: Negative number"
    return a**0.5
