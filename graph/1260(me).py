n,m,v = map(int,input().split())
check1,check2 = [0 for i in range(n+6)],[0 for i in range(n+6)]

def bfs(list,v):
    import queue
    q = queue.Queue
    q.put(v)
    while q.qsize():

        x = q.get()
        print('bfs',x)
        for i in list[x]:
            if not check1[i]:
                check1[i] = 1
                q.put(i)


def dfs(list,v):

    if check2[v]:
        return

    print('dfs',v)

    for i in list[v]:
        if not check2[v]:
            check2[v] = 1
            dfs(list,i)

