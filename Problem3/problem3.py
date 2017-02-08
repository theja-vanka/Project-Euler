import math

n = 600851475143

nn = math.ceil(math.sqrt(n))

for i in range(2,nn):
    while(n % i == 0):
        n = n/i;
    if n == 1:
        break

print(i)

    