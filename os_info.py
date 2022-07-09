import os
import  stat as st# интерпретирует результаты os.stat()
import time

def get_info(filename):
    f_stat = os.stat(filename)
    res = {}
    res['Name'] = filename
    res['Mode'] = f_stat.st_mode
    res['Size'] = f_stat.st_size
    res['Owner'] = f_stat.st_uid
    res['Device'] = f_stat.st_dev
    res['Created'] = time.ctime(f_stat.st_ctime)
    res['Last modified'] = time.ctime(f_stat.st_mtime)
    res['Last accessed'] = time.ctime(f_stat.st_atime)
    res['Stat'] = f_stat
    res['Filemode str'] = st.filemode(f_stat.st_mode)
    res['Is Directory'] = st.S_ISDIR(f_stat.st_mode)

    return res
