from PyQt5.QtWidgets import *
import os
import UI.UiEnums as en


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

        self.info_button = QPushButton()
        self.info_button.setText('?')
        self.info_button.setFixedWidth(30)

        self.down_dir_button = None
        if self.is_dir:
            self.down_dir_button = QPushButton()
            self.down_dir_button.setText('↓')
            self.down_dir_button.setFixedWidth(30)

        self.doc_info_button = None
        if self.is_docx:
            self.doc_info_button = QPushButton()
            self.doc_info_button.setText('.doc')
            self.doc_info_button.setFixedWidth(30)


        self.replace_button = QPushButton()
        self.replace_button.setFixedWidth(30)
        self.create_buttons()




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
            pass






