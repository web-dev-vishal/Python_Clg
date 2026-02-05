# Q 5. Factors

n = int(input("Enter number: "))

for i in range(1, n+1):
    if n % i == 0:
        if i % 2 == 0:
            continue
        print(i)

'''
output
Enter number: 34
1
17

Enter number: 98
1
7
49
'''