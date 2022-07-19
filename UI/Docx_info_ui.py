from PyQt5.QtWidgets import *
import os, sys
import file_info_parser as parser
import doc_statistics as ds


class DocxInfoWindow(QWidget):
    def __init__(self, fullpath):
        super().__init__()
        self.fullpath =fullpath
        self.name = fullpath[fullpath.rfind('/') + 1:]
        self.setWindowTitle(f'{self.name} info')
        self.setGeometry(100,100,700,900)
        self.text_area = QTextBrowser()
        os.chdir(self.fullpath[:fullpath.rfind('/')])
        self.doc_info = ds.docx_staticstics(self.name)




        self.text_area.setText('привет')
        text_layout = QVBoxLayout()
        text_layout.addWidget(self.text_area)
        scroll = QScrollArea()
        scroll.setLayout(text_layout)


        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.create_paragraph_entering())
        self.main_layout.addWidget(scroll)

        self.setLayout(self.main_layout)

    def create_paragraph_entering(self):
        lt = QHBoxLayout()
        label = QLabel()
        label.setText(f'введите номер абзаца от 1 до {self.doc_info.paragraph_count}')

        self.p_num_text = QLineEdit()

        self.accept_btn = QPushButton()
        self.accept_btn.setText('Выбрать')
        self.accept_btn.clicked.connect(lambda: self.get_info_from_p_num())

        self.last_par_btn = QPushButton()
        self.last_par_btn.setText('←')
        self.last_par_btn.setFixedWidth(20)
        self.last_par_btn.clicked.connect(lambda checked, dir = -1: self.get_next_or_back_par(dir))

        self.next_par_btn = QPushButton()
        self.next_par_btn.setText('→')
        self.next_par_btn.setFixedWidth(20)
        self.next_par_btn.clicked.connect(lambda checked, dir = 1: self.get_next_or_back_par(dir))

        lt.addWidget(label)
        lt.addWidget(self.last_par_btn)
        lt.addWidget(self.p_num_text)
        lt.addWidget(self.next_par_btn)
        lt.addWidget(self.accept_btn)
        return lt


    def get_info_from_p_num(self):
        try:
            index = int(self.p_num_text.text())
        except ValueError:
            self.p_num_text.setText('Введите норм число')
            return

        if index <0 or index > self.doc_info.paragraph_count:
            self.p_num_text.setText('Такого нет')
            return


        par = self.doc_info.get_par_from_index(index)
        info = ''
        info = parser.dict_to_str(par.get_par_info(), info)

        self.text_area.setText(info)

    def get_next_or_back_par(self, delta):
        '''
        Следующий абзац
        :param delta: 1 => +; -1 => -
        :return:
        '''
        current_par = int(self.p_num_text.text())
        if (current_par <=1 and delta==-1) or (current_par >= int(self.doc_info.paragraph_count) and delta==1):
            return

        self.p_num_text.setText(str(current_par+delta))
        self.get_info_from_p_num()
