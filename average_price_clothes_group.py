import csv
sum_price = 0.0
count_items = 0

sum_infant = 0.0
sum_kid = 0.0
sum_men = 0.0
sum_unisex = 0.0
sum_woman = 0.0

count_infant = 0
count_kid = 0
count_men = 0
count_unisex = 0
count_woman = 0

with open('./catalog_full.csv', newline='') as csvfile:
    f = csv.reader(csvfile, delimiter=',', quotechar='"')
    for line in f:

        if line[5] == "Infant":
            sum_infant += float(line[6])
            count_infant += 1
        elif line[5] == "Kid":
            sum_kid += float(line[6])
            count_kid += 1
        elif line[5] == "Men":
            sum_men += float(line[6])
            count_men += 1
        elif line[5] == "Unisex":
            sum_unisex += float(line[6])
            count_unisex += 1
        elif line[5] == "Woman":
            sum_woman += float(line[6])
            count_woman += 1
        else:
            print('Тази категория я няма: {}'.format(line[5]))
            continue
        
        #print(line)
        sum_price += float(line[6])
        #print(sum_price)
        count_items += 1

print('All items: {}, Средна цена: {}'.format(count_items,sum_price/count_items))
print('Infant: {}, Средна цена: {}'.format(count_infant,sum_infant/count_infant))
print('Kid: {}, Средна цена: {}'.format(count_kid,sum_kid/count_kid))
print('Men: {}, Средна цена: {}'.format(count_men,sum_men/count_men))
print('Unisex: {}, Средна цена: {}'.format(count_unisex,sum_unisex/count_unisex))
print('Woman: {}, Средна цена: {}'.format(count_woman,sum_woman/count_woman))
