import os, sys
from PyQt5.QtWidgets import *

import UI.main_ui_v2
import UI.main_ui_v1

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = UI.main_ui_v2.MainWindow()
    sys.exit(app.exec_())