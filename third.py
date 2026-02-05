# Q3. Random numbers

import random

even = 0
odd = 0

for i in range(10):
    n = random.randint(1, 100)
    print(n)

    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even count:", even)
print("Odd count:", odd)

'''output: 
18
74
36
83
79
87
50
4
85
56
Even count: 6
Odd count: 4
'''