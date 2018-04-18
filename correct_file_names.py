#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:22:47 2018

@author: ajaver
"""
import glob
import pandas as pd
import os
from tierpsy.helper.misc import remove_ext

if __name__ == '__main__':
    #%%
    #read files to change
    fname = '/Volumes/behavgenom_archive$/Serena/AggregationScreening/Video_Title_Corrections.xlsx'
    df = pd.read_excel(fname, header=None)
    good_rows = ~df.isnull().all(axis=0)
    good_rows = good_rows.index[good_rows]
    df = df[good_rows].dropna()
    
    print(df)
    bn2change = df.values.tolist()
    #%%
    #read all the files
    search_str = os.path.join('/Volumes/behavgenom_archive$/Serena/AggregationScreening/', '**', '*.hdf5')
    all_files = glob.glob(search_str, recursive=True)
    
    files_d = {}
    for fname in all_files:
        bn = remove_ext(os.path.basename(fname))
        if not bn in files_d:
            files_d[bn] = []
        files_d[bn].append(fname)
    #%%
    for old_f, new_f in bn2change:
        bn_old = remove_ext(old_f)
        bn_new = remove_ext(new_f)
        if bn_old in files_d:
            f2change = files_d[bn_old]
            
            for old_fname in f2change:
                new_fname = old_fname.replace(bn_old, bn_new)
                assert new_fname != old_fname
                os.rename(old_fname, new_fname)
            
        else:
            print('!!!!!', old_f)
        
    