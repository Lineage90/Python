def hanoi_t(n, start, end) :
    if n == 1 :
        print(start, end)
        return

    hanoi_t(n-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    hanoi_t(n-1, 6-start-end, end) # 3단계
    
n = int(input())
print(2**n-1) # 총 이동 횟수
hanoi_t(n, 1, 3)


