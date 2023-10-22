import collections

while True:
    n, m, k = map(int, input().split())
    if n and m and k == 0:
        break
    person = []
    count = 0


    for i in range(1, n+1):
        person.append(i)


    for _ in range(k): 
        if len(person) <= m:
            print(person[0])
            break
        else:
            a = person.pop(m-1) # 6
            count = 0
            
        # 6, 7, 8를 지울 방법?
        for j in range(len(person)):
            if j >= m-1:
                person.insert(count, person[j])
                person.pop(j+1)
                count += 1