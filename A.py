a=input(":").split("\n")
b=[]
d=0
n=int(a[0].split()[0])
m=int(a[0].split()[1])
a.pop(0)
for num in range(n):
    t=a[num].split()
    c=(int(t[0])**2+int(t[1])**2+int(t[2])**2)**0.5
    b.append(c)
for item in b:
    if item<=m/2:
        d+=1
print(d)