#Q1
i=1
while i<=3:
    x=input("enter the name : ")
    i+=1
    y=len(x)
    f=1
    n=0
    while f<=y:
        if x[n]=="l" :
            x=x[0:n]+'*'+x[n+1:]
        elif x[n]=="u":
            x=x[0:n]+'*'+x[n+1:]
        elif x[n]=="u" and "l":
            x=x[0:n]+'*'+x[n+1:]    

        n=n+1
        f=f+1    
    print(x)

# --------------------------------------------
#Q2

q=int(input('inter the number : '))
while 2<=q:
    z=2
    if q==2:
        print("prime and even ")
    elif q%z==0:
        print("not prime",end=" , ")
        z+=1
        break             
    elif q%z==1:
        print("prime",end=" , ")
        break
while True:
    if q%2==0:
        print("even")
        break
    else :
        print("odd")  
        break