n, k = input("").split()
b = input("").split()
result = 0
for item in b:
    if int(item) > 0 and int(item) >= int(b[int(k) - 1]):
        result += 1
print(result)
