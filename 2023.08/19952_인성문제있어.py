from collections import deque
import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    visited = [[0]*W for _ in range(H)]
    visited[r][c] = F
    q = deque()
    q.append((r, c))

    while q:
        r, c = q.popleft()
        # 내 위치에서 힘이 0이면 더갈수 없으므로 return
        if visited[r][c] == 0:
            return "인성 문제있어??"
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            # 유효범위이고 방문하지 않았을 때
            if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc]:
                # 오르막길인데 높이차이가 현재 내 힘보다 작거나 같다면
                if board[nr][nc]-board[r][c] <= visited[r][c]:
                    # 이동할 곳이 도착점이라면 return
                    if nr == E_x-1 and nc == E_y-1:
                        return "잘했어!!"
                    q.append((nr, nc))
                    # 방문처리시 현재 내힘 -1
                    visited[nr][nc] = visited[r][c]-1
    # 갈 수 있는곳 모두 탐색했는데 도착하지 못했다면 return                
    return "인성 문제있어??"
    
T = int(input())
for tc in range(T):
    H, W, O, F, S_x, S_y, E_x, E_y = map(int, input().split())
    board = [[0]*W for _ in range(H)]
    
    for _ in range(O):
        x, y, l  = map(int, input().split())
        board[x-1][y-1] = l
    print(bfs(S_x-1, S_y-1))