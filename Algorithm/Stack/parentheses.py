# 괄호

# 주어지는 N개의 괄호 문자열이 VPS 인지 판단해 YES NO 를 반환하라

# VPS : () 로 이루어진 한쌍의 괄호
import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    per = input()
    a = []
    for i in per:
        if i == '(':
            a.append(i)
        elif i == ')':
            if len(a) == 0:
                a.append(i)
                break
            else:
                a.pop()
    # 리스트 길이가 0이 아니면 NO           
    if len(a) != 0:
        print('NO')
    # 맞으면 YES
    else:
        print('YES')
                