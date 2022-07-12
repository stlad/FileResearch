from PyQt5.QtWidgets import *
import os, sys
import file_info_pareser as parser

class FileInfoWindow(QWidget):
    def __init__(self, fullpath):
        super().__init__()
        self.fullpath =fullpath
        self.name = fullpath[fullpath.rfind('/') + 1:]
        self.setWindowTitle(f'{self.name} info')
        self.setGeometry(100,100,700,900)
        self.text_area = QTextBrowser()
        os.chdir(self.fullpath[:fullpath.rfind('/')])
        file_info = parser.parse_file(self.name)

        self.text_area.setText(file_info.get_all_info())
        text_layout = QVBoxLayout()
        text_layout.addWidget(self.text_area)
        scroll = QScrollArea()
        scroll.setLayout(text_layout)
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(scroll)

        self.setLayout(self.main_layout)


