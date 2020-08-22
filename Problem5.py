'''
Q5
Write a Python program that takes as input three integers, “a”, “b” and “c”, from the console and
determines if they can be used in the following arithmetic formulas: (i) “a+b=c”, (ii) “a=b-c”, (iii) “a*b=c”.
'''

a= list(map(int,input().split()))

if a[0]+a[1] == a[2]:
    print("a+b=c or {}+{}={}".format(a[0],a[1],a[2]))
if a[0]+a[2] == a[1]:
    print("a=b-c or {}={}-{}".format(a[0],a[1],a[2]))
if a[0]*a[1] == a[2]:
    print("a*b=c or {}*{}={}".format(a[0],a[1],a[2]))