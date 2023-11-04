# 1
# nums = [2,7,9,3,1]

# result_a = 0
# result_b = 0

# for i in range(0, len(nums), 2):
#     result_a += nums[i]

# for j in range(1, len(nums), 2):
#     result_b += nums[j]


# if result_a > result_b:
#     print(result_a)
# else:
#     print(result_b)

# [2,1,1,2] 오류

# 2
nums = [2,1,1,2]

dp = [0 for _ in range(len(nums))]

# 배열에 값 없으면 0
if not nums:
    print(0)

# 배열 길이가 2 이하이면 최고 큰 숫자가 답
if len(nums) <= 2:
    print(max(nums))

# dp[0], dp[1]에 nums[0], 
dp[0], dp[1] = nums[0], max(nums[0], nums[1])
print(dp)
for i in range(2, len(nums)):
    dp[i] = max(dp[i-1], dp[i-2]+nums[i])

print(dp.pop())