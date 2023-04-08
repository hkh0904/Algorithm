from collections import deque
from sys import stdin
input = stdin.readline

dr = [-1, 1, 0, 0]  # 4방향 탐색
dc = [0, 0, -1, 1]
# N, M 배열 크기 입력
N, M = map(int, input().split())
# 백조위치 저장할 리스트, 호수 입력받을 리스트
swan, lake = [], []
water, melt = deque(), set()    # 물을 저장할 큐, 집합 생성

for i in range(N):
    lake.append(list(input()))  # 호수의 초기상태 입력받음
    for j in range(M):
        if lake[i][j] == '.':       # 물이라면 water 큐에 저장
            water.append((i, j))
        elif lake[i][j] == 'L':     # 백조라면 swan리스트에 저장
            swan.append((i, j))

sq = deque()       # 다른 백조를 찾기 위한 큐
sq.append((swan[0][0], swan[0][1]))     # 1번백조의 위치를 큐에 추가

visited = [[0]*M for _ in range(N)] # visited배열
visited[swan[0][0]][swan[0][1]] = 1 # 1번백조 위치 방문처리

def bfs():
    global lake, melt, sq  # 함수 밖에서 선언했던 리스트, 큐들 글로벌선언
    cnt = 0         # 며칠이 지났는지 체크
    
    while water:
        while water:
            r, c = water.popleft()      # 물 위치 리스트에서 하나씩pop
            for d in range(4):          # 상,하,좌,우 탐색
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < M:     # 유효범위이고
                    if lake[nr][nc] == 'X':         # 물 옆에 얼음이라면
                        melt.add((nr, nc))          # melt 집합에 추가
        while melt:
            r, c = melt.pop()       # melt에서 하나씩 pop
            lake[r][c] = '.'        # 얼음을 물로 변환
            water.append((r, c))    # 녹아서 물이된 칸만 탐색하도록 water 큐에 추가
            
        temp = deque()     # 백조를 찾는 큐가 계속 반복하지 않도록 임시큐
        while sq:
            r, c = sq.popleft()         # sq 큐에서 pop
            if r == swan[1][0] and c == swan[1][1]:     # r, c의 위치가 두번째 백조의 위치라면 리턴
                    return cnt
            for d in range(4):          # 상,하,좌,우 탐색
                nr, nc = r + dr[d], c + dc[d]
                # 유효범위가 아니거나 이미 방문했다면 continue
                if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc] == 1:
                    continue
                if lake[nr][nc] == '.':     # 방문한적 없고 물이라면
                    sq.append((nr, nc))     # 이번 반복에서 계속 탐색하도록 sq 큐에 추가
                else:       # 물이 아니라면 (얼음이라면)
                    temp.append((nr, nc))   # 다음 반복에서 탐색하도록 temp 큐에 추가
                visited[nr][nc] = 1     # 방문처리
        sq = temp   # sq에 temp 저장해 다음 반복에서 temp를 반복하도록 해줌
        cnt += 1    # 소요된 일 추가

print(bfs())        # 며칠 걸렸는지 출력