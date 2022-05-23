nvek=input(":").split()
n=int(nvek[0])
k=int(nvek[1])
b=k
c=""
d=1
while b>=9:
    c+="9"
    b-=9
if b<9 and b>0:
    c+=str(b)
if len(c)>n:
    print(0)
else:
    c+=(n-len(c))*"0"  
    c=list(c)
    for item in range(len(c)):
        c[item]=int(c[item])
    for num in range(len(c)):
        while num!=len(c)-1 and c[num]!=0 and c[num+1]!=9:
            c[num]=c[num]-1
            c[num+1]=c[num+1]+1
            d+=1
    print(d)