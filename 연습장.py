def b(idx, ans):
    global res

    # 가지치기
    if res >= ans:
        return
    
    # 종료조건
    if idx == N:
        res = max(res, ans)
        return
    # 탐색
    for j in range(N): # 열
        if vis[j]== 0:
            vis[j] = 1
            b(idx+1, ans* num_list[idx][j]*(1/100))
            vis[j] = 0

# vis = [0,1,0,0]
T = int(input())

for tc in range(T):
    N = int(input())

    num_list = [list(map(int,input().split())) for _ in range(N)]
    vis = [0]*N
    res = 0
    
    b(0, 1)

    print(f"#{tc+1} {res*100:.6f}")