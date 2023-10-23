nums = [1,2,3]

result = []
twos = []

def subset_b(start):
    result.append(twos[:])
    
    # 재귀함수로 호출
    for i in range(start, len(nums)):
        if nums[i] not in twos:
            twos.append(nums[i])
            subset_b(i + 1)
            
            twos.pop()
            
subset_b(0)
print(result)
