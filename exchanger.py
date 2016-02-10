rates_filename = input()
exchange_rates = {}
with open(rates_filename, encoding='utf-8') as f:
    for line in f:
        if not line.isspace():
            key, exrate, *_ = line.split()
            exchange_rates[key] = float(exrate)
money_file = input()
with open(money_file) as f2:
    for line in f2:
        if not line.isspace():
            amount, valuta, *_ = line.split()
            print("{:.2f}".format(float(amount)/exchange_rates[valuta]))
