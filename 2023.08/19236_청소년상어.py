# from pprint import pprint
# from copy import deepcopy
# # 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
# # 12시, 11시, 9시, 7시, 6시, 5시, 3시, 1시
# dr = [-1, -1, 0, 1, 1, 1, 0, -1]
# dc = [0, -1, -1, -1, 0, 1, 1, 1]

# def move_fish():
#     global fish
#     for i in range(1, 17):
#         if fish[i]:
#             for d in range(8):
#                 방향 = sea[fish[i][0]][fish[i][1]][1]-1
#                 nr = fish[i][0] + dr[(방향 + d)%8]
#                 nc = fish[i][1] + dc[(방향 + d)%8]
#                 if 0 <= nr < 4 and 0 <= nc < 4 and sea[nr][nc][0] != 'S':
#                     if fish[sea[nr][nc][0]] == 0:
#                         sea[nr][nc], sea[fish[i][0]][fish[i][1]] = [sea[fish[i][0]][fish[i][1]][0], (방향+d)%8+1], sea[nr][nc]
#                         fish[i] = (nr, nc)
#                     else:
#                         sea[nr][nc], sea[fish[i][0]][fish[i][1]] = [sea[fish[i][0]][fish[i][1]][0], (방향+d)%8+1], sea[nr][nc]
#                         j = sea[fish[i][0]][fish[i][1]][0]
#                         fish[i], fish[j] = fish[j], fish[i]
#                     break

# def dfs(r, c, go, cnt):
#     global max_ans, sea, fish, depth
#     # 물고기들이 먼저 이동
#     move_fish()
#     print('================================')
#     pprint(sea)
    
#     x, y = r, c
    
#     while True:
#         if depth[1] == 1 and depth[0] != 0:
#             depth[0] -= 1
#             if depth[0] == 0:
#                 depth[1] = 0
#             return
#         # 상어의 방향으로 한칸씩 이동
#         r, c = r+dr[go-1], c+dc[go-1]
#         # 상어가 범위밖으로 나가려하면 리턴(종료조건)
#         if r < 0 or r >= 4 or c < 0 or c >= 4:
#             max_ans = max(max_ans, cnt)
#             depth[0] -= 1
#             depth[1] = 1
#             print(max_ans)
#             return
#         tmp_sea = deepcopy(sea)
#         tmp_fish = deepcopy(fish)
#         sea[x][y] = [0, 0]
#         temp = sea[r][c]    # 상어가 이동할 곳
        
#         fish[sea[r][c][0]] = False      # 물고기 먹혔다고 처리
#         if sea[r][c][0] == 0:
#             continue
#         else:
#             sea[r][c] = ['S', temp[1]]
#         depth[0] += 1
#         dfs(r, c, temp[1], cnt + temp[0])
        
#         sea = tmp_sea
#         fish = tmp_fish
#         print('============ 복귀 =================')
#         pprint(sea)
# sea = [[] for _ in range(4)]
# fish = [False] * 17
# for i in range(4):
#     line = list(map(int, input().split()))
#     for j in range(0, 8, 2):
#         sea[i].append([line[j], line[j + 1]])
#         fish[line[j]] = (i, j//2)
        
# max_ans = sea[0][0][0]
# fish[sea[0][0][0]] = False
# sea[0][0] = ['S', sea[0][0][1]]
# depth = [0, 0]

# dfs(0, 0, sea[0][0][1], max_ans)
# print(max_ans)



# 청소년 상어 - BOJ 19236
# DFS+구현
import copy

board = [[] for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # 물고기 번호, 방향
        fish.append([data[2*j], data[2*j+1]-1])
    board[i] = fish


max_score = 0


def dfs(sx, sy, score, board):
    global max_score
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    board[sx][sy][0] = 0

    # 물고기 움직임
    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        f_d = board[f_x][f_y][1]

        for i in range(8):
            nd = (f_d+i) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            board[f_x][f_y][1] = nd
            board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
            break

    # 상어 먹음
    s_d = board[sx][sy][1]
    for i in range(1, 5):
        nx = sx + dx[s_d]*i
        ny = sy + dy[s_d]*i
        if (0<= nx < 4 and 0<= ny < 4) and board[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(board))

dfs(0, 0, 0, board)
print(max_score)