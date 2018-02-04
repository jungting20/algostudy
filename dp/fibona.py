


#n 번쨰 피보나치수

n = int(input())
flist = []
def fibo(a):
    if a <= 1:
        return a
    else:
        flist[a] = fibo(a-1)+fibo(a-2)
        return flist[a]

print(fibo(n))