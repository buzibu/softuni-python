import math

aa = input()
bb = input()
cc = input()
try:
    a = float(aa)
    b = float(bb)
    c = float(cc)
except ValueError:
    print('INVALID INPUT')
else:
    if (a + b) <= c or (a + c) <= b or (b + c) <= a:
        print('INVALID INPUT')
    else:
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("{:.2f}".format(S))
