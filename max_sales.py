
print('ВХОД:')
product = input()
product = '"' + product + '"'
filename = './1-sales.txt' #input()
min_city = ''
min_price = 0.0
with open(filename, encoding='utf-8') as f:
    for line in f:
        if not line.isspace():
            code, country, city, sale_date, price, *_ = line.split(',')
            if code == product:
                if min_price == 0.0:
                    min_price = float(price)
                    min_city = city
                else:
                    if float(price) <= min_price:
                        min_price = float(price)
                        min_city = city
print('РЕЗУЛТАТ:')
print(min_city)


