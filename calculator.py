a=int(input("enter first number"))
b=int(input("enter second number"))
choose=input("choose number 1 for addition ,2 for subtraction ,3 for multiplication , 4 for division")

if choose=='1':
    result=a+b
elif choose=='2':
    result=a-b
elif choose=='3':
    result=a*b
elif choose=='4':
    if b!=0:
        result=a/b
    else:
       result=("divison by zero not possible")
else:
    print("error")

print("result",result)
