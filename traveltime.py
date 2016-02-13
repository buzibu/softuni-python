print('ВХОД:')
filename = '301-2-distances.txt' #input()
time_to_travel = 0.0

with open(filename, encoding='utf-8') as f:
    for line in f:
        if not line.isspace():
            from_point, to_point, speed, *_ = line.split(',')
            print('{}, {}, {}'.format(from_point, to_point, speed))
            time_to_travel += (int(to_point)-int(from_point)+1)/int(speed)
print('РЕЗУЛТАТ:')
print("{:.2f}".format(time_to_travel))