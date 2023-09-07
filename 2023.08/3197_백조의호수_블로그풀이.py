from collections import deque
from sys import stdin
input = stdin.readline

def water():
    while wq1:
        x, y = wq1.popleft()   #왼쪽에서 pop
        a[x][y] = '.'
        for i in range(4):   #상하좌우 4번 진행
            nx, ny = x+dx[i], y+dy[i]
            #nx가 0보다 작거나 R보다 크거나 같으면 넘어간 것을 의미, ny도 마찬가지(인덱스 번호)
            if nx < 0 or nx >= R or ny < 0 or ny >= C or wc[nx][ny]:
                continue   
            if a[nx][ny] == '.':   #물이 있다면 wq1에 추가
                wq1.append((nx, ny))
            else:   #물이 없다면 wq2에 추가
                wq2.append((nx, ny))
            wc[nx][ny] = True

def swan():
    while sq1:
        x, y = sq1.popleft()
        if x == ex and y == ey:   #백조끼리 만나면 true를 리턴
            return True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or sc[nx][ny]:
                continue
            if a[nx][ny] == '.':
                sq1.append((nx, ny))
            else:
                sq2.append((nx, ny))
            sc[nx][ny] = True
    return False

ex, ey, ans = 0, 0, 0   #ex와 ey는 다른 백조 하나의 위치,ans는 날짜
dx, dy = (0, -1, 0, 1), (-1, 0, 1, 0)   #상하좌우 방향을 의미
R, C = map(int, input().split())   #행과 열 입력
a = [list(input().strip()) for _ in range(R)]
wc = [[False]*C for _ in range(R)]
sc = [[False]*C for _ in range(R)]
wq1, wq2 = deque(), deque()   #양방향 큐 2개 생성
sq1, sq2 = deque(), deque()

for i in range(R):
    for j in range(C):
        if a[i][j] == 'L':   #백조의 위치 설정
            if not sq1:   #sq1의 큐가 없다면, 백조 한 마리의 위치를 추가
                sq1.append((i, j))
                sc[i][j] = True
            else:   #나머지 백조의 위치를 ex와 ey에 저장(도착지로 사용)
                ex, ey = i, j
            a[i][j] = '.'   #백조의 위치도 물을 의미
        if a[i][j] == '.':   #물을 wq1에 추가
            wq1.append((i, j))
            wc[i][j] = True   #물의 위치를 true로 변경
            
while True:
    water()
    if swan():   #백조가 만나면 true를 return하므로 while문을 break
        break
    wq1 = wq2   #다음 날이 되어 다음 빙판을 녹여야 하기 때문에 wq2를 wq1으로 대체
    sq1 = sq2   #다음 날이 되어 백조가 만날 때까지 움직여야 하기 때문에 sq2를 sq1으로 대체
    wq2 = deque()   #새로운 값을 넣어주기 위해 초기화
    sq2 = deque()   #새로운 값을 넣어주기 위해 초기화
    ans += 1   #날짜 추가
print(ans)