import sys

import os_info as osI
import meta_info as metaI
import os
import pprint as pp

FileTypes ={
    'Image':['.jpg','.png','.gif'],
    'Video':['.mp4', '.avi','.mkv'],
    'Audio':['.mp3','.wav'],
    'Document':['.docx','.pptx','.pdf',],
    'Executable':['.exe'],
    'Directory':['']
}


class FileInfo:
    '''Класс, содержащий подробную информацию о файле'''
    def __init__(self, name, full_path, file_type, info, meta):
        self.filename = name
        self.full_path = full_path
        self.file_type = file_type

        self.info = info
        self.info_size = 0
        for key in self.info:
            self.info_size += sys.getsizeof(self.info[key])

        self.meta_info = meta
        self.meta_info_size =0
        for key in self.meta_info:
            self.meta_info_size += sys.getsizeof(self.meta_info[key])


    def print_all_info(self):
        print('______FILE______:')
        print(f'Name            : {self.filename}')
        print(f'full path       : {self.full_path}')
        print(f'file type       : {self.file_type}')
        print('_____OS_Info____:')
        self.print_os_info()
        print('_____META_INFO__:')
        self.print_meta_info()

    def print_os_info(self):
        for key in self.info:
            print(f'{key:16}: {self.info[key]}')

    def print_meta_info(self):
        if len(self.meta_info) == 0:
            print('None')
            pass
        pp.pprint(self.meta_info)




    def print_os_info(self):
        for key in self.info:
            print(f'{key:16}: {self.info[key]}')

    def print_meta_info(self):
        if len(self.meta_info) == 0:
            print('None')
            pass
        pp.pprint(self.meta_info)


    def get_all_info(self):
        res = ""
        res += '______FILE______:\n\n'
        res += f'Name            : {self.filename}\n\n'
        res += f'full path       : {self.full_path}\n\n'
        res += f'file type       : {self.file_type}\n\n'
        res += '_____OS_Info____:\n\n'
        for key in self.info:
            res+=f'{key:16}: {self.info[key]}\n\n'
        res += '_____META_INFO__:\n\n'

        if len(self.meta_info) == 0:
            res+='None\n\n'
            return res

        res = dict_to_str(self.meta_info, res)
        #for key in self.meta_info:
        #    res+= f'{key:16}: {self.meta_info[key]}\n\n'

        return res


def parse_directory():
    pass


def parse_file(filename) -> FileInfo:
    '''Вытаскивает подруюную инфомарцию о файле и возвращает FileInfo'''
    file_extention = filename[filename.find('.'):]
    file_type = 'Directory'
    for key in FileTypes:
        if FileTypes[key].__contains__(file_extention):
            file_type = key

    meta_info ={}
    os_info = osI.get_info(filename)

    if file_type == 'Image':
        meta_info = metaI.get_image_meta(filename)
    elif file_type=='Video' or file_type=='Audio':
        meta_info = metaI.get_vid_meta(filename)
    elif file_type=='Document' and file_extention=='.pdf':
        meta_info = metaI.get_pdf_meta(filename)
    elif file_type=='Document' and file_extention=='.docx':
        meta_info = metaI.ger_docx_meta(filename)

    return FileInfo(filename, os.path.abspath(filename), file_type, os_info,meta_info)

def dict_to_str(dct, s, depth =0):
    for key in dct:
        s+=' '*depth*10 +f'{key}: '
        if isinstance(dct[key], dict):
            s+='\n'
            s = dict_to_str(dct[key],s, depth+1)
        elif isinstance(dct[key],list):
            s+='\n'
            s = list_to_str(dct[key],s, depth+1)

        else:
            s+=f'{dct[key]}\n\n'
    return s

def list_to_str(l, s, depth=0):
    for elem in l:
        if isinstance(elem, dict):
            s+='\n'
            s = dict_to_str(elem,s,depth+1)
        elif isinstance(elem,list):
            s+='\n'
            s = list_to_str(elem,s,depth+1 )
        else:
            s += ' '*depth*10 +f'{elem}\n\n'
    return s



s=''
a = {
    'a':10,
    'b':{
        'as':20,
        'vv':123,
    },
    's':0,
    'd':[1,2,{'ttt':2},23,4,5,[12,32]]
}

print(dict_to_str(a,s))