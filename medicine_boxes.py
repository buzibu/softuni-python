filename = 'packages.txt'
print('ВХОД:')
ww = input()
hh = input()
dd = input()

try:
    w = float(ww)
    h = float(hh)
    d = float(dd)
except ValueError:
    print('INVALID INPUT')
else:
    box = [w, h, d]
    box.sort()
    print('РЕЗУЛТАТ:')
    with open(filename, encoding='utf-8') as f:
        for line in f:
            if not line.isspace():
                m_name, a, b, c, *_ = line.split(',')
                medicine = [float(a), float(b), float(c)]
                medicine.sort()
                if box[0]>medicine[0] and box[1]>medicine[1] and box[2]>medicine[2]:
                    print(m_name)





