n=int(input("Enrer the number of terms"))
a,b=-1,1
for i in range(1,n+1):
    c=a+b
    print(c,end='\n')
    a=b
    b=c