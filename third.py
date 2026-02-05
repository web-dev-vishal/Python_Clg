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