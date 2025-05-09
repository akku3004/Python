num=int(input("Enter a num :"))
sum=0
while num>0:
    sum += num % 10   
    num//=10
print("sum of digits :",sum)    