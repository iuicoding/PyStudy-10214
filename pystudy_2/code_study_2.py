a = float(input('a'))
b = float(input('b'))
c = float(input('c'))

print('michael jackson', a, b, c)
print('michael jordan')

score = int(input('score'))


if score == 2:
    print(score*a)
elif score <= 2:
    print(score*b)
elif score >= 2:
    print('horray')
else:
    print('what!')
if a >= score:
    print('sdfsdfsdfsdfsdfsdf')
elif a <= score:
    print('123')
else:
    a = b
    print(b)

gogangmin = 1
puyopuyo = int(input('puyopuyo combo'))
if puyopuyo > 10:
    print('gogangmin dead by daylight number', puyopuyo-gogangmin)
elif puyopuyo == 10:
    print('gogangmin die on perfect', puyopuyo)
else:
    print('goganmin overpowered puyupuyo by', puyopuyo*puyopuyo)
t = float(input('t'))
bb = float(input('bb'))
cc = float(input('cc'))
s = (t+bb+cc)/2
A = (s*(s-t)*(s-bb)*(s-cc))**(1/2)
print(A)

MS = 37
SS = 22
LS = 31
steroid = 2

print(MS*steroid+SS*steroid+LS*steroid, "you can't stop michael jordan")
list_basket = []
michael = 37
kobe = 35
curry = 32
miller = 24
lebron = 31
plus = 0
for i in range(5 + plus):
    Ba = (input('choose your basket hero(michael, kobe, curry, miller, lebron)'))
    if Ba == 'michael':
        list_basket.append(michael)
    elif Ba == 'curry':
        list_basket.append(curry)
    elif Ba == 'kobe':
        list_basket.append(kobe)
    elif Ba == 'miller':
        list_basket.append(miller)
    elif Ba == 'lebron':
        list_basket.append(lebron)
    else:
        plus = plus + 1
Point = sum(list_basket)
if Point > 100:
    print(Point, 'you win')
elif Point == 100:
    print(Point, 'draw')
else:
    print(Point, 'you lose')
#행복나라 연두
alist = [1, 2, 3, 4, 5]
print(alist)

if 4 in alist:
    print("4가 있네")

if 121 not in alist:
    print("121없음 뭐임")

print(alist[1])

alist = alist + [1]
alist = alist * 2
alist.append(8)
print(alist)

del alist[0]
alist.remove(2)
alist.pop(4)
alist.pop()
print(alist)

print(alist + [2])
print(alist * 3)
for element in alist:
    print('eye', element)