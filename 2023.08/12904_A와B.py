s = list(input())
t = list(input())

while t:
    a = t.pop()
    if a == 'B':
        t.reverse()
    if s == t:
        print(1)
        exit()
print(0)