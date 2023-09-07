'''
입력을 뒤에서부터 pop
폭발 문자열 끝문자가 나왔을때 폭발리스트 저장
아니라면 결과리스트에 저장
폭발 문자열이 완성되기 전에 다른 문자가 나왔다면
모든 폭발 문자열 문자 결과리스트에 저장
'''

str_list = input()
boom = input()
str_boom = list(boom)
rlt = []
len_boom = len(str_boom)

for i in str_list:
    rlt.append(i)
    if rlt[-len_boom:] == str_boom:
        for _ in range(len_boom):
            rlt.pop()
if len(rlt) == 0:
    print('FRULA')
else:
    print(''.join(rlt))
        
