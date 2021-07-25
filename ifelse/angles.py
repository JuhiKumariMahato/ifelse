a1=int(input("enter the 1st angle"))
a2=int(input("enter the 2nd angle"))
a3=int(input("enter the 3rd angle"))
s=a1+a2+a3
if(s==180 or s<180):
    if((a1>a2) and (a1>a3)):
         print("the greatest angle is" ,a1)
    elif((a2>a3) and(a2>a1)):
        print("the greatest angle is ",a2)
    elif(a3>a1) and (a3>a2):
        print("the greatest angle is ",a3)
else:
    print("invalid set of angles")


