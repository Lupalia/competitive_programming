from sympy import nextprime
t=input(":")
res=[]
alphdict={0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z"}
for i in range(1,int(t)+1):
    n,l=input().split()
    values=input().split()
    p1=2
    alphabet=set()
    while int(values[0])%p1!=0:
        p1=nextprime(p1)
    else:
        product=[[p1,int(values[0])/p1]]
        if int(values[1])%product[0][1]==0:
            product.append([product[0][1],int(values[1])/product[0][1]])
            alphabet.add(product[0][0])
            alphabet.add(product[1][0])
            alphabet.add(product[1][1])
        else:
            product[0].reverse()
            product.append([product[0][1],int(values[1])/product[0][1]])
        for num in range(2,int(l)):
            product.append([product[num-1][1],int(values[num])/product[num-1][1]])
            alphabet.add(product[num][1])
    alphabet=list(alphabet)
    alphabet.sort()
    end=alphdict[alphabet.index(product[0][0])]
    for num in range(len(product)):
        end+=alphdict[alphabet.index(product[num][1])]
    res.append(end)
for h in range(1,len(res)+1):
    print(f"Case #{h}:",res[h-1])

