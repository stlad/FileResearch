from PyQt5.QtWidgets import *
import os
import UI.UiEnums as en
from UI.FileElement import *
from UI import styles as st

class PathBrowser(QWidget):
    '''
    Содержит навигацию по папкам
    '''
    def __init__(self, side, main_parent):
        super().__init__()
        self.path = '...'
        self.side = side
        self.main_parent = main_parent

        self.path_text_field = QLineEdit()
        self.path_text_field.setText(self.path)
        self.path_text_field.textChanged.connect( self.change_directory)
        self.path_text_field.setStyleSheet(st.text_scrolls_style + 'padding:3px 3px 3px 3px')

        self.back_button = QPushButton()
        self.back_button.setText('←')
        self.back_button.setFixedWidth(50)
        self.back_button.clicked.connect(self.set_back_directory)
        self.back_button.setStyleSheet(st.button_style)

        self.browse_button = QPushButton()
        self.browse_button.setText('...')
        self.browse_button.clicked.connect(self.openFileNamesDialog)
        self.browse_button.setStyleSheet(st.button_style)

        self.add_file_btn = QPushButton()
        self.add_file_btn.setFixedWidth(50)
        self.add_file_btn.setText('+')
        self.add_file_btn.clicked.connect(lambda: self.create_file())
        self.add_file_btn.setStyleSheet(st.button_style)


        self.dir_menu_layout = QHBoxLayout()
        self.dir_menu_layout.addWidget(self.back_button)
        self.dir_menu_layout.addWidget(self.add_file_btn)
        self.dir_menu_layout.addStretch()

        self.layout = QGridLayout()
        self.layout.addLayout(self.dir_menu_layout,1,0)
        self.layout.addWidget(self.path_text_field,0,0)
        self.layout.addWidget(self.browse_button,0,1)


    def openFileNamesDialog(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if directory=='':
            return
        self.path_text_field.setText(directory)


    def change_directory(self):
        '''Метод меняет рабочую директорию'''
        self.path = self.path_text_field.text()

    def set_back_directory(self):
        path = self.path_text_field.text()
        index = path.rfind('/')
        if index == -1:
            return
        self.path_text_field.setText(path[0:index])

    def create_file(self):
        if self.path =='...':
            return

        name, type = QFileDialog.getSaveFileName(self, 'Создать файл','', '(*.txt)')
        if name == '':
            return

        file = open(name[0], 'w+')
        file.close()




