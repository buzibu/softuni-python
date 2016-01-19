def main():
    
    price_list = []
    suma = 0
    while True:
        price = input("Дай цената (stop за край)> ")
        if price == 'stop':
            break
        else:
            if price.isdigit():
                price_list.append(int(price))
            else:
                print("Невалидна цена: %s" % price)

    print(price_list)

    price_list.sort()
    print('Sorted')
    print(price_list)

    while price_list[0] == price_list[1]:
        print("Премахната най-ниска цена: %s (повтаря се)" % price_list[0])
        price_list.pop(0)
        print(price_list)

    while price_list[-1] == price_list[-2]:
        print("Премахната най-висока цена: %s (повтаря се)" % price_list[0])
        price_list.pop(len(price_list)-1)
        print(price_list)

    print('Тези са за смятане на средната стойност')
    print(price_list[1:-1])

    if len(price_list) < 4:
        print("Много малко цени си въвел бе братле, трябват минимум 4, и то без да се броят повтарящите се (ако се падат най-голяма или най-малка)")
        return
    else:
        for pr in price_list[1:-1]:
            suma = suma + pr
        average_price = suma/len(price_list[1:-1])

    print("Най-ниска цена: %s" % price_list[0])
    print("Най-висока цена: %s" % price_list[-1])
    print("Средна цена на останалите: %s" % average_price)

if __name__ == "__main__":
    main()
