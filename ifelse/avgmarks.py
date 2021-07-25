s1=int(input("enter 1st sub marks"))
s2=int(input("enter 2nd sub marks"))
s3=int(input("enter 3rd sub marks"))
s4=int(input("enter 4th sub marks"))
s5=int(input("enter 5th sub marks"))
avg=(s1+s2+s3+s4+s5)//5
if(avg>=60):
    print("1st div")
elif(avg>=45):
    print("2nd div")
elif(avg>=30):
    print("3rd div")
elif(avg<30):
    print("fail")
