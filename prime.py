n=int(input("Enter ypur number:"))
pr=True
if n>2:
    for i in range(2,n):
        if n%i==0:
            pr = False
            break
    if pr:
        print("Number is prime")
    else:
        print("not prime")        