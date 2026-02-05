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