n = int(input())

def sqr(m):
    a=0
    for i in range(1,m):
        a= a+ i**2
    return a

print(sqr(n))