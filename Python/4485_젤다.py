import heapq

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(cost, r, c):
    visited = [[9*125]*n for _ in range(n)]
    visited[0][0] = cave[0][0]
    q = [] # 힙큐로 사용할 리스트
    # 힙큐에 현재 값, 위치 저장
    heapq.heappush(q, (cave[0][0], r, c))
    
    while q:
        cost, r, c = heapq.heappop(q)   # 힙큐에서 pop
        # pop한 위치가 목표지점이라면 return
        if r == n-1 and c == n-1:
            return f"Problem {cnt}: {visited[n-1][n-1]}"
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            # 유효범위라면
            if 0 <= nr < n and 0 <= nc < n:
                # 새로운 값 = 기존 값 + 이동할 위치의 값
                new_cost = cost + cave[nr][nc]
                # 새 값이 이동할 위치에 저장된 값보다 작다면
                if new_cost < visited[nr][nc]:
                    visited[nr][nc] = new_cost  # 최소값 갱신
                    heapq.heappush(q, (new_cost, nr, nc))   # 힙큐에 추가
    
cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(n)]
    print(bfs(cave[0][0], 0, 0))
    cnt += 1