num = int(input("Enter a number: "))  
sum = 0  
i = num  
while i > 0:  
   digit = i % 10  
   sum += digit ** 3  
   i //= 10  
  
if num == sum:  
   print(" Armstrong number")  
else:  
   print(" Not Armstrong number")  