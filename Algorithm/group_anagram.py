# 1. 그룹 아나그램
import collections

# 풀이
strs = ["eat","tea","tan","ate","nat","bat"]
    # 풀이
    
anagrams = collections.defaultdict(list)

for word in strs:
            # 정렬하여 딕셔너리에 추가
    anagrams[''.join(sorted(word))].append(word)

print(anagrams.values())