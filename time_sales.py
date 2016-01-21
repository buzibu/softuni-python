from datetime import datetime

sales = {
'1': 0,
'2': 0,
'3': 0,
'4': 0,
'5': 0,
'6': 0,
'0': 0
}

with open("sales.csv") as f:
    for line in f:
        sales_data = line.split(',')
        datetime_value = datetime.strptime(sales_data[0], '%Y-%m-%d %H:%M:%S')
        sales[datetime_value.strftime('%w')]+=float(sales_data[1])

for ind in sales:
    print("Day {} : {} sales".format(ind,sales[ind]))
    
    