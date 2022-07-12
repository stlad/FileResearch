from PyQt5.QtWidgets import *
import os
import UI.UiEnums as en
from UI.FileElement import *
from UI.PathBrowser import *


class FileList(QWidget):
    def __init__(self, parent_browser):
        super().__init__()
        self.parent_browser = parent_browser

        self.btn_list = []
        self.layout = QVBoxLayout()
        self.full_path = self.parent_browser.path

        for i, file in enumerate(os.listdir(self.full_path)):
            file_el = FileElement(self.full_path+f'/{file}', parent_browser)
            self.btn_list.append(file_el)

            self.layout.addLayout(file_el.layout,i)
