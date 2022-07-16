import docx
import os

def ger_docx_meta(docname): # вооще из дока можнов вытащить все что у годно. тут только минимум
    doc = docx.Document(docname)
    props = doc.core_properties
    info ={
        'Author':props.author,
        'Last modified by': props.last_modified_by,
        'Creation Date':f'{props.created.day}.{props.created.month}.{props.created.year}',
        'Last Mod Date':f'{props.modified.day}.{props.modified.month}.{props.modified.year}',
        'Last Print Date':f' {props.last_printed}',
        'Saves Count':props.revision
    }
    return info



class docx_staticstics:
    def __init__(self, name):
        self.name = name
        self.doc = docx.Document(self.name)

        self.paragraph_count = len(self.doc.paragraphs)


    def get_info(self):
        paragraphs = self.doc
        for paragraph in self.doc.paragraphs:
            print(paragraph.text)


    def get_par_from_index(self, index):
        p_list = list(self.doc.paragraphs)
        p = Paragraph(p_list[index-1])
        return p

class Paragraph:
    def __init__(self, par):
        self.paragraph = par
        self.text = par.text
        self.symbol_count = len(self.text)

    def get_par_info(self):
        res ={}
        res['Текст']= self.text,
        res['Количество символов']= self.symbol_count

        return res




'''os.chdir(os.getcwd()+'/Files')

a = docx_staticstics('Document.docx')
print(a.paragraph_count)
'''