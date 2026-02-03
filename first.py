# Command line arguments: sum, average, maxixmum, minimum

import sys

print("Command Line Argumnets")
print("-"*40)

if len(sys.argv) ==6:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    num3 = int(sys.argv[3])
    num4 = int(sys.argv[4])
    num5 = int(sys.argv[5])
 
total = num1 + num2 + num3 + num4 + num5
average = total / 5

maxixmum = num1
if num2 > maxixmum:
    maxixmum = num2
if num3 > maxixmum:
    maxixmum = nu3
if num4 > maxixmum:
    maxixmum = num4
if num5 > maxixmum:
    maxixmum = num5

minimum = num1
if num2 > minimum:
    minimum = num2
if num3 > minimum:
    minimum = nu3
if num4 > minimum:
    minimum = num4
if num5 > minimum:
    minimum = num5

print("Sum", total)
print("Average", average)
print("Maximum", maxixmum)
print("Minimum", minimum)
else:
    print("Please provide 5 numbers")
print()