# print even no
num=(int(input("Enter your number")))
i=2
while i<=num:
    print(i)
    i+=2
    
    # optimize
num=(int(input("Enter your number")))
for i in range(2,num,2):
     print(i)