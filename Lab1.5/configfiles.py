import os
import glob

path = os.environ['HOME'] + '/Seafile/p4ne_training/config_files/'
z = glob.glob(path + "*.txt")

ip_list = []
ip_counter = 0

for i in z:
    with open(i) as f:
        for j in f:
            a = f.readline()
            if a.find('ip address') > 0 and a.find('.') > 0:
                ip_list.append(a.strip().replace("ip address ", ""))
                ip_counter += 1

#print(ip_list)
#for i in ip_list:
#    print(i)

print('Всего найдено %s записи)' % ip_counter)

clear_list = []
ip_clear_counter = 0
for i in ip_list:
    if i not in clear_list:
        clear_list.append(i)
        ip_clear_counter += 1
#        print(i)
    else:
        print(i +'- повторая хуйня!!! Я тебя поймал!!!')

print('Итого, уникальных записей - %s!' % ip_clear_counter)

for i in clear_list:
    print(i)