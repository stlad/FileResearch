import os_info as osI
import meta_info as metaI
import os,sys,json
import pprint as pp
import  stat as st

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

    def get_json(self):
        res = {}
        res['OS Info'] = self.info
        res['Meta Info'] = self.meta_info
        return json.dumps(res)


    def print_all_info(self):
        print('______FILE______:')
        print(f'Name            : {self.filename}')
        print(f'full path       : {self.full_path}')
        print(f'file type       : {self.file_type}')
        print('_____OS_Info____:')
        self._print_os_info()
        print('_____META_INFO__:')
        self._print_meta_info()

    def _print_os_info(self):
        for key in self.info:
            print(f'{key:16}: {self.info[key]}')

    def _print_meta_info(self):
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
        #for key in self.info:
        #    res+=f'{key:16}: {self.info[key]}\n\n'
        res = dict_to_str(self.info, res)
        res += '_____META_INFO__:\n\n'

        if len(self.meta_info) == 0:
            res+='None\n\n'
            return res

        res = dict_to_str(self.meta_info, res)
        return res



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
        elif isinstance(dct[key],list) or isinstance(dct[key],tuple):
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
        elif isinstance(elem,list) or isinstance(elem, tuple):
            s+='\n'
            s = list_to_str(elem,s,depth+1 )
        else:
            s += ' '*depth*10 +f'{elem}\n\n'
    return s

def is_directory(filename):
    f_stat = os.stat(filename)
    return st.S_ISDIR(f_stat.st_mode)




