def reverse_int(a):
    rev = 0
    while(a>0):
        rem = a % 10
        rev = ( rev * 10 ) + rem
        a = a // 10
    return rev

def ispal(p):
    y = reverse_int(p)
    if p == y:
        return 1

def pal():
    x = 999
    max = 0
    for i in range(x,100,-1):
        for j in range(x,100,-1):
            n = i * j
            if ispal(n) == 1:
                if (max < n):
                    max = n
    return max

x = pal()
print(x)
    

