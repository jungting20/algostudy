import queue
mat=[[0]*1001 for _ in range(1001)]
chk1,chk2=[0 for _ in range(1001)],[0 for _ in range(1001)]
def dfs(v):
    global mat,chk1,n
    print(v,end=" ")
    chk1[v]=1
    for i in range(1,n+1):
        if mat[v][i] and not chk1[i]:
            dfs(i)
def bfs(v):
    global mat,chk2,n
    q=queue.Queue()
    q.put(v)
    chk2[v]=1
    while q.qsize():
        x=q.get()
        print(x,end=" ")
        for i in range(1,n+1):
            if mat[x][i] and not chk2[i]:
                chk2[i]=1
                q.put(i)
n,m,v=map(int,input().split())
while m:
    a,b=map(int,input().split())
    mat[a][b]=1
    mat[b][a]=1
    m-=1
dfs(v)
print()
bfs(v)
print()