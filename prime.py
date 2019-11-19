user_input = input("enter your number")
i = 2
while i < (user_input):
    if user_input % i == 0:
        print ("not prime number")
        break
    i = i + 1
else:
    print ("prime number")        
