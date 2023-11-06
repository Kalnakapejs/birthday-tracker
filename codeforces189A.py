#A. Cut Ribbon 189A

rinda = [int(x) for x in input().split()]
n, a, b, c = rinda
res = 0

for i in range((n//a)+1):
    for j in range ((n//b)+1):
        left = n-(a*i)-(b*j)
        if left <0:
            break
        if left % c != 0:
            continue
        skaits = i + j+(left//c)
        if skaits > res:
            res = skaits
    
print(res)