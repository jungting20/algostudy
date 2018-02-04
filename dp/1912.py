
n = int(input())


d = [0 for i in range(n)]


for i,value in enumerate(map(int,input().split())):
    d[i] = value
    if i == 0:
        continue
    if d[i] < d[i-1]+value:
        d[i] = d[i-1]+value


print(max(d))