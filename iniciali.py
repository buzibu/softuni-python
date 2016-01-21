name = input("Въведете име: ")
mletter = ''
for a in range(0,len(name)):
    if a==0 and name[a].isalpha():
        mletter = mletter+name[a].upper()+'.'
    else:
        if name[a-1] == ' ' and name[a].isalpha():
            mletter = mletter+name[a].upper()+'.'
print("Инициали: %s" % mletter)
