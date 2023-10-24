def fuction(n):
    if n > 1:
        print(n)
        return fuction(n-1)
    else:
        print(n)
        return

fuction(4)


# 첫번째 방법
def factorial(num):
    if num <= 1:
        return num
    else:
        return num * factorial(num-1)

for num in range(10):
    print(factorial(num))
    
# 두번째 방법
def factorial2(num):
    if num > 1:
        return num * factorial2(num-1)
    
    return num

for num in range(10):
    print(factorial2(num))

