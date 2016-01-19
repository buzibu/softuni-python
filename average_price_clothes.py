import csv
sum_price = 0.0
count_items = 0
with open('./catalog_full.csv', newline='') as csvfile:
    f = csv.reader(csvfile, delimiter=',', quotechar='"')
    for line in f:
        #print(line)
        sum_price += float(line[6])
        #print(sum_price)
        count_items += 1
print('Items: {}, Средна цена: {}'.format(count_items,sum_price/count_items))
