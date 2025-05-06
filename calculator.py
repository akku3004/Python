#calculator
num1,num2=map(float,input("Enter your numbers:").split())
op=(input("+,-,*,/: "))
if op =='+':
    print('result',num1+num2)
elif op=='-':
    print('result',num1-num2)   
elif op=='*':
    print('result',num1*num2)   
elif op=='/':
    if num2==0:
        print("cannot divide by zero")
    else:    
        print('result',num1/num2)             