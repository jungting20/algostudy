
n = int(input())
a = list(map(int,input().split()))

d = [0]*n


for i in range(n):
    for j in range(i,n):
        if d[i] < d[i-j] + a[j]:
            d[i] = d[i-j]+a[j]
