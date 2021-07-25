age=int(input("enter your age"))
count=0
for i in range(age,18):
    count=count+1
if(age>=18):
    print("u are eligible to vote")
else:
    print("u are not eligible to vote until u are",count)
    
