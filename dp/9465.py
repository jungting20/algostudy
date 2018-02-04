
n = int(input())

for i in range(n):

    b = int(input())

    a = [[0 for i in range(2)] for j in range(b)]
    li = list(map(int,input().split()))
    for i in range(b):
        a[i][0] = li[i]
    li = list(map(int, input().split()))
    for i in range(b):
        a[i][1] = li[i]

    d = [[0 for i in range(3)] for j in range(b)]


    for i in range(1,b):
        
        d[i][0] = max(d[i-1][0],d[i-1][1],d[i-1][2])
        d[i][1] = max(d[i-1][0],d[i-1][2])+a[i][0]
        d[i][2] = max(d[i-1][0],d[i-1][1])+a[i][1]



    print(max(d[b-1][0],d[b-1][1],d[b-1][2]))



