from collections import deque

n, m = map(int, input().split())
MAX = 100001        # 문제에서 주어진 max값 = 100000
check = [0] * MAX   # check리스트를 만들어 탐색했던 곳 재탐색 방지
check[n] = 1        # 입력위치 방문처리
dq = deque()
dq.append((n, 0))   # 큐에 현재위치와 시간(0초) 추가

# 만약 수빈이가 동생보다 앞이라면 n - m 출력
if n >= m:
    print(n - m)
else:
    while dq:
        # 위치와 시간을 꺼냄
        x, y = dq.popleft()
        # 동생을 찾았다면 시간을 출력하고 반복탈출
        if x == m:
            print(y)
            break
        # 순간이동 한 값이 max보다 작고 방문한적 없다면
        if x*2 <= MAX-1 and check[x*2] == 0:
            # 순간이동은 0초가 걸리므로 먼저 처리하도록 큐의 앞에 추가
            dq.appendleft((x*2,y))
            check[x*2] = 1
        # 앞으로 한칸 이동한 값이 max보다 작고 방문한적 없다면
        if x+1 <= MAX-1 and check[x+1] == 0:
            dq.append((x + 1, y+1))
            check[x+1] = 1
        # 뒤로 한칸 이동한 값이 0보다 크고 방문한적 없다면
        if 0 <= x-1 and check[x-1] == 0:
            dq.append((x - 1, y+1))
            check[x-1] = 1