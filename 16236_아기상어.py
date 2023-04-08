
# BFS 돌아서 먹을수 있는 물고기 탐색
# 가장 가까운 물고기 먹고 다시 거리계산(BFS X)
# 상어 크기가 커졌다면 다시 BFS로 먹을수 있는 물고기 탐색
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find(r, c):
    visited = [[0]*N for _ in range(N)]
    visited[r][c] = 1
    q = deque()
    q.append((r, c))
    
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            # 유효범위, 방문한적 없음, 상어 크기와 같거나 작음
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and shark[2] >= sea[nr][nc]:
                # 상어보다 작은 물고기
                if 0 < sea[nr][nc] < shark[2]:
                    if fish == []:  # 물고기없다면 추가
                        fish.append((nr, nc, visited[r][c]))
                    # 더 가까운 물고기있다면 원래물고기 제거하고 추가
                    elif fish[-1][2] > visited[r][c]:
                        fish.pop()
                        fish.append((nr, nc, visited[r][c]))
                    # 거리 같은 물고기라면 리스트에 추가
                    elif fish[-1][2] == visited[r][c]:
                        fish.append((nr, nc, visited[r][c]))
                # 물고기 위치와 상어사이의 거리
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))

def eat():
    global ate, shark, time
    
    ate += 1
    time += fish[0][2]
    shark[0], shark[1] = fish[0][0], fish[0][1]
    sea[shark[0]][shark[1]] = 0
    
    if ate == shark[2]:
        ate = 0
        shark[2] = shark[2] + 1

N = int(input())
sea = []
shark = 0
# 상어 위치 탐색
for i in range(N):
    sea.append(list(map(int, input().split())))
    for j in range(N):
        if sea[i][j] == 9:
            shark = [i, j, 2]
            sea[i][j] = 0
ate = 0
time = 0

while True:
    fish = []
    find(shark[0], shark[1])
    if fish == []:
        break
    fish = sorted(fish, key=lambda x: (x[0], x[1]))
    eat()

print(time)