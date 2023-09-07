n = int(input())
num = list(input().split())

for i in range(n-1, 0, -1):
    for j in range(i):
        if int(num[j] + num[j+1]) < int(num[j+1] + num[j]):
            num[j], num[j+1] = num[j+1], num[j]

a = ''.join(num)
print(int(a))