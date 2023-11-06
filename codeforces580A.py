n = int(input())
a = [int(x) for x in input().split()]

l = [1]*n
for i in range(1,n):
    if a[i]>a[i-1]:
        l[i] = l[i-1]+1

print(max(l))