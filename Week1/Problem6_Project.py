'''
Q6
https://en.wikipedia.org/wiki/Birthday_problem
Design a program that can test the Birthday problem, by a series of experiments, on randomly generated
birthdays which test this paradox for n = 5,10,15,20,25,30...200.
'''

def numerator(a, n):
    num=1
    b=a-n
    for i in range(b+1,a,1):
        num=num*i
    return float(num)

def denominator(a, n):
    den=1
    for i in range(n-1):
        den= den*a
    return float(den)

def probability(n, numberofdays):
    if n<=120:  #ease of computation & Precise answers for values less than or equal to 120
        num= numerator( numberofdays ,n)
        den= denominator( numberofdays ,n)
        probab= 1- num/den
        return probab*100
    else:       #Not so precice, but can be computed for larger numbers easily
        probab_inv=1
        for i in range(n):
            probab_inv= probab_inv*(1 - float(n)/float(numberofdays))
        return "(100 -{})".format(probab_inv)

print(str(probability(int(input()),365))+ "%")