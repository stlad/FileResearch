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
        self.setStyleSheet("background-color:#087712")



        self.set_dir_buttons()
        self.show()




    def set_dir_buttons(self):
        grid = QGridLayout()
        self.dir_browse_btn = QPushButton("...")
        self.dir_browse_btn.clicked.connect(self.openFileNamesDialog)


        grid.addWidget(self.dir_browse_btn,1,2)
        grid.addWidget(self.path_text,1,1)
        self.setLayout(grid)
        return


    def openFileNamesDialog(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.path_text.setText(directory)
        os.chdir(directory)
        print(os.listdir())


    def get_diectory_files_list(self):
        pass





if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())