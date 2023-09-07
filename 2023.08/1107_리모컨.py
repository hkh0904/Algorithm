chanal = int(input())       # 목표채널
n = int(input())            # 고장난 버튼 개수
broken = []
if n:
    broken = list(map(int, input().split()))    # 고장난 버튼들
# 초기 채널 100에서 목표채널까지의 차를 ans에 저장
ans = abs(chanal-100)
# 1000000까지 순회
for num in range(1000001):
    for i in str(num):  # 순회하는 숫자에 고장난 버튼의 숫자가 있다면 break
        if int(i) in broken:
            break
    # 고장난 버튼이 없었다면 현재 num의 길이와 num과 목표채널의 차이를 더한값과
    # 기존 답을 비교하여 최솟값 갱신
    else:
        ans = min(ans, len(str(num)) + abs(num-chanal))
        
print(ans)