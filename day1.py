# cerner_2tothe5th_2021
# get_exponent
# A very inelegant way of getting an exponent. But it works.

def get_exponent(x, y):
    i = 1
    z = 1
    while (i < y + 1):
        z = z * x
        i = i + 1
    return z

exponent = get_exponent(2, 10)

print(exponent)