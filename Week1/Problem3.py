a = list(map(int,input().split()))

def ocheck(a):
    for i in len(a):
        for j in len(a):
            if i!=j:
                product = a[i]*a[j]
                if product%2!=0:
                    return True
    return False

print(ocheck(a))
