import glob
import os
import shutil

main_dir = '/run/media/ajaver/33ec2489-9d06-4e14-ad9b-f12c2db97cfd/Aggregation'

with open('files2copy.txt', 'r') as fid:
    fnames2copy = [x for x in fid.read().split('\n')]


for ii, fname in enumerate(fnames2copy):
    print(ii, len(fnames2copy))

    dst = os.path.join(main_dir, os.path.basename(fname))
    if not os.path.exists(dst):
        print('copy', fname)
        shutil.copy(fname, main_dir)
    
        