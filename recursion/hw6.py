file = open('crime_scene.TXT', 'r')
content = file.read()
lines = content.splitlines()
evi = []
b = lines[0].split()
for j in range(2, len(lines)):
    evi.append(lines[j].split())
n = int(lines[1])
w = int(b[0])
t = int(b[1])


def weight(r_limit, i):
    if i == len(evi):
        return 0, []
    if r_limit - int(evi[i][1]) >= 0:
        col_v, col_l = weight(r_limit-int(evi[i][1]), i+1)
        col_v += int(evi[i][3])
        col_l.append(evi[i])
    else:
        col_v = 0
        col_l = []
    c_v_dont_take, c_l_dont_take = weight(r_limit, i+1)
    if col_v > c_v_dont_take:
        return col_v, col_l
    else:
        return c_v_dont_take, c_l_dont_take


def time(r_limit, i):
    if i == len(evi):
        return 0, []
    if r_limit - int(evi[i][2]) >= 0:
        col_v, col_l = time(r_limit-int(evi[i][2]), i+1)
        col_v += int(evi[i][3])
        col_l.append(evi[i])
    else:
        col_v = 0
        col_l = []
    c_v_dont_take, c_l_dont_take = time(r_limit, i+1)
    if col_v > c_v_dont_take:
        return col_v, col_l
    else:
        return c_v_dont_take, c_l_dont_take


def both(t_left, w_left, i):
    if i == len(evi):
        return 0, []
    if (t_left - int(evi[i][2]) >= 0) and (w_left - int(evi[i][1]) >= 0):
        col_v, col_l = both(t_left-int(evi[i][2]), w_left-int(evi[i][1]), i+1)
        col_v += int(evi[i][3])
        col_l.append(evi[i])
    else:
        col_v = 0
        col_l = []
    c_v_dont_take, c_l_dont_take = both(t_left, w_left, i+1)
    if col_v > c_v_dont_take:
        return col_v, col_l
    else:
        return c_v_dont_take, c_l_dont_take


w_list = list(weight(w, 0))
t_list = list(time(t, 0))
both_list = list(both(t, w, 0))
sort_count = 0


def sort(lst):
    global sort_count
    if len(lst) <= 1:
        return lst
    p = int(lst[0])
    i = 1
    q = len(lst) - 1
    while True:
        if q < i:
            break
        if int(lst[i]) <= p:
            i += 1
            continue
        elif int(lst[q]) >= p:
            q -= 1
            continue
        lst[i], lst[q] = lst[q], lst[i]
        sort_count += 1
    lst[0], lst[q] = lst[q], lst[0]
    sort_count += 1
    lst[0:q] = sort(lst[0:q])
    lst[q + 1:] = sort(lst[q + 1:])
    return lst

w_final = []
for i in w_list[1]:
    w_final.append(i[0])

t_final = []
for i in t_list[1]:
    t_final.append(i[0])

both_final = []
for i in both_list[1]:
    both_final.append(i[0])

sort(w_final)
sort(t_final)
sort(both_final)

def string_conv(lst):
    st = ' '.join(lst)
    return st


part1 = open("solution_part1.txt", "w")
part1.write(str(w_list[0]))
part1.write('\n')
part1.write(string_conv(w_final))

part2 = open("solution_part2.txt", "w")
part2.write(str(t_list[0]))
part2.write('\n')
part2.write(string_conv(t_final))

part3 = open("solution_part3.txt", "w")
part3.write(str(both_list[0]))
part3.write('\n')
part3.write(string_conv(both_final))

file.close()
part1.close()
part2.close()
part3.close()
