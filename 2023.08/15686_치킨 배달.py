from itertools import combinations

n, m = map(int, input().split())
city = []
home = []
chick = []

for i in range(n):
    city.append(list(map(int, input().split())))
    for j in range(n):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chick.append((i, j))

c_lst = list(combinations(chick, m))
rlt = 999999

for i in c_lst:
    d = [9999] * len(home)
    for r, c in i:
        for j in range(len(home)):
            d[j] = min(d[j], abs(r - home[j][0]) + abs(c - home[j][1]))
    rlt = min(rlt, sum(d))
        
print(rlt)