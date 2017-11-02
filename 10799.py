import sys
r = lambda: sys.stdin.readline().strip()
s = r()
stack = []
ans = 0
for (i,c) in enumerate(s):
    if c == '(':
        stack.append(i)
    else:
        if stack[-1]+1 == i:
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1
print(ans)