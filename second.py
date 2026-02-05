# Q2. Membership Operator

numbers = [10, 20, 30, 40]

x = int(input("Enter number: "))

if x in numbers:
    print("Number found in list")
else:
    numbers.append(x)
    print("Number added")
    print(numbers)
