import glob
import os
import shutil

main_dir = '/run/media/ajaver/33ec2489-9d06-4e14-ad9b-f12c2db97cfd/Aggregation'
fnames = glob.glob(os.path.join(main_dir, '*.*'))


with open('files2copy.txt', 'r') as fid:
    fnames2copy = [x for x in fid.read().split('\n')]

fnames2copy_d = {os.path.basename(x):x for x in fnames2copy}

for ii, fname in enumerate(fnames):
    print(ii, len(fnames))
    dst = fnames2copy_d[os.path.basename(fname)]
    if not os.path.exists(dst):
        shutil.copy(fname, os.path.dirname(dst))
    else:
        print('???', dst)

    #








