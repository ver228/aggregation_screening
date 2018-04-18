#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:40:46 2018

@author: avelinojaver
"""
import os
import glob
import tables
import numpy as np

if __name__ == '__main__':
    is_save_files = False
    
    #main_dir = '/Volumes/rescomp1/WormData/screenings/CeNDR/Results/'
    main_dir = '/Volumes/rescomp1/WormData/screenings/Serena_WT_Screening/Results'
    
    
    fnames = glob.glob(os.path.join(main_dir, '**','*_skeletons.hdf5'), recursive=True)
    #fnames = glob.glob(os.path.join(main_dir, '**','*_featuresN.hdf5'), recursive=True)
    
    
    bad_files = []
    for fname in fnames:
        
        try:
            with tables.File(fname, 'r') as fid:
                food_cnt_coord = fid.get_node('/food_cnt_coord')[:]
                if np.any(np.isnan(food_cnt_coord)):
                    raise ValueError
        except (tables.exceptions.NoSuchNodeError, ValueError):
            bad_files.append(fname)
    
    if is_save_files:
        with open('bad_files.txt') as fid:
            fid.write('\n'.join(bad_files))
    
    print('Unsegmented files: {} of {}'.format(len(bad_files), len(fnames)))