# 유효한 괄호

# 문제
# s문자만 포함된 문자열이 주어 지면 입력 문자열이 유효한지 확인.'('')''{''}''['']'

# 다음과 같은 경우 입력 문자열이 유효하다

# 1. 열린 괄호는 동일한 유형의 괄호로 닫혀야 합니다.

# 2. 열린 괄호는 올바른 순서로 닫혀야 합니다.

# 3. 모든 닫는 괄호에는 동일한 유형의 해당 열린 괄호가 있습니다.

# 입, 출력
# 입력: s = "()"
#  출력: true    

# 입력: s = "(]"
#  출력: false

# s = '()'

# dict = {
#             ")" : "(",
#             "}" : "{",
#             "]" : "[",
#         }

# stack = []

# for str in s:
#     if str not in dict:
#         stack.append(str)
#     elif not stack or dict[str] != stack.pop():
#         return False

# return len(stack) == 0

