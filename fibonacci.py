n=int(input("enter the number of terms for the fibonacci series"))
n1=0
n2=1
if n==1:
    print("0")
else:
    while n!=0:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        n=n-1
