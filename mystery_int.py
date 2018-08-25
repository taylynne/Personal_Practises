mystery_int = 5

multi = 1
for i in range(1, mystery_int+1):
    multi = multi * i
    print(multi)

string = "CS1301"
num = 0

for letter in string:
    print(str(num) + " " + letter)
    num += 1

value = 87
while value <= 100:
    value += 9
    print(value)