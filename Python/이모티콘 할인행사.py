from itertools import product

def solution(users, emoticons):
    # 이모티콘 할인율 모든 경우의수
    discount = product([10, 20, 30, 40], repeat=len(emoticons))

    tot_user = 0
    tot_price = 0

    for d in discount:
        user = 0
        price = 0

        for u in users:
            chk = 0
            # 각 이모티콘이 유저가 정한 할인률보다 높거나 같다면 구매(chk에 추가)
            for p in range(len(emoticons)):
                if d[p] >= u[0]:
                    chk += round(emoticons[p] * ((100 - d[p]) / 100))
            # 구매하려 한 이모티콘 가격의 총 합이 유저가 정해둔 가격보다 높다면
            # 이모티콘 플러스 유저 +1
            if chk >= u[1]:
                user += 1
            # 가격 총합이 유저가 정한 가격보다 높지 않다면 price 업데이트
            else:
                price += chk
        
        # 유저의 수가 최고인 경우의 수에서 tot_user, tot_price 업데이트
        if user > tot_user:
            tot_user = user
            tot_price = price
        # 유저의 수가 같다면 tot_price 비교 후 업데이트
        elif user == tot_user:
            if price > tot_price:
                tot_price = price
    
    answer = [tot_user, tot_price]

    return answer


# [1, 5400]
print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
# [4, 13860]
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))