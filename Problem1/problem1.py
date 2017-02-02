x = 1000
y = 0

for i in range(x):
    if i % 3 == 0:
        y = y + i
    if i % 5 == 0:
        y = y + i
    if i % 5 == 0 and i % 3 == 0:
        y = y - i

print(y)