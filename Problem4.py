def findvowel(a):
    a = a.lower()
    arr= [char for char in a]
    count=0
    for i in a:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count+=1
    return count

print(findvowel(input()))