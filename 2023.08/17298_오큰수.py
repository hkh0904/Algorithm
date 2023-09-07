n = int(input())
nge = list(map(int, input().split()))

stack = [0]
rlt = [0]*n

for i in range(1, n):
    if nge[i] <= nge[stack[-1]]:
        stack.append(i)
    else:
        while stack and nge[stack[-1]] < nge[i]:
            a = stack.pop()
            rlt[a] = nge[i]
        stack.append(i)

while stack:
    rlt[stack.pop()] = -1
    
print(' '.join(map(str, rlt)))