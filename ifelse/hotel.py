days=int(input("enter the no of days u stayed here "))
n=int(input("select 1 2 3 4 respectively for ac room,suite,villa,super delux villa"))
if(n==1):
    bill=1800*days+((5.5*1800)/100)
    print("total charges=",bill)
elif(n==2):
    bill=2000*days+((12.5*2000)/100)
    print("total charges=",bill)
elif(n==3):
    bill=2200*days+((18*2200)/100)
    print("total charges=",bill)
elif(n==4):
    bill=3000*days+((28*3000)/100)
    print("total charges=",bill)

