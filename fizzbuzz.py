# cerner_2tothe5th_2021
# My way of doing fizzbuzz. Gets you fizz, gets you buzz, gets you fizzbuzz. Invoke with "python ./fizzbuz.py <integer>"
# and it will loop through until it finds all N fizz, buzz and fizzbuzz.
import sys
try:
    length = int(sys.argv[1])
except ValueError:
    print("Value must be a number")
    sys.exit()
number = 0
fizz = []
buzz = []
fizzbuzz = []

while ((len(fizz) <= length) or (len(buzz) <= length) or (len(fizzbuzz) <= length)):
    if ((number % 3 == 0) and (number % 5 == 0)):
        print(f"{number} is fizzbuzz")
        fizzbuzz.append(number)
        number += 1
    if (number % 3 == 0):
        print(f"{number} is fizz")
        fizz.append(number)
        number += 1
    elif (number % 5 == 0):
        print(f"{number} is buzz")
        buzz.append(number)
        number += 1
    else:
        number += 1
print(f"Fizz: {fizz}")
print(f"Buzz: {buzz}")
print(f"Fizzbuzz: {fizzbuzz}")
