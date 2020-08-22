a = list(map(int,input().split()))

def ocheck(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if i!=j:
                product = a[i]*a[j]
                if product%2!=0:
                    return True
    return False

print(ocheck(a))
