
def fibonacci(n):
    n1 = 0
    n2 = 1
    count = 0
    if n < 0:
        print("that ain't it Chief")
    else:
        while count < n:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count +=1
    return n1
