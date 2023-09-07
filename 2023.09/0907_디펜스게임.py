import math

def solution(n, k, enemy):
    answer = 0
    # 최적화(무적권이 Enemy Wave만큼 존재)
    if len(enemy) <= k:
        answer = len(enemy)
        return answer
    
    alive = n

    for i in enemy:
        if math.ceil(n/2) <= i and k > 0:
            k -= 1
            answer += 1
        elif i > alive and k > 0:
            k -= 1
            answer += 1
        elif alive - i >= 0:
            alive -= i
            answer += 1
        else:
            break
    return answer
# print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1])) # 5
print(solution(2, 4, [3, 3, 3, 3])) # 4
