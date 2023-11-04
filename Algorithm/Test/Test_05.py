import sys

input = sys.stdin.readline

while True:
    n = int(input())
    
    if n == 0:
        break
    
    card = [i for i in range(1,51)]
    

    start, end = card[0], card[-1]
    
    while card:
        mid = (start+end) // 2
        print(mid)
        if mid == n:
            break
        elif mid < n:
            start = mid + 1
        elif mid > n:
            end = mid - 1
        
        
