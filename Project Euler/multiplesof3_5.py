# Project Euler
# Multiples of 3 and 5
# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

numbers = []

for num in range(1, 1000):
    if num % 3 == 0:
        numbers.append(num)
    elif num % 5 == 0:
        if num in numbers:
            continue
        else:
            numbers.append(num)

sum = 0

for num in numbers:
    sum = sum + num

print(sum)

