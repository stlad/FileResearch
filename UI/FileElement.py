from PyQt5.QtWidgets import *
import os
import UI.UiEnums as en
from UI.File_info_ui import *


class FileElement(QWidget):
    '''
    Содержит клавищи управления файлами
    '''
    def __init__(self, fullpath, parent_path_browser ):
        super().__init__()
        self.fullpath = fullpath
        self.name = fullpath[fullpath.rfind('/')+1:]
        self.parent_browser = parent_path_browser
        self.is_dir = os.path.isdir(self.fullpath)
        self.is_docx = self.name[self.name.find('.'):] == '.doc'

        self.layout = QHBoxLayout()

        self.file_button = QPushButton()
        self.file_button.setText(self.name)
        self.file_button.setFixedWidth(150)


        self.child_window = [] # дочернее окно тут хренится, чтобы предотвратить закрытие дочернего окна
        self.info_button = QPushButton()
        self.info_button.setText('?')
        self.info_button.setFixedWidth(30)
        self.info_button.clicked.connect(lambda: self.create_file_info_window())


        self.down_dir_button = QPushButton()
        self.down_dir_button.setFixedWidth(30)

        if self.is_dir:
            self.down_dir_button.setText('↓')
            self.down_dir_button.clicked.connect(lambda: self.go_dir_down())

        self.doc_info_button = QPushButton()
        if self.is_docx:
            self.doc_info_button.setText('.doc')
            self.doc_info_button.setFixedWidth(30)


        self.replace_button = QPushButton()
        self.replace_button.setFixedWidth(30)
        self.create_buttons()


    def create_file_info_window(self):
        f = FileInfoWindow(self.fullpath)
        self.child_window.append(f)
        f.show()

    def go_dir_down(self):
        next = self.fullpath
        self.parent_browser.path_text_field.setText(next)

    def create_buttons(self):
        if self.parent_browser.side==en.Side.LEFT:
            self.layout.addWidget(self.file_button,0)
            self.layout.addWidget(self.info_button,1)
            self.layout.addWidget(self.doc_info_button,2)
            self.layout.addWidget(self.down_dir_button,3)
            self.replace_button.setText('→')
            self.layout.addWidget(self.replace_button,4)
        elif self.parent_browser.side==en.Side.RIGHT:
            self.layout.addWidget(self.replace_button,0)
            self.layout.addWidget(self.down_dir_button,1)
            self.layout.addWidget(self.doc_info_button,2)
            self.layout.addWidget(self.info_button,3)
            self.layout.addWidget(self.file_button,4)
            self.replace_button.setText('←')
        else:
            return






