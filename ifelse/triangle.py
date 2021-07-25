a1=int(input("enter the 1st angle"))
a2=int(input("enter the 2nd angle"))
a3=int(input("enter the 3rd angle"))
s=a1+a2+a3
if(s==180 or s<180):
    print("valid triangle")
    if(a1==a2 and a2==a3):
        print("equilateral triangle")
    elif(a1!=a2 and a2!=a3):
        print("scalene triangle")
    elif(a1==a2 or a2==a3 or a3==a1):
        print("isosceles tringle")
else:
    print("invalid")
        
