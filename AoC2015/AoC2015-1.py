i = 0
tall = 0
kjeller = False

value = input("Skriv inn: ")
value.split()
for e in value:
    tall=tall+1
    if e == "(":
        i = i+1
    elif e == ")":
        i = i-1
    
    if (i < 0):
        if not kjeller:
            kjeller = True
            print("Kjeller: " + str(tall))


print(i)