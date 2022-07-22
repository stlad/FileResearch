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
    res['Is Directory'] = st.S_ISDIR(f_stat.st_mode)
    res['Filemode str'] = st.filemode(f_stat.st_mode)
    res['Access rights'] = file_mod_str_to_dict(res['Filemode str'])

    return res

def file_mod_str_to_dict(mode):
    #res['Тип по rwx'] = 'Файл' if mode[0]=='-' else 'Директория'

    owner = mode[1:4]
    main_group = mode[4:7]
    rest = mode[7:]

    dct = {
        'Owner':parse_filemode_triple(owner),
        'Main Group':parse_filemode_triple(main_group),
        'Rest Users':parse_filemode_triple(rest)
    }
    return dct


def parse_filemode_triple(triple):
    s = []
    if triple[0]=='r':
        s.append('Read')

    if triple[1]=='w':
        s.append('Write')

    if triple[2]=='x':
        s.append('Execute')
    return s


