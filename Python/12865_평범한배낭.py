import sys

N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))


#냅색 문제 풀이
for i in range(1, N + 1):
    wei = stuff[i][0] 
    val = stuff[i][1]
    for j in range(1, K + 1):
        if j < wei:
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(val + knapsack[i - 1][j - wei], knapsack[i - 1][j])

print(knapsack[N][K])