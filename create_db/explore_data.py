import os
import datetime
import pandas as pd

def split_file(x):
    dir_name, bn = os.path.split(x)
    prefix, postfix = bn.split('_Set0_Pos0_')

    ch_str, _, remainder = postfix.partition('_')
    ch_n = int(ch_str[2:])
    ts_str = remainder[:-5]
    ts = datetime.datetime.strptime(ts_str, "%d%m%Y_%H%M%S")

    prefix = prefix.lower()
    is_bad = '_x_' in prefix
    prefix = prefix.replace('_x_', '_')

    block_str, _, remainder = prefix.partition('_')
    block_str = block_str.replace(',', '.')
    block, day = block_str.split('.')


    if remainder[0].isdigit():
        run, _, strain_data = remainder.partition('_')
    else:
        run, strain_data = 0, remainder
    
    strain_data = strain_data.replace('da609', 'da609_xx')
    strain_data = strain_data.replace('none', 'none_none')
    strain_data = strain_data.replace('gwx1', 'gxw1')
    strain_data = strain_data.upper()
    
    #here sometimes there are two names and we have to use the channel to decide what is the correct strain
    s_parts = strain_data.split('_')
    if len(s_parts) == 2:
        strain_name, strain_code = s_parts
    elif len(s_parts) == 4:
        if ch_n % 2 == 1:
            strain_name, strain_code = s_parts[:2]
        else:
            strain_name, strain_code = s_parts[2:]
    else:
        raise ValueError(prefix)



    return (bn, dir_name, is_bad, block, day, run, strain_name, strain_code, ch_n, ts)

if __name__ == '__main__':
    fname = 'all_masked_files.txt'
    with open(fname, 'r') as fid:
        masked_videos = fid.read().split('\n')
        masked_videos = [x for x in masked_videos if x]
        masked_videos = [x for x in masked_videos if not 'test' in x.lower()]

    cols = ['basename', 'dirname',  'is_bad', 'block', 'day', 'run', 'strain_name', 'strain_code', 'channel', 'timestamp']
    
    data = list(map(split_file, masked_videos))
    df = pd.DataFrame(data, columns = cols)

    print(df['strain_name'].value_counts())

    df.to_csv('aggregation_data.csv', index=False)








