import os
import random


listnames = ['cb_copy.txt',  'da_copy.txt',  'n2_copy.txt']


all_files = []
for lname in listnames:
    with open(lname, 'r') as fid:
        all_files += fid.read().split('\n')

all_files = [x for x in all_files if x]


all_files_f = []
for x in all_files:
    bn = os.path.basename(x)
    elem = bn.split('_')
    
    ch_n = [int(x[2:]) for x in elem if x.startswith('Ch')][0]
    if (elem[4] == 'Set0' or elem[3] == 'Set0')  and ch_n % 2 == 1:#and elem[0].endswith('1'):
        all_files_f.append(x)


#random.shuffle(all_files_f)

with open('files2copy.txt', 'w') as fid:
    dd = '\n'.join(all_files_f)
    fid.write(dd)
