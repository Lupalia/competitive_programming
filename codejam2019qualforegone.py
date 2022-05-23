a=input(":")
b=[]
e=""
g=""
f=True
for num in range(int(a)):
    b.append(input(":"))
for item in b:
    c=[]
    d=[]
    e=""
    g=""
    f=True
    for harf in item:
        if harf!="4":
            c.append(harf)
            d.append("0")
        else:
            c.append("3")
            d.append("1")
        
    for item in c:
        e+=item
    e=int(e)
    for item in d:
        while f:
            if item!=0:
                f=False
                g+=item
                break
                
            else:
                pass
        else:
            g+=item
    if g!="": 
        g=int(g)
    print(e,g)
