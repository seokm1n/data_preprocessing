# python_basic 디렉토리 아래에 'reference' 디렉토리를 만들고
# '20260521' 디렉토리 내부에 존재하는 'Health_info.csv' 파일을
# 'reference' 디렉토리 내부로 이동(복사 가능)

import os
import shutil

rootdir = os.getcwd().replace('20260522', '')
dir_0521 = rootdir + '20260521/'

if os.path.exists(rootdir + 'reference'):
    if not os.path.exists(rootdir + 'reference/Health_info.csv'):
        shutil.copy2(dir_0521 + 'Health_info.csv', rootdir + 'reference')
else:
    os.mkdir(rootdir + 'reference')

destpath = rootdir + 'reference' + '\\'
print(destpath)

srcfilepath = rootdir + '20260521/' + 'Health_info.csv'
print(srcfilepath)

import time
print(time.localtime())