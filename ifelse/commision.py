dis=int(input("enter the distance"))
if(dis<=10):
    print("yr commission is 150")
elif(dis>10 and dis<=40):
    com1=(dis-10)*5
    print("ur commision is",150+com1)
elif(dis>40 and dis<=100):
    com2=(dis-40)*7
    print("ur commission is",300+com2)
elif(dis>100):
    com3=(dis-100)*20
    print(" ur commission is",500+com3)
        
