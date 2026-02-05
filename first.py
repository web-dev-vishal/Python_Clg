

import sys

print("Command Line Arguments")
print("-"*40)

if len(sys.argv) == 6:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    num3 = int(sys.argv[3])
    num4 = int(sys.argv[4])
    num5 = int(sys.argv[5])
 
    total = num1 + num2 + num3 + num4 + num5
    average = total / 5

    maximum = num1
    if num2 > maximum:
        maximum = num2
    if num3 > maximum:
        maximum = num3
    if num4 > maximum:
        maximum = num4
    if num5 > maximum:
        maximum = num5

    minimum = num1
    if num2 < minimum:
        minimum = num2
    if num3 < minimum:
        minimum = num3
    if num4 < minimum:
        minimum = num4
    if num5 < minimum:
        minimum = num5

    print("Sum:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
else:
    print("Please provide 5 numbers")

print()