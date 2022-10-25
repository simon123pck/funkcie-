c = int(input("Zadaj cislo: "))
retazec = input("Zadaj retazec: ")

if c > len(retazec):
    print("zly index")
else:
    print(retazec[c])


