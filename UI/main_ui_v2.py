import os
import file_info_parser as parser
from PyQt5.QtWidgets import *
from UI import styles as st
from UI.UiEnums import *
from UI.PathBrowser import *
from UI.FileElement import *
from UI.FilesLIst import *
from PyQt5 import QtCore


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setGeometry(300, 300, 1200, 700)
        self.setWindowTitle('FileResearcher v2')
        self.setStyleSheet(st.main_background)
        self.main_layout = QGridLayout()

        self.left_files=  []
        self.right_files = []

        self.left_browser = PathBrowser(Side.LEFT, self)
        self.main_layout.addLayout(self.left_browser.layout,0,0)
        self.left_browser.path_text_field.textChanged.connect(
            lambda checked, browser = self.left_browser: self.create_btn_list(browser)
        )

        self.right_browser = PathBrowser(Side.RIGHT, self)
        self.main_layout.addLayout(self.right_browser.layout,0,1)
        self.right_browser.path_text_field.textChanged.connect(
            lambda checked, browser = self.right_browser: self.create_btn_list(browser)
        )

        self.footer_layot = QHBoxLayout()
        label = QLabel('Ваганов Владислав, \nЛетняя практика 2022')
        self.footer_layot.addWidget(label)

        self.main_layout.addLayout(self.footer_layot,2,0)
        self.centralWidget.setLayout(self.main_layout)
        self.show()

    def create_btn_list(self, browser):
        path = self.left_browser.path
        if not os.path.exists(path):
            browser.path_text_field.setText('Такого пути нет')
            return
        l = FileList(browser).layout

        scroll = QScrollArea()
        w = QWidget()
        w.setLayout(l)
        scroll.setWidget(w)
        scroll.setStyleSheet(st.text_scrolls_style)

        if browser.side == Side.LEFT:
            self.main_layout.addWidget(scroll,1,0)
        else:
            self.main_layout.addWidget(scroll,1,1)

    def refresh_browsers(self):
        self.create_btn_list(self.left_browser)
        self.create_btn_list(self.right_browser)
