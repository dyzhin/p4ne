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
                ip_list.append(a.strip())
                ip_counter += 1

#print(ip_list)
#for i in ip_list:
#    print(i)

print(ip_counter)

new_list = []
ip_clear_couter = 0
for i in ip_list:
    if i not in new_list:
        new_list.append(i)
        ip_clear_couter += 1
#        print(i)
    else:
        print(i)

print(ip_clear_couter)