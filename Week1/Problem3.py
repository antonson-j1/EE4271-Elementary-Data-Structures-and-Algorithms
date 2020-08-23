a = list(map(int,input().split()))

def ocheck(a):
    for i in a:
        for j in a:
            if i!=j:
                product = i*j
                if product%2!=0:
                    return True
    return False

print(ocheck(a))
