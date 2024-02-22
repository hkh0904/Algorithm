dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    
    pass

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))