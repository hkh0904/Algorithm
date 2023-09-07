import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())
gem = [list(map(int,input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
gem.sort()  # 보석을 무게순 정렬
bag.sort()  # 가방 크기순 정렬

Q =[]   # 우선순위 큐가 될 리스트
answer = 0
# 가방 작은 순부터 반복
for i in bag:
    # 보석의 무게가 가방에 들어갈수 없을때까지 반복
    while gem and gem[0][0]<=i:
        # 최대힙을 이용해서 우선순위 큐에 추가
        heapq.heappush(Q, -heapq.heappop(gem)[1])
    # 반복이 끝난 후 가장 큐의 앞에있는 값을 pop하여 더해줌
    if Q: answer -= heapq.heappop(Q)
print(answer)




# import sys
# imput = sys.stdin.readline

# n, k = map(int, input().split())
# # 보석과 가방 입력
# jem = [list(map(int, input().split())) for _ in range(n)]
# bag = [int(input()) for _ in range(k)]
# # 보석을 무게순으로 정렬한 후 가치가 높은순으로 다시정렬
# jem = sorted(jem, key=lambda x:x[0])
# jem = sorted(jem, key=lambda x:x[1], reverse=True)
# # 가방은 크기가 작은거부터 정렬
# bag = sorted(bag)

# pack = [False]  # 가방을 사용했는지 체크
# ans, cnt = 0, 0     # 보석의 가치, 사용한 가방 개수
# for i in range(len(jem)):
#     for j in range(len(bag)):
#         # 정렬된 보석을 돌면서 작은 가방부터 확인
#         # 가방이 비어있고, 보석이 가방에 들어갈 수 있는 크기라면
#         if jem[i][0] <= bag[j] and pack[j] == False:
#             pack[j] == True     # 가방 사용했다고 체크
#             ans += jem[i][1]    # 보석 가치 더해줌
#             cnt += 1            # 가방 사용개수 +1
#             break
#     # 가방을 전부 사용했다면 반복종료
#     if cnt == len(bag):
#         print(ans)
#         break