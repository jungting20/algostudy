

n = int(input())


l = [[0 for i in range(n)] for j in range(n)]



# 끝자리가 0일경우와 9 일 경우는 그 전 자리의 수와 같으니까 셀필요가 없다
def a(a):


    for i in range(n):

        l[1][i] = 1

    for i in range(2,n):
        for j in range(10):
            if j - 1 >= 0:
                l[i][j] += l[i-1][j-1]
            if j + 1 <= 9:
                l[i][j] += l[i-1][j+1]

