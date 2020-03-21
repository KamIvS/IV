import random
from random import randint
from itertools import product
i = int(input())
j = 0
j += i
list10d = ['крестьянин', 'ob', 'ferd']
mobexptip = [['10g', '10n', list10d[random.randint(0,2)], '10z', '10m', '10a', '10v', '10r', '10s', '10ne', '10k', '10e', '10i', '10f'],
     ['25g', '25n', '25d', '25z', '25m', '25a', '25v', '25r', '25s', '25ne', '25k', '25e', '25i', '25f'],
     ['50g', '50n', '50d', '50z', '50m', '50a', '50v', '50r', '50s', '50ne', '50k', '50e', '50i', '50f'],
     ['100g', '100n', '100d', '100z', '100m', '100a', '100v', '100r', '100s', '100ne', '100k', '100e', '100i', '100f'],
     ['200g', '200n', '200d', '200z', '200m', '200a', '200v', '200r', '200s', '200ne', '200k', '200e', '200i', '200f'],
     ['450g', '450n', '450d', '450z', '450m', '450a', '450v', '450r', '450s', '450ne', '450k', '450e', '450i', '450f'],
     ['700g', '700n', '700d', '700z', '700m', '700a', '700v', '700r', '700s', '700ne', '700k', '700e', '700i', '700f'],
     ['1100g', '1100n', '1100d', '1100z', '1100m', '1100a', '1100v', '1100r', '1100s', '1100ne', '1100k', '1100e', '1100i', '1100f'],
     ['1800g', '1800n', '1800d', '1800z', '1800m', '1800a', '1800v', '1800r', '1800s', '1800ne', '1800k', '1800e', '1800i', '1800f'],
     ['2300g', '2300n', '2300d', '2300z', '2300m', '2300a', '2300v', '2300r', '2300s', '2300ne', '2300k', '2300e', '2300i', '2300f'],
     ['2900g', '2900n', '2900d', '2900z', '2900m', '2900a', '2900v', '2900r', '2900s', '2900ne', '2900k', '2900e', '2900i', '2900f'],
     ['3900g', '3900n', '3900d', '3900z', '3900m', '3900a', '3900v', '3900r', '3900s', '3900ne', '3900k', '3900e', '3900i', '3900f'],
     ['5000g', '5000n', '5000d', '5000z', '5000m', '5000a', '5000v', '5000r', '5000s', '5000ne', '5000k', '5000e', '5000i', '5000f'],
     ['5900g', '5900n', '5900d', '5900z', '5900m', '5900a', '5900v', '5900r', '5900s', '5900ne', '5900k', '5900e', '5900i', '5900f'],
     ['7200g', '7200n', '7200d', '7200z', '7200m', '7200a', '7200v', '7200r', '7200s', '7200ne', '7200k', '7200e', '7200i', '7200f'],
     ['8400g', '8400n', '8400d', '8400z', '8400m', '8400a', '8400v', '8400r', '8400s', '8400ne', '8400k', '8400e', '8400i', '8400f'],
     ['10000g', '10000n', '10000d', '10000z', '10000m', '10000a', '10000v', '10000r', '10000s', '10000ne', '10000k', '10000e', '10000i', '10000f'],
     ['11500g', '11500n', '11500d', '11500z', '11500m', '11500a', '11500v', '11500r', '11500s', '11500ne', '11500k', '11500e', '11500i', '11500f'],
     ['13000g', '13000n', '13000d', '13000z', '13000m', '13000a', '13000v', '13000r', '13000s', '13000ne', '13000k', '13000e', '13000i', '13000f'],
     ['15000g', '15000n', '15000d', '15000z', '15000m', '15000a', '15000v', '15000r', '15000s', '15000ne', '15000k', '15000e', '15000i', '15000f'],
     ['18000g', '18000n', '18000d', '18000z', '18000m', '18000a', '18000v', '18000r', '18000s', '18000ne', '18000k', '18000e', '18000i', '18000f'],
     ['20000g', '20000n', '20000d', '20000z', '20000m', '20000a', '20000v', '20000r', '20000s', '20000ne', '20000k', '20000e', '20000i', '20000f'],
     ['22000g', '22000n', '22000d', '22000z', '22000m', '22000a', '22000v', '22000r', '22000s', '22000ne', '22000k', '22000e', '22000i', '22000f'],
     ['25000g', '25000n', '25000d', '25000z', '25000m', '25000a', '25000v', '25000r', '25000s', '25000ne', '25000k', '25000e', '25000i', '25000f'],
     ['33000g', '33000n', '33000d', '33000z', '33000m', '33000a', '33000v', '33000r', '33000s', '33000ne', '33000k', '33000e', '33000i', '33000f'],
     ['41000g', '41000n', '41000d', '41000z', '41000m', '41000a', '41000v', '41000r', '41000s', '41000ne', '41000k', '41000e', '41000i', '41000f'],
     ['50000g', '50000n', '50000d', '50000z', '50000m', '50000a', '50000v', '50000r', '50000s', '50000ne', '50000k', '50000e', '50000i', '50000f'],
     ['62000g', '62000n', '62000d', '62000z', '62000m', '62000a', '62000v', '62000r', '62000s', '62000ne', '62000k', '62000e', '62000i', '62000f'],
     ['75000g', '75000n', '75000d', '75000z', '75000m', '75000a', '75000v', '75000r', '75000s', '75000ne', '75000k', '75000e', '75000i', '75000f'],
     ['90000g', '90000n', '90000d', '90000z', '90000m', '90000a', '90000v', '90000r', '90000s', '90000ne', '90000k', '90000e', '90000i', '90000f'],
     ['105000g', '105000n', '105000d', '105000z', '105000m', '105000a', '105000v', '105000r', '105000s', '105000ne', '105000k', '105000e', '105000i', '105000f'],
     ['120000g', '120000n', '120000d', '120000z', '120000m', '120000a', '120000v', '120000r', '120000s', '120000ne', '120000k', '120000e', '120000i', '120000f'],
     ['135000g', '135000n', '135000d', '135000z', '135000m', '135000a', '135000v', '135000r', '135000s', '135000ne', '135000k', '135000e', '135000i', '135000f'],
     ['155000g', '155000n', '155000d', '155000z', '155000m', '155000a', '155000v', '155000r', '155000s', '155000ne', '155000k', '155000e', '155000i', '155000f']]
list1 = [10, 25, 50, 100, 200]
list2 = [450, 700, 1100, 1800, 2300]
list3 = [2900, 3900, 5000, 5900, 7200]
list4 = [8400, 10000, 11500, 13000, 15000, 18000, 20000, 22000, 25000, 33000]
list5 = [41000, 50000, 62000, 75000, 90000, 105000, 120000, 135000, 155000]
listexp = []
listtip = ['a', 'n', 'y', 't']
listexp1 = []
listmob = []
list10e = []
list10f = []
list10d = ['крестьянин', 'обываетль', 'фьерд']
list10k = []
amountmob = 0
difficulty = 0
x = (random.choice(list5) or (list4))
if  i >= 62000:
    while i >= 41000:
        x = random.choice(list5) or (list4)
        while i < x:
            x = (random.choice(list5) or (list4))
        i -= x
        listexp.append(x)
    while i >= 2900:
        x = random.choice(list3)
        while i < x:
            x = (random.choice(list3))
        i -= x
        listexp.append(x)
    while i >= 450:
        x = random.choice(list2)
        while i < x:
            x = (random.choice(list2))
        i -= x
        listexp.append(x)
    while i >= 0:
        x = (random.choice(list1))
        i -= x
        listexp.append(x)
    print (listexp)
elif 62000 > i >= 18000:
    while i >= 8400:
        x = random.choice(list4) or (list3)
        while i < x:
            x = (random.choice(list4) or (list3))
        i -= x
        listexp.append(x)
    while i >= 2900:
        while i < x:
            x = (random.choice(list3))
        i -= x
        listexp.append(x)
    while i >= 450:
        while i < x:
            x = (random.choice(list2))
        i -= x
        listexp.append(x)
    while i >= 0:
        x = (random.choice(list1))
        i -= x
        listexp.append(x)
    print (listexp)
elif 18000 > i >= 5000:
    while i >= 2900:
        while i < x:
            x = (random.choice(list3) or (list2))
        i -= x
        listexp.append(x)
    while i >= 450:
        while i < x:
            x = (random.choice(list2))
        i -= x
        listexp.append(x)
    while i >= 0:
        x = (random.choice(list1))
        i -= x
        listexp.append(x)
    print (listexp)
elif 5000 > i >= 450:
    while i >= 450:
        while i < x:
            x = (random.choice(list2)or(list1))
        i -= x
        listexp.append(x)
    while i > 0:
        while i < x:
            x = (random.choice(list1))
        i -= x
        listexp.append(x)
        if i < 10:
            break
    print (listexp)
elif i > 0:
    x = (random.choice(list1))
    while i > 0:
        while i < x:
            x = (random.choice(list1))
        i -= x
        listexp.append(x)
        if i < 10:
            break
    print(listexp)
listexp1 = sorted(listexp, reverse=True)
for i in range (len(listexp)):
    if listexp[i] == 10:
        listexp[i] = 0
    elif listexp[i] == 25:
        listexp[i] = 1
    elif listexp[i] == 50:
        listexp[i] = 2
    elif listexp[i] == 100:
        listexp[i] = 3
    elif listexp[i] == 200:
        listexp[i] = 4
    elif listexp[i] == 450:
        listexp[i] = 5
    elif listexp[i] == 700:
        listexp[i] = 6
    elif listexp[i] == 1100:
        listexp[i] = 7
    elif listexp[i] == 1800:
        listexp[i] = 8
    elif listexp[i] == 2300:
        listexp[i] = 9
    elif listexp[i] == 2900:
        listexp[i] = 10
    elif listexp[i] == 3900:
        listexp[i] = 11
    elif listexp[i] == 5000:
        listexp[i] = 12
    elif listexp[i] == 5900:
        listexp[i] = 13
    elif listexp[i] == 7200:
        listexp[i] = 14
    elif listexp[i] == 8400:
        listexp[i] = 15
    elif listexp[i] == 10000:
        listexp[i] = 16
    elif listexp[i] == 11500:
        listexp[i] = 17
    elif listexp[i] == 13000:
        listexp[i] = 18
    elif listexp[i] == 15000:
        listexp[i] = 19
    elif listexp[i] == 18000:
        listexp[i] = 20
    elif listexp[i] == 20000:
        listexp[i] = 21
    elif listexp[i] == 22000:
        listexp[i] = 22
    elif listexp[i] == 25000:
        listexp[i] = 23
    elif listexp[i] == 33000:
        listexp[i] = 24
    elif listexp[i] == 41000:
        listexp[i] = 25
    elif listexp[i] == 50000:
        listexp[i] = 26
    elif listexp[i] == 62000:
        listexp[i] = 27
    elif listexp[i] == 75000:
        listexp[i] = 28
    elif listexp[i] == 90000:
        listexp[i] = 29
    elif listexp[i] == 105000:
        listexp[i] = 30
    elif listexp[i] == 120000:
        listexp[i] = 31
    elif listexp[i] == 135000:
        listexp[i] = 32
    elif listexp[i] == 155000:
        listexp[i] = 33
print (listexp)
amountmob = len(listexp1)
if amountmob == 2:
    difficulty = (listexp1[0] + listexp1[1]) * 0.5 + j
elif 6 >= amountmob >= 3:
    difficulty = (listexp1[0] + listexp1[1] + listexp1[2]) + j
elif 10 >= amountmob >= 7:
    difficulty = (listexp1[0] + listexp1[1] + listexp1[2] + listexp1[3] ) * 1,5 + j
elif 14 >= amountmob >= 11:
    difficulty = (listexp1[0] + listexp1[1] + listexp1[2] + listexp1[3] + listexp1[4]) * 2 + j
elif  amountmob >= 15:
    difficulty = (listexp1[0] + listexp1[1] + listexp1[2] + listexp1[3] + listexp1[4] + listexp1[5]) * 2.5 + j
print(listexp1)
print(amountmob)
print ('сложность боя', '=', difficulty)
i = 0
for o in range (len(listexp)):
    randomtip = random.randint(0, 13)
    listmob.append(mobexptip[listexp[i]][randomtip])
    i += 1
print (listmob)
n = 0
for i in range(len(listmob)):
    if listmob[n] == 'крестьянин':
        print ('\t', '\t', 'крестьянин','\n','класс доспеха: 10','\n', 'хиты: 5', '\n', 'скорость: 30 фт')
    elif listmob[n] == 'ob':
        print ('\t', '\t', 'обыватель','\n','класс доспеха: 10','\n', 'хиты: 5', '\n', 'скорость: 30 фт')
    elif listmob[n] == 'ferd':
        print ('\t', '\t', 'фьерд','\n','класс доспеха: 10','\n', 'хиты: 5', '\n', 'скорость: 30 фт')
    n += 1





















