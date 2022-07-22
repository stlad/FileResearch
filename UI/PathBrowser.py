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
        #self.path_text_field.setStyleSheet(st.text_areas_s)

        self.back_button = QPushButton()
        self.back_button.setText('←')
        self.back_button.setFixedWidth(50)
        self.back_button.clicked.connect(self.set_back_directory)

        self.browse_button = QPushButton()
        self.browse_button.setText('...')
        self.browse_button.clicked.connect(self.openFileNamesDialog)

        self.add_file_btn = QPushButton()
        self.add_file_btn.setFixedWidth(50)
        self.add_file_btn.setText('+')
        self.add_file_btn.clicked.connect(lambda: self.create_file())


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

    def create_file_old(self):
        if self.path =='...':
            return
        dialog = QInputDialog(self)
        new_name, ok = dialog.getText(self, 'Создание файла', 'Новое имя:',QLineEdit.Normal)

        if not ok:
            return

        if os.listdir(self.path).__contains__(new_name):
            print('такой файл есть')
            return

        new_file = open(self.path+'/'+new_name, "w+")
        new_file.close()

    def create_file(self):
        if self.path =='...':
            return
        name = QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name[0], 'w+')
        file.close()




