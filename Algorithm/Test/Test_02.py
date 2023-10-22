N = int(input())

dishes = []
wash = []
dry = []

# N에서 입력한 숫자 역순으로 리스트에 넣기
for i in range(N, 0 , -1):
    dishes.append(i)
while True:
    # dry 와 N이 같으면 break
    if len(dry) == N:
        # 리스트에서 역순으로 결과값 출력
        for i in dry[::-1]:
            print(i)
        break
    
    # a, b 입력받기
    a, b = map(int, input().split())
    
    # 두번째 입력이 1이면 dishes 리스트에서 pop -> wash 리스트에 push
    if a == 1:
        for _ in range(b):
            wash.append(dishes.pop())
    
    # 두번째 입력이 2면 wash 리스트에서 pop -> dry 리스트에 push
    elif a == 2:
        for _ in range(b):
            dry.append(wash.pop())
    
        




