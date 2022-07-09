import os, sys
import file_info_pareser as parser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *



class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.path_text = QLineEdit("...")
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('FileResearcher')



        self.main_layout = self.set_dir_buttons()

        self.setLayout(self.main_layout)
        self.show()




    def set_dir_buttons(self):
        grid = QGridLayout()
        self.dir_browse_btn = QPushButton("...")
        self.dir_browse_btn.clicked.connect(self.openFileNamesDialog)


        grid.addWidget(self.dir_browse_btn, 1, 2)
        grid.addWidget(self.path_text, 1, 1)
        return grid


    def openFileNamesDialog(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.path_text.setText(directory)
        os.chdir(directory)

        self.set_directory_files_list()
        print(os.listdir())


    def set_directory_files_list(self):
        self.files = os.listdir()
        grid = QGridLayout()

        for i in range(len(self.files)):
            file = self.files[i]
            btn = QPushButton(file)
            #btn.clicked.connect(btn.get_File_info())
            grid.addWidget(btn, i, 0)

        self.main_layout.addLayout(grid,2,2)
        return





if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())