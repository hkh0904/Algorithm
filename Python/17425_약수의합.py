max_val = 1000000

dp = [0] * (max_val + 1)
dp_sum = [0] * (max_val + 1)

for i in range(1, (max_val + 1)):
    j = 1
    while i*j <= max_val:
        dp[i*j] += i
        j += 1
    dp_sum[i] = dp_sum[i-1] + dp[i]

for _ in range(int(input())):
    num = int(input())
    print(dp_sum[num])