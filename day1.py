# cerner_2tothe5th_2021
# get_exponent
# A very inelegant way of getting the power of a number given a base and an exponent. But it works.

def get_power(x, y):
    i = 1
    z = 1
    while (i < y + 1):
        z = z * x
        i = i + 1
    return z

base = 2
exponent = 5
power = get_power(base, exponent)

print(f"Cerner's {base} to the {exponent} has me coding for {power} days.")