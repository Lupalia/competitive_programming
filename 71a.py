n = input("")
b = []
for s in range(int(n)):
    b.append(input(""))
for item in b:
    if len(item) > 10:
        print(item[0] + str(len(item) - 2) + item[-1])
    else:
        print(item)
