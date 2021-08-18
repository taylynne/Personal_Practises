# codewars, IQ Test
# pick out a number that is different from the rest.

def iq_test(numbers):

    even = []
    odd = []

    for num in numbers:
        if (int(num) % 2 == 0):
            even.append(num)
        else:
            odd.append(num)

    even_len = len(even)
    odd_len = len(odd)

    if even_len > odd_len:
        return odd[0]
    else:
        return even[0]


iq_test("1 2 2")
iq_test("2 4 7 8 10")