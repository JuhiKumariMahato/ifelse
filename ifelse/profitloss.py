cp=int(input("enter the cost price"))
sp=int(input("enter the selling price"))
if(cp>sp):
    loss=cp-sp
    print("u are in loss,nd ur loss is",loss)    
elif(sp>cp):
    profit=sp-cp
    print("u are in profit,nd ur profit is",profit)
else:
    print("u are neither in loss nor at profit")
    
