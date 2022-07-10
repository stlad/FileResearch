import copy
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


        '''Кнопки поиска директории'''
        self.path_text = QLineEdit("...")
        #self.path_text.setEnabled(False)
        self.path_text.textChanged.connect(self.change_current_directory)

        self.browse_button = QPushButton("...")
        self.browse_button.clicked.connect(self.openFileNamesDialog)

        browser_text_btn = QHBoxLayout()
        browser_text_btn.addWidget(self.path_text)
        browser_text_btn.addWidget(self.browse_button)

        '''Текстовое поле'''
        self.info_text_area = QTextBrowser()


        '''Основные слои'''
        self.main_layout = QGridLayout()
        self.main_layout.addLayout(browser_text_btn, 1, 0)
        self.main_layout.addWidget(self.info_text_area,2,1)


        '''Слайдер списка фалов'''
        self.files_scroll_area  = QScrollArea()
        self.files_scroll_area.setWidget(QWidget())

        self.main_layout.addWidget(self.files_scroll_area, 2, 0)
        self.centralWidget.setLayout(self.main_layout)

        self.show()



    def change_current_directory(self):
        '''Метод меняет рабочую директорию'''

        try:
            os.chdir(self.path_text.text())
        except OSError:
            self.path_text.setText('Такой папки нет')
            return

        self.create_files_list_widget()
        print(os.listdir())

    def openFileNamesDialog(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.path_text.setText(directory)


    def create_files_list_widget(self):
        '''Метод сканируюет рабочую директорию и создает кнопки для всех файлов в ней'''
        self.clear_layout(self.files_scroll_area.widget().layout())
        if self.path_text.text() == '...':
            return
        files = os.listdir()
        files_layout = QVBoxLayout()

        for i in range(len(files)):
            file = files[i]
            btn = QPushButton(file)
            btn.setObjectName(f'button {i}')
            btn.clicked.connect(
                lambda checked, filename = file: self.parse_file_info(filename)
            )
            files_layout.addWidget(btn, i)

        scroll_widget = QWidget()
        scroll_widget.setLayout(files_layout)
        self.files_scroll_area.setWidget(scroll_widget)


    def clear_layout(self, layout):
        """Очищает переданный слой от всех виджетов"""
        if layout==None:
            return
        widgets = layout.layout().count()
        for i in range(widgets):
            widget = layout.layout().itemAt(0).widget()
            layout.layout().removeWidget(widget)
            widget.hide()



    def parse_file_info(self, filename):
        print(filename)
        file_info = file_info_pareser.parse_file(filename)
        self.info_text_area.setText(file_info.get_all_info())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())