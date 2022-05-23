a=input(":")
b=[]
c=[]
for num in range(int(a)):
    b.append(input(":"))
for item in range(len(b)):
    b[item]=int(b[item])
for item in b:
    c.append((item+1)/2)
for num in c:
    print(int(3*(2*num**2-1)-6))
print("whe")
