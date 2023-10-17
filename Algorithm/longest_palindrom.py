# 2. 가장 긴 팰린드롬
# 팰린드롬 > 'eye', 'kayak' 등 거꾸로 읽어도 똑같은 문장이나 단어

s = 'babad'

a = []
b = []
c = []

for i in s:
    a.append(i)
print(a)

r = s[::-1]
for j in r:
    b.append(j)
print(b)
    
if len(a) < 2 or a != r:
    
    print(a[0])

for k in range(len(s)):
    if a[k] == b[k]:
        c.append(a[k])
    result = ''.join(c)    
print(result)

# 책 풀이
# def expand(left: int, right: int) -> str:
#     # 팰린드롬 판별 및 투 포인터 확장
#     while left >= 0 and right <= len(s) and s[left] == s[right -1]:
#         left -= 1
#         right += 1
#     return s[left + 1:right -1]
    
#     # 해당 사항이 없을 때 빠르게 리턴
#     if len(s) < 2 or s == s[::-1]:
#         return s
    
#     result = ''
    
#     # 슬라이딩 윈도우 우측으로 이동
#     for i in range(len(s) -1):
#         result = max(result,
#                         expand(i, i + 1),
#                         expand(i, i + 2),
#                         key = len)
    
#     return result