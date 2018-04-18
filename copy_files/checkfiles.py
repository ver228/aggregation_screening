import glob
import os
import shutil

main_dir = '/run/media/ajaver/33ec2489-9d06-4e14-ad9b-f12c2db97cfd/Aggregation'
fnames = glob.glob(os.path.join(main_dir, '*.*'))


with open('files2copy.txt', 'r') as fid:
    fnames2copy = [x for x in fid.read().split('\n')]


dd = set(map(os.path.basename, fnames2copy)) - set(map(os.path.basename, fnames)) 

fnames2copy_d = {os.path.basename(x):x for x in fnames2copy}


f2copy = [fnames2copy_d[x] for x in iter(dd)]

with open('checkbkp.txt', 'w') as fid:
   fid.write('\n'.join(sorted(f2copy)))

