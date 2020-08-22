'''
What parameter values should be sent to the range constructor to produce a range with values:
(a) 60,70,80
(b) 4,2,0,-2,-4
'''

# 2.a
a=[] 
for i in range(60,81,10):
    a.extend([i])
print(*a) #for checking the values

# 2.b
b=[]
for i in range(4,-5,-2):
    b.extend([i])
print(*b) #for checking the values