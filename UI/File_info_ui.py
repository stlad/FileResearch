from PyQt5.QtWidgets import *
import os
import file_info_parser as parser
import UI.styles as st
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize, Qt

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
        self.setStyleSheet(st.main_background)

        self.text_area.setText(self.file_info.get_all_info())
        self.text_area.setStyleSheet(st.text_scrolls_style)
        text_layout = QVBoxLayout()
        text_layout.addWidget(self.text_area)
        scroll = QScrollArea()
        scroll.setLayout(text_layout)

        menu_layput = QHBoxLayout()

        self.save_btn = QPushButton()
        self.save_btn.setText('Save as .json')
        self.save_btn.clicked.connect(lambda: self.save_json())
        self.save_btn.setFixedWidth(100)
        self.save_btn.setStyleSheet(st.button_style)
        menu_layput.addWidget(self.save_btn)
        menu_layput.addStretch(1)

        self.main_layout = QGridLayout()
        self.main_layout.addLayout(menu_layput,0,0)
        self.main_layout.addWidget(scroll,1,0)

        self.image = QLabel()
        if self.file_info.file_type=='Image':
            self.setGeometry(100,100,1000,900)
            pixmap = QPixmap(self.file_info.full_path)
            pixmap = pixmap.scaled(QSize(600, 900), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image.setPixmap(pixmap)
        self.main_layout.addWidget(self.image,1,1)

        self.setLayout(self.main_layout)

    def save_json(self):
        name, type = QFileDialog.getSaveFileName(self, 'Save File','', '(*.json)')
        if name=='':
            return
        file = open(name[0], 'w+')
        file.write(self.file_info.get_json())
        file.close()


