import random

a="abcdefghijklmnopqrstuvwxyz0123456789"
length=int(input("enter password length"))

password =''.join(random.sample(a,length))
print(" your password is ",password)

        
