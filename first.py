# Q1. 5 numbers – Sum, Average, Max, Min
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))
e = int(input("Enter number 5: "))

nums = [a, b, c, d, e]

print("Sum =", a+b+c+d+e)
print("Average =", (a+b+c+d+e)/5)
print("Maximum =", max(nums))
print("Minimum =", min(nums))

''' output
Enter number 1: 23
Enter number 2: 45
Enter number 3: 89
Enter number 4: 64
Enter number 5: 24
Sum = 245
Average = 49.0
Maximum = 89
Minimum = 23 '''