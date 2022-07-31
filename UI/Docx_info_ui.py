from PyQt5.QtWidgets import *
import os,json
import file_info_parser as parser
import doc_statistics as ds
import UI.styles as st

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
        self.setStyleSheet(st.main_background)

        self.text_area.setText('')
        self.text_area.setStyleSheet(st.text_scrolls_style)
        text_layout = QVBoxLayout()
        text_layout.addWidget(self.text_area)
        paragraph_scroll = QScrollArea()
        paragraph_scroll.setLayout(text_layout)



        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.create_paragraph_entering())
        self.main_layout.addWidget(paragraph_scroll)


        self.main_layout.addLayout(self._create_zip_unppack_layout())
        self.main_layout.addWidget(self._create_doc_zip_info())

        self.main_layout.addLayout(self._create_footer())

        self.setLayout(self.main_layout)

    def create_paragraph_entering(self):
        lt = QHBoxLayout()
        label = QLabel()
        label.setText(f'введите номер абзаца от 1 до {self.doc_info.paragraph_count}')

        self.p_num_text = QLineEdit()
        self.p_num_text.setFixedWidth(80)
        self.p_num_text.setStyleSheet(st.text_scrolls_style)


        self.accept_btn = QPushButton()
        self.accept_btn.setText('Выбрать')
        self.accept_btn.clicked.connect(lambda: self._get_info_from_p_num())
        self.accept_btn.setStyleSheet(st.button_style)

        self.last_par_btn = QPushButton()
        self.last_par_btn.setText('←')
        self.last_par_btn.setFixedWidth(30)
        self.last_par_btn.clicked.connect(lambda checked, dir = -1: self._get_next_or_back_par(dir))
        self.last_par_btn.setStyleSheet(st.button_style)

        self.next_par_btn = QPushButton()
        self.next_par_btn.setText('→')
        self.next_par_btn.setFixedWidth(30)
        self.next_par_btn.clicked.connect(lambda checked, dir = 1: self._get_next_or_back_par(dir))
        self.next_par_btn.setStyleSheet(st.button_style)

        lt.addWidget(label)
        lt.addWidget(self.last_par_btn)
        lt.addWidget(self.p_num_text)
        lt.addWidget(self.next_par_btn)
        lt.addWidget(self.accept_btn)
        return lt


    def _get_info_from_p_num(self):
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

    def _get_next_or_back_par(self, delta):
        '''
        Следующий абзац
        :param delta: 1 => +; -1 => -
        :return:
        '''
        try:
            current_par = int(self.p_num_text.text())
        except ValueError:
            current_par = 0 if delta >0 else 2

        if (current_par <=1 and delta==-1) or (current_par >= int(self.doc_info.paragraph_count) and delta==1):
            return

        self.p_num_text.setText(str(current_par+delta))
        self._get_info_from_p_num()

    def _create_footer(self):
        footer_layout = QHBoxLayout()
        footer_layout.addStretch(2)

        self.save_btn = QPushButton()
        self.save_btn.setText('Save as .json')
        self.save_btn.clicked.connect(lambda: self._save_json())
        self.save_btn.setFixedWidth(100)
        self.save_btn.setStyleSheet(st.button_style)

        footer_layout.addWidget(self.save_btn)
        return footer_layout

    def _save_json(self):
        try:
            index = int(self.p_num_text.text())
        except ValueError:
            return

        par = self.doc_info.get_par_from_index(index)
        info = par.get_par_info()

        name, type = QFileDialog.getSaveFileName(self, 'Save File','', '(*.json)')
        if name=='':
            return

        file = open(name, 'w+')
        jinfo = json.dumps(info)
        file.write(jinfo)
        file.close()

    def _create_doc_zip_info(self):
        text = ''
        text = parser.list_to_str(self.doc_info.get_doxc_zip_info(),text)
        text_br = QTextBrowser()
        text_br.setText(text)
        text_br.setStyleSheet(st.text_scrolls_style)

        text_layout = QVBoxLayout()
        text_layout.addWidget(text_br)

        self.zip_scroll = QScrollArea()
        self.zip_scroll.setLayout(text_layout)
        return self.zip_scroll

    def _create_zip_unppack_layout(self):
        layout = QHBoxLayout()
        self.unpack_btn = QPushButton()
        self.unpack_btn.setText('unpack to...')
        self.unpack_btn.setStyleSheet(st.button_style)
        self.unpack_btn.clicked.connect(lambda : self._unpack_docx())

        label = QLabel()
        label.setText('.docx представляет собой фактически .zip архив. \nНиже представлена информация о каждом файле, содержащемся в архиве ')
        layout.addWidget(label)
        layout.addStretch(1)
        layout.addWidget(self.unpack_btn)
        return layout

    def _unpack_docx(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if directory=='':
            return

        dirname = self.name[:self.name.rfind('.')]
        dir_path= directory + '/' + dirname
        os.mkdir(path=dir_path)
        self.doc_info.unzip_docx(dir_path)

        pass


