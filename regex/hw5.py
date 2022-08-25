import re
import sys

key_w = ['sifir', 'bir', 'iki', 'uc', 'dort', 'bes', 'alti', 'yedi', 'sekiz', 'dokuz', 'dogru', 'yanlis',
         've', 'veya',
         '(', ')',
         'degeri', 'olsun',
         'nokta',
         'arti', 'eksi', 'carpi',
         '+', '-', '*',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         'ac-parantez', 'kapa-parantez',
         'AnaDegiskenler', 'YeniDegiskenler', 'Sonuc']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(10):
    for j in range(10):
        numbers.append(str(i) + '.' + str(j))

t_numbers = ['sifir', 'bir', 'iki', 'uc', 'dort', 'bes', 'alti', 'yedi', 'sekiz', 'dokuz']

for i in range(10):
    for j in range(10):
        t_numbers.append(t_numbers[i] + ' nokta ' + t_numbers[j])

t_numerals = ['sifir', 'bir', 'iki', 'uc', 'dort', 'bes', 'alti', 'yedi', 'sekiz', 'dokuz']

booleans = ['dogru', 'yanlis']

paranthesis = ['ac-parantez', 'kapa-parantez', '(', ')']

l_operations = ['ve', 'veya']
a_operations = ['arti', 'eksi', 'carpi', '+', '-', '*']

controller = True


def baybaytatlim():
    q = open("calc.out", "w")
    q.write('Dont Let Me Down')
    sys.exit()


file = open('calc.in', 'r')
content = file.read()
lines = content.splitlines()
lines_list = []
lines_s = []  # each word split
init_dic_a = {}  # arithmetic initial
init_dic_l = {}  # logical initial
mid_dic_a = {}  # arithmetic mid
mid_dic_l = {}  # logical mid

for i in lines:
    if i == '':
        continue
    lines_list.append(i)
for i in range(len(lines_list)):
    lines_s.append((lines_list[i].split()))


if lines_list[0] != 'AnaDegiskenler':
    baybaytatlim()
if ('YeniDegiskenler' or 'Sonuc') not in lines_list:
    baybaytatlim()
if not lines_list.index('AnaDegiskenler') < lines_list.index('YeniDegiskenler') < lines_list.index('Sonuc'):
    baybaytatlim()

for i in lines_s:
    if 'nokta' in i:
        if (i[i.index('nokta') - 1] or i[i.index('nokta') + 1]) not in t_numbers:
            baybaytatlim()

init_s = lines_s[1:lines_s.index(['YeniDegiskenler'])]  # initial statements split list
mid_s = lines_s[lines_s.index(['YeniDegiskenler']) + 1:lines_s.index(['Sonuc'])]  # mid statements split list
final_s = lines_s[lines_s.index(['Sonuc'])+1:]  # final statements split list

for sentence in init_s:
    for index in range(len(sentence)):
        if sentence[index] == 'nokta':
            if index == 0:
                baybaytatlim()
            if index == len(sentence) - 1:
                baybaytatlim()


for sentence in init_s:
    for index in range(len(sentence)):
        if sentence[index] == 'nokta':
            if not sentence[index - 1] in t_numerals:
                baybaytatlim()
            if not sentence[index + 1] in t_numerals:
                baybaytatlim()

for i in init_s:
    if len(i) < 4:
        baybaytatlim()
    if '.' in i:
        baybaytatlim()

    if 'nokta' in i:
        if len(i) != 6:
            baybaytatlim()
    else:
        if len(i) != 4:
            baybaytatlim()

for i in range(len(init_s)):
    init_var_name = re.findall('[a-zA-Z0-9]{1,10}', init_s[i][0])
    if init_var_name[0] in key_w:
        baybaytatlim()
    if init_var_name[0] != init_s[i][0]:
        baybaytatlim()

    if init_s[i][2] == 'dogru':
        init_dic_l[init_var_name[0]] = 'dogru'
    elif init_s[i][2] == 'yanlis':
        init_dic_l[init_var_name[0]] = 'yanlis'

    elif init_s[i][2] in numbers:
        init_dic_a[init_var_name[0]] = str(init_s[i][2])

    elif init_s[i][2] in t_numbers:
        init_dic_a[init_var_name[0]] = str(init_s[i][2])
    else:
        baybaytatlim()

    if init_s[i][1] != 'degeri' or init_s[i][-1] != 'olsun':
        baybaytatlim()


# MID PART
for j in range(len(mid_s)):
    mid_var_name = re.findall('[a-zA-Z0-9]{1,10}', mid_s[j][0])
    if mid_var_name[0] in key_w:
        baybaytatlim()
    if mid_var_name[0] != mid_s[j][0]:
        baybaytatlim()
    for i in init_dic_a.keys():
        if i == mid_var_name[0]:
            baybaytatlim()
    for i in init_dic_l.keys():
        if i == mid_var_name[0]:
            baybaytatlim()

for sentence in mid_s:
    while 'ac-parantez' in sentence:
        sentence[sentence.index('ac-parantez')] = '('
    while 'kapa-parantez' in sentence:
        sentence[sentence.index('kapa-parantez')] = ')'

n_parantez = 0

mid_bool_var_names = []
mid_a_var_names = []

for sentence in mid_s:

    if sentence[1] != 'degeri':
        baybaytatlim()

    if sentence[-1] != 'olsun':
        baybaytatlim()
    for word in sentence:
        if word == '(':
            n_parantez += 1
        elif word == ')':
            n_parantez -= 1
            if n_parantez < 0:
                baybaytatlim()
        if word == '.':
            baybaytatlim()
    if n_parantez != 0:
        baybaytatlim()

    for index in range(len(sentence)):
        if sentence[index] == 'nokta':
            if not sentence[index - 1] in t_numerals:
                baybaytatlim()
            if not sentence[index + 1] in t_numerals:
                baybaytatlim()

    log = False
    a = False
    for word in sentence:
        if word in booleans:
            log = True
            if not sentence[0] in mid_bool_var_names:
                mid_bool_var_names.append(sentence[0])

        if word in (numbers + t_numbers):
            a = True
            if not sentence[0] in mid_a_var_names:
                mid_a_var_names.append(sentence[0])

        for key in init_dic_a.keys():
            if word == key:
                a = True
                if not sentence[0] in mid_a_var_names:
                    mid_a_var_names.append(sentence[0])

        for key in init_dic_l.keys():
            if word == key:
                log = True
                if not sentence[0] in mid_bool_var_names:
                    mid_bool_var_names.append(sentence[0])

        if word in l_operations:
            log = True
            if not sentence[0] in mid_bool_var_names:
                mid_bool_var_names.append(sentence[0])

        if word in mid_a_var_names:
            if not sentence[0] in mid_a_var_names:
                mid_a_var_names.append(sentence[0])

        if word in mid_bool_var_names:
            if not sentence[0] in mid_bool_var_names:
                mid_bool_var_names.append(sentence[0])

        if word in a_operations:
            a = True

        if log and a:
            baybaytatlim()

    for index in range(len(sentence)):
        if sentence[index] in a_operations:
            lst = t_numbers + numbers + paranthesis + mid_a_var_names
            for i in init_dic_a.keys():
                lst.append(i)

            if not sentence[index - 1] in lst:
                baybaytatlim()
            if not sentence[index + 1] in lst:
                baybaytatlim()

        if sentence[index] in l_operations:
            lst = booleans + paranthesis + mid_bool_var_names
            for i in init_dic_l.keys():
                lst.append(i)
            if not sentence[index - 1] in lst:
                baybaytatlim()
            if not sentence[index + 1] in lst:
                baybaytatlim()

    for word in sentence:
        kontrol_list = key_w + mid_bool_var_names + mid_a_var_names + numbers
        for i in init_dic_l.keys():
            kontrol_list.append(i)
        for i in init_dic_a.keys():
            kontrol_list.append(i)
        if word not in kontrol_list:
            baybaytatlim()

for sentence in mid_s:
    for i in range(len(sentence)-1):
        if sentence[i] in t_numbers:
            if sentence[i+1] in t_numbers:
                baybaytatlim()
        if sentence[i] in numbers:
            if sentence[i+1] in numbers:
                baybaytatlim()


# FINAL PART
for sentence in final_s:
    while 'ac-parantez' in sentence:
        sentence[sentence.index('ac-parantez')] = '('
    while 'kapa-parantez' in sentence:
        sentence[sentence.index('kapa-parantez')] = ')'

# pasted

n_final_parantez = 0
for sentence in final_s:
    for word in sentence:
        kontrol_list = key_w + mid_bool_var_names + mid_a_var_names + numbers
        for i in init_dic_l.keys():
            kontrol_list.append(i)
        for i in init_dic_a.keys():
            kontrol_list.append(i)
        if word not in kontrol_list:
            baybaytatlim()

    for word in sentence:
        if word == '(':
            n_final_parantez += 1
        elif word == ')':
            n_final_parantez -= 1
            if n_final_parantez < 0:
                baybaytatlim()
        if word == '.':
            baybaytatlim()
    if n_final_parantez != 0:
        baybaytatlim()

    for index in range(len(sentence)):
        if sentence[index] == 'nokta':
            if not sentence[index - 1] in t_numerals:
                baybaytatlim()
            if not sentence[index + 1] in t_numerals:
                baybaytatlim()

    log = False
    a = False
    for word in sentence:
        if word in booleans:
            log = True

        if word in (numbers + t_numbers):
            a = True

        for key in init_dic_a.keys():
            if word == key:
                a = True

        for key in init_dic_l.keys():
            if word == key:
                log = True

        if word in l_operations:
            log = True

        if word in mid_a_var_names:
            a = True

        if word in mid_bool_var_names:
            log = True

        if word in a_operations:
            a = True

        if log and a:
            baybaytatlim()

    for index in range(len(sentence)):
        if sentence[index] in a_operations:
            lst = t_numbers + numbers + paranthesis + mid_a_var_names
            for i in init_dic_a.keys():
                lst.append(i)

            if not sentence[index - 1] in lst:
                baybaytatlim()
            if not sentence[index + 1] in lst:
                baybaytatlim()

        if sentence[index] in l_operations:
            lst = booleans + paranthesis + mid_bool_var_names
            for i in init_dic_l.keys():
                lst.append(i)
            if not sentence[index - 1] in lst:
                baybaytatlim()
            if not sentence[index + 1] in lst:
                baybaytatlim()



var_deposu = []

for sentence in init_s:
    if sentence[0] in var_deposu:
        baybaytatlim()
    var_deposu.append(sentence[0])

for sentence in mid_s:
    if sentence[0] in var_deposu:
        baybaytatlim()
    var_deposu.append(sentence[0])
    for i in range(len(sentence)-1):
        if sentence[i] == '(':
            if sentence[i+1] == ')':
                baybaytatlim()

for sentence in final_s:
    for i in range(len(sentence)-1):
        if sentence[i] == '(':
            if sentence[i+1] == ')':
                baybaytatlim()
if len(final_s) > 1:
    baybaytatlim()

a = open("calc.out", "w")
a.write('Here Comes the Sun')
