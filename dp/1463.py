
n = int(input())
c= 987654321
def make1(n,s = 0):
    global c
    if n != 1:

        if n % 2==0:
            make1(n/2,s+1)
        if n % 3 == 0:
            make1(n / 3, s + 1)
        else:
            make1(n-1,s+1)
    else:
        if c > s:
            c = s


make1(n,0)
print(c)