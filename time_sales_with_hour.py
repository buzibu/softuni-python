from datetime import datetime

sales = {

}

with open("sales.csv") as f:
    for line in f:
        sales_data = line.split(',')
        datetime_value = datetime.strptime(sales_data[0], '%Y-%m-%d %H:%M:%S')
        dict_key = datetime_value.strftime('%w %H')
        if dict_key in sales:
            sales[dict_key] += float(sales_data[1])
        else:
            sales[dict_key] = float(sales_data[1])

maximum = 0.0
maxday = ''

for ind in sales:
    print("Time {} : {} sales".format(ind,sales[ind]))
    if sales[ind] > maximum:
        maximum = sales[ind]
        maxday = ind

print('Maximum sales {} on Time {}'.format(maximum,maxday))