str1 = input('дай първия стринг > ')
str2 = input('дай сега втория > ')
try:
    print( str1[str1.rindex(str2)+len(str2):])
except ValueError:
    print('substring not found')
