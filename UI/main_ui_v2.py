import os
import file_info_pareser as parser
from PyQt5.QtWidgets import *
from UI import main_window_styles as styles
from UI.UiEnums import *
from UI.PathBrowser import *
from UI.FileElement import *
from UI.FilesLIst import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setGeometry(300, 300, 1200, 700)
        self.setWindowTitle('FileResearcher v2')
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



        self.centralWidget.setLayout(self.main_layout)
        self.show()

    def create_btn_list(self, browser):
        path = self.left_browser.path
        print(path)
        l = FileList(browser).layout

        scroll = QScrollArea()
        w = QWidget()
        w.setLayout(l)
        scroll.setWidget(w)
        if browser.side == Side.LEFT:
            self.main_layout.addWidget(scroll,1,0)
        else:
            self.main_layout.addWidget(scroll,1,1)





