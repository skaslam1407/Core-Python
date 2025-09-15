import math
import random
import datetime

# def lcm(a, b):
#     return abs(a * b) // math.gcd(a, b)



# print(lcm(4, 6))  # Output: 12


# print(sum([1, 2, 3, 4, 5]))  # Output: 15


# print(random.randint(1, 10))  # Output: Random integer between 1 and 10

# print(random.choice(['apple', 'banana', 'cherry']))  # Output: Random choice from the list

# print(random.sample(range(100), 5))  # Output: List of 5 unique random numbers from 0 to 99

# print(random.uniform(1.0, 10.0))  # Output: Random float between 1.0 and 10.0
# print(random.shuffle([1, 2, 3, 4, 5]))  # Output: Shuffled list [1, 2, 3, 4, 5]
# print(random.seed(42))  # Set seed for reproducibility      
# print(random.random())  # Output: Random float between 0.0 and 1.0
# print(random.getrandbits(8))  # Output: Random integer with 8 random bits
# print(random.randrange(0, 100, 5))  # Output: Random integer from
# print(random.choices(['red', 'blue', 'green'], k=3))  # Output: List of 3 random choices from the list


print(datetime.datetime.now())  # Output: Current date and time
print(datetime.date.today())  # Output: Current date
print(datetime.datetime(2023, 1, 1))  # Output: Specific date

print(datetime.timedelta(days=5))  # Output: Time delta of 5 days
print(datetime.datetime.now() + datetime.timedelta(days=5))  # Output: Date and time

print(datetime.datetime.strptime('2023-01-01', '%Y-%m-%d'))  # Output: Parsed date
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # Output: Formatted current date and time
print(datetime.datetime.now().isoformat())  # Output: ISO formatted date and time
print(datetime.datetime.now().timestamp())  # Output: Current timestamp

print(datetime.datetime.now().date())  # Output: Date part of current date and time



