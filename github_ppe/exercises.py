# Going through the exercises from github "Python Programming Exercises"
# will separate into different files if/when necessary

# Q1

numlist = []
for num in range(2000, 3001):
    if num % 7 == 0:
        if num % 5 == 0:
            pass
        else:
            numlist.append(str(num))
    else:
        pass

print(', '.join(numlist))

# Q2

