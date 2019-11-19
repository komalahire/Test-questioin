number=[10,6,4,0,3,9,2,7,5,1,8]
j=0
while j<len(number):
    i=j+1
    while i<len(number):
        if number[j]>number[i]:
            a=number[i]
            number[i]=number[j]
            number[j]=a
        i=i+1
    j=j+1
print(number)