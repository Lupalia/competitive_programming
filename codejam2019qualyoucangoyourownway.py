a=input(":")
dim=[]
gring=[]
for num in range(int(a)):
    dim.append(input(":"))
    gring.append(input(":"))
for item in range(int(a)):
    outy=""
    for num in range(2*int(dim[item])-2):
        if gring[item][num]=="S":
            outy+="E"
        else:
            outy+="S"
    print("Case #{}:".format(item+1),outy)
    
