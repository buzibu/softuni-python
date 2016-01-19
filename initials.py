name = input("Как се казваш? > ")
short_name = ""

for indx, ch in enumerate(name):
    if indx ==0:
        short_name += ch.upper() + "."
    else:
        if ch.isalpha() and name[indx-1]==' ':
            short_name += ch.upper() + "."

print(short_name)
