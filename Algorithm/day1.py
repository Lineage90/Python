# 1. 그룹 아나그램
# import collections

# strs = ["eat","tea","tan","ate","nat","bat"]

# 
# for str in strs:
#   s = ''.join(sorted(str))
#   result[s] = result.get(s,[]) + [str]
# return result.values()


# 책 풀이
# import collections
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         # 풀이
#         anagrams = collections.defaultdict(list)

#         for word in strs:
#             # 정렬하여 딕셔너리에 추가
#             anagrams[''.join(sorted(word))].append(word)

#         return anagrams.values()    

# 2. 가장 긴 팰린드롬
# 팰린드롬 > 'eye', 'kayak' 등 거꾸로 읽어도 똑같은 문장이나 단어

# s = 'babad'

# a = []
# b = []
# c = []

# for i in s:
#     a.append(i)
# print(a)

# r = s[::-1]
# for j in r:
#     b.append(j)
# print(b)
    
# if len(a) < 2 or a != r:
    
#     print(a[0])

# for k in range(len(s)):
#     if a[k] == b[k]:
#         c.append(a[k])
#     result = ''.join(c)    
# print(result)

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



# 3. 세 수의 합

# nums = [-1, 0, 1, 2, -1, -4]



# 4. 배열 파티션

# nums = [6,2,6,5,1,2]
# nums.sort()
# result = []
# add = 0

# for i in range(0, len(nums), 2):
#     result.append(nums[i:i+2])

# for j in range(len(result)):
#     add += min(result[j])


# 책 풀이

# nums = [1,4,3,2]

# sum = 0
# pair = []
# nums.sort()

# for n in nums:
#     # 앞에서부터 오름차순으로 페어를 만들어 합산
#     pair.append(n)
#     if len(pair) == 2:
#         sum += min(pair)
#         pair = []

# return sum