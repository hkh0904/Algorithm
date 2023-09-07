from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(redx, redy, bluex, bluey):
    q = deque()
    q.append((redx, redy, bluex, bluey))
    visited = []
    visited.append((redx, redy, bluex, bluey))
    cnt = 0
    
    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if cnt > 10:
                return 0
            if board[rx][ry] == 'O':
                return 1
            for d in range(4):
                nrx, nry = rx, ry
                while True:
                    nrx += dr[d]
                    nry += dc[d]
                    if board[nrx][nry] == '#':
                        nrx -= dr[d]
                        nry -= dc[d]
                        break
                    if board[nrx][nry] == 'O':
                        break
                nbx, nby = bx, by
                while True:
                    nbx += dr[d]
                    nby += dc[d]
                    if board[nbx][nby] == '#':
                        nbx -= dr[d]
                        nby -= dc[d]
                        break
                    if board[nbx][nby] == 'O':
                        break
                    
                if board[nbx][nby] == 'O':
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx-rx) + abs(nry-ry) > abs(nbx-bx) + abs(nby-by):
                        nrx -= dr[d]
                        nry -= dc[d]
                    else:
                        nbx -= dr[d]
                        nby -= dc[d]
                if (nrx, nry, nbx, nby) not in visited:
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        cnt += 1
    return 0

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

for i in range(1, n-1):
    for j in range(1, m-1):
        if board[i][j] == 'R':
            red = (i, j)
        elif board[i][j] == 'B':
            blue = (i, j)
            
print(bfs(red[0], red[1], blue[0], blue[1]))
