'''
Q6
https://en.wikipedia.org/wiki/Birthday_problem
Design a program that can test the Birthday problem, by a series of experiments, on randomly generated
birthdays which test this paradox for n = 5,10,15,20,25,30...200.
'''
import random

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
        return probab_inv

# print("Enter the number of Random PPL: ")
# n1= int(input())

print("Enter the number of iterations to check on: ")
largetest= int(input())

# randomlist = random.sample(range(10, 201, 5), n1)
# print(randomlist)

for i in range(10, 201, 5):
    print("The number selected= "+ str(i))
    p=[]

    for m in range(largetest):
        birthdays=[]
        for k in range(i):
            birthdays.extend([random.randrange(0,365)])
        
        if any(birthdays.count(element) > 1 for element in birthdays): #len(birthdays) != len(set(birthdays)):
            p.append(True)
        else:
            p.append(False)

    print(str(float(sum(p))/float(largetest)*100)+ "%" +"  on test")
    
    if i<=120:
        print(str(probability(i,365))+ "%" + "  on theory \n")
        print("Theory - test= " + str(probability(i,365) -float(sum(p))/float(largetest)*100) + "% \n\n")
    else:
        print("(100 - "+ str(probability(i,365))+ ") %" + "  on theory \n")
        print("Theory - test= " + str(100 - probability(i,365) -float(sum(p))/float(largetest)*100) + "% \n\n")