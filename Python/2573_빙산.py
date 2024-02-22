import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    # 현재위치 deque에 추가 후 방문처리
    q = deque([(x, y)])
    visited[x][y] = 1
    seaList = []

    while q:
        x, y = q.popleft()
        sea = 0
        # 4방향 탐색
        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]
            # nr, nc가 유효범위일때
            if 0 <= nr < n and 0 <= nc < m:
                # 주변에 0이있다면 sea+1
                if not board[nr][nc]:
                    sea += 1
                # 주변이 0이 아니고, 방문한적이없다면
                elif board[nr][nc] and not visited[nr][nc]:
                    q.append((nr, nc))      # deque에 추가, 방문처리
                    visited[nr][nc] = 1
        # 위치 (r,c)에서 주변에 바다가 있다면
        # 바다리스트에 바다칸 수와 함께 저장
        if sea > 0:
            seaList.append((x, y, sea))
    # 반복 종료 후 얼음이 녹은 것 처리(0보다 작다면 0으로)
    for x, y, sea in seaList:
        board[x][y] = max(0, board[x][y] - sea)
    # 얼음 한블록이 나왔으므로 return 1
    return 1


n, m = map(int, input().split())    
# 현재 빙산 현황입력
board = [list(map(int, input().split())) for _ in range(n)]

ice = []
for i in range(n):
    for j in range(m):
        if board[i][j]:
            ice.append((i, j))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
year = 0

while ice:
    # 방문처리 배열 생성
    visited = [[0] * m for _ in range(n)]
    melt = []   # 녹아서 얼음이 없어지는 배열
    block = 0   # 빙산 조각 개수
    for i, j in ice:
        # 빙산이 있고 아직 방문하지 않은 경우
        if board[i][j] and not visited[i][j]:
            block += bfs(i, j)
        # bfs를 돌고 board[i][j]가 0이되었다면 melt에 추가
        if board[i][j] == 0:
            melt.append((i, j))
    # 빙산 조각개수가 1보다 크다면(2 이상이라면)
    # 몇년 걸렸는지 출력 후 반복종료
    if block > 1:
        print(year)
        break
    # 빙산 리스트에서녹아서 없어진 빙산자리 제거
    ice = sorted(list(set(ice) - set(melt)))
    year += 1   # 1년 추가
# 얼음이 다녹아도 2조각 이상으로 갈라지는 경우가 없는경우
if block < 2:
    print(0)