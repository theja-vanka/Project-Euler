x = 1
y = 2
z = 0
tot = 0


while z < 4000000:
    z = y
    if z % 2 == 0:
        tot = tot + z
    z = x + y
    x = y
    y = z

print(tot)