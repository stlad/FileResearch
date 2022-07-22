from PyQt5.QtWidgets import *
import os, sys
import file_info_parser as parser

class FileInfoWindow(QWidget):
    def __init__(self, fullpath):
        super().__init__()
        self.fullpath =fullpath
        self.name = fullpath[fullpath.rfind('/') + 1:]
        self.setWindowTitle(f'{self.name} info')
        self.setGeometry(100,100,700,900)
        self.text_area = QTextBrowser()
        os.chdir(self.fullpath[:fullpath.rfind('/')])
        self.file_info = parser.parse_file(self.name)

        self.text_area.setText(self.file_info.get_all_info())
        text_layout = QVBoxLayout()
        text_layout.addWidget(self.text_area)
        scroll = QScrollArea()
        scroll.setLayout(text_layout)

        menu_layput = QHBoxLayout()

        self.save_btn = QPushButton()
        self.save_btn.setText('Save as .json')
        self.save_btn.clicked.connect(lambda: self.save_json())
        self.save_btn.setFixedWidth(100)
        menu_layput.addWidget(self.save_btn)
        menu_layput.addStretch(1)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(menu_layput)
        self.main_layout.addWidget(scroll)
        self.setLayout(self.main_layout)

    def save_json(self):
        name, type = QFileDialog.getSaveFileName(self, 'Save File','', '(*.json)')
        if name=='':
            return
        file = open(name[0], 'w+')
        file.write(self.file_info.get_json())
        file.close()


