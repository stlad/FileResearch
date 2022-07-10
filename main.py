import os, sys

import file_info_pareser
import file_info_pareser as parser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        '''СОЗДАНИЕ ОСНОВНОГО ОКНА'''
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('FileResearcher')


        '''Кнопки '''
        self.path_text = QLineEdit("...")
        self.path_text.setEnabled(False)
        self.path_text.textChanged.connect(self.change_current_directory)

        self.browse_button = QPushButton("...")
        self.browse_button.clicked.connect(self.openFileNamesDialog)

        '''Текстовое поле'''


        '''Основные слои'''
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.path_text, 1, 0)
        self.main_layout.addWidget(self.browse_button, 1, 1)

        self.files_scroll_area  = QScrollArea()
        self.files_scroll_area.setWidget(QWidget())

        self.main_layout.addWidget(self.files_scroll_area, 2, 0)
        self.centralWidget.setLayout(self.main_layout)

        self.show()



    def change_current_directory(self):
        '''Метод меняет рабочую директорию'''
        os.chdir(self.path_text.text())
        self.create_files_list_widget()
        print(os.listdir())

    def openFileNamesDialog(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.path_text.setText(directory)


    def create_files_list_widget(self):
        '''Метод сканируюет рабочую директорию и создает кнопки для всех файлов в ней'''
        print(self.files_scroll_area.widget().layout())
        self.clear_layout(self.files_scroll_area.widget().layout())
        if self.path_text.text() == '...':
            return
        files = os.listdir()
        files_layout = QVBoxLayout()

        for i in range(len(files)):
            file = files[i]
            btn = QPushButton(file)
            btn.setObjectName(f"button {i}")
            #get_file_indo_lambda = lambda : file_info_pareser.parse_file(file)

            files_layout.addWidget(btn, i)

        scroll_widget = QWidget()
        scroll_widget.setLayout(files_layout)
        self.files_scroll_area.setWidget(scroll_widget)


    def clear_layout(self, layout):
        """Очищает переданный слой от всех виджетов"""
        if layout==None:
            return

        widgets = layout.layout().count()

        print(widgets)
        for i in range(widgets):
            print(layout.layout().itemAt(0).widget().objectName())
            widget = layout.layout().itemAt(0).widget()
            layout.layout().removeWidget(widget)
            widget.hide()






    def set_directory_files_list(self):
        self.files = os.listdir()
        self.clear_layout(self.directory_files_layout)



        return





if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())