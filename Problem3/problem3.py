import math

n = 600851475143

for i in range(2,n):
    while(n % i == 0):
        n = n/i;
    if n == 1:
        break

print(i)

    