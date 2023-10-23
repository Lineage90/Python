num = [1,2,3]

result = []
middle = []

def backtrack(start):
    result.append(middle[:])
    
    for i in range(start, len(num)):
        if num[i] not in middle:
            middle.append(num[i])
            backtrack(i+1)
            middle.pop()

backtrack(0)
print(result)
