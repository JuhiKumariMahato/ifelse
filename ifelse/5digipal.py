n=int(input("enter the number"))
pal=0
x=n
while(n>0):
    r=n%10
    pal=pal*10+r
    n=n//10
if(pal==x):
    print("the no is pallindromr")
else:
    print("not")
