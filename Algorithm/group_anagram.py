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