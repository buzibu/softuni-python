my_text = input('ВХОД:')

if my_text == '' or my_text.isspace():
    print('INVALID INPUT')
else:
    my_dict = {}
    for ch in my_text:
        if ch in my_dict:
            my_dict[ch] += 1
        else:
            my_dict[ch] = 1
    most_used = max(my_dict, key=my_dict.get)
    if most_used == ' ':
        print('space')
    else:
        print(most_used)
