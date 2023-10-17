# 4. 배열 파티션

nums = [6,2,6,5,1,2]
nums.sort()
result = []
add = 0

for i in range(0, len(nums), 2):
    result.append(nums[i:i+2])

for j in range(len(result)):
    add += min(result[j])


# 책 풀이

nums = [1,4,3,2]

sum = 0
pair = []
nums.sort()

for n in nums:
    # 앞에서부터 오름차순으로 페어를 만들어 합산
    pair.append(n)
    if len(pair) == 2:
        sum += min(pair)
        pair = []
