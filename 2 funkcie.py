def p_cisel(retazec):
    p=0
    cisla = "0,1,2,3,4,5,6,7,8,9"
    for i in range(len(retazec)):
        if retazec[i] in cisla:
            p=p+1
    return p

retazec = input("zadaj retazec: ")
print(p_cisel(retazec))