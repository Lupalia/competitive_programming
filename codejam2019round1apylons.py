snumber=0
pbility=0
win=1
winlist=[]
def jump(table,startpos):
        global win
        global winlist
        global pbility
        global snumber
        global prevhamle
        global i
        check=0
        o1=startpos[0]
        p1=startpos[1]
        prevhamle.append(startpos)
        potentialjumplist=[s for s in table]
        potentialjumplist.remove(startpos)
        if win==len(table):
            print(f"Case #{i+1}: POSSIBLE")
            for item in winlist:
                print(item[0],item[1])
            return None
        for potentialjump in potentialjumplist:
            if potentialjump in prevhamle:
                continue
            o2=potentialjump[0]
            p2=potentialjump[1]
            if o1==o2 or p1==p2 or o1-p1==o2-p2 or o1+p1==o2+p2:
                check+=1
                if check==len(potentialjumplist):
                    if pbility==len(potentialjumplist):
                        print(f" Case #{i+1}: IMPOSSIBLE")
                        return None
                    else:
                        pbility+=1
                        prevhamle=[]
                        jump(table,table[snumber+1])
            else:
                pbility=0
                win+=1
                winlist.append((potentialjump[0],potentialjump[1]))
                jump(table,potentialjump)
                
             
testcase=int(input(":"))
for i in range(testcase):
    prevhamle=[]
    table=[]
    r,c=[int(s) for s in input(":").split()]
    for num1 in range(r):
        for num2 in range(c):
            table.append((num1+1,num2+1))
    jump(table,table[snumber])
             
        
