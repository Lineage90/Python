# 일일 온도

temperatures = [73,74,75,71,69,72,76,73]

answer = [0] * len(temperatures)
stack = []
for i, cur in enumerate(temperatures):
    # 현재 온도가 스택 값보다 높으면 정답 처리
    while stack and cur > temperatures[stack[-1]]:
        last = stack.pop()
        answer[last] = i - last
    stack.append(i)

print(answer)