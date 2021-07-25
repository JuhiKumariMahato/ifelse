n=int(input("enter the no u want to check"))
f=0
if (n>0) :
    print("positive no")
    if(n%2!=0) and (n%5==0):
        print("the no is odd as well as divisible by 5")
    else:
        print("not divisible")
elif(n<0):
    print("negative no")
elif(n==0):
    print("zero")

