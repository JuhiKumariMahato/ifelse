n=int(input("enter a 3 digit no"))
f=0
m=n
while n>0:
    rem=n%10
    n=n//10
    if(rem%2==0):
        f=1
        break
if f==0:
    print("all digits are odd")
else:
    print("some of the digits are even")
    

    
        
        
    
