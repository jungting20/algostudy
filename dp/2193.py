


n = int(input())


d = [0 for i in range(n+1)]
d[1] = 1
d[2] = 1

for i in range(3,n+1):

    d[n] = d[n-1]+d[n-2]


print(d[n])