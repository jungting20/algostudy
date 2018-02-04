
def go(n):

    if n < 0:
        return 0
    if n <= 1:
        return 1

    a = go(n-1)+go(n-2)+go(n-3)

    return a


n = int(input())
for i in range(n):

    print(go(int(input())))



