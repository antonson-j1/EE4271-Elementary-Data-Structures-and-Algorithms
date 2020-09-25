n = int(input())

def osqr(m):
    a=0
    for i in range(1,m,2):
        a = a+ i**2
    return a

print(osqr(n))