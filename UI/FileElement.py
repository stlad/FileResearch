from PyQt5.QtWidgets import *
import os
import UI.UiEnums as en
from UI.File_info_ui import *
import UI.styles as st
from UI.Docx_info_ui import *


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

        self.extention = '' if self.is_dir else self.name[self.name.find('.'):]
        self.is_docx = self.extention == '.docx'
        buttnos= []

        self.layout = QHBoxLayout()

        self.file_button = QPushButton()
        self.file_button.setText(self.name)
        self.file_button.setFixedWidth(150)
        self.file_button.clicked.connect(lambda: self.rename_file_dialog())
        buttnos.append(self.file_button)

        self.child_window = [] # дочернее окно тут хренится, чтобы предотвратить закрытие дочернего окна
        self.info_button = QPushButton()
        self.info_button.setText('?')
        self.info_button.setFixedWidth(50)
        self.info_button.clicked.connect(lambda: self.create_file_info_window())
        buttnos.append(self.info_button)


        self.down_dir_button = QPushButton()
        self.down_dir_button.setFixedWidth(50)

        if self.is_dir:
            self.down_dir_button.setText('↓')
            self.down_dir_button.clicked.connect(lambda: self.go_dir_down())

        buttnos.append(self.down_dir_button)

        self.extention_info_button = QPushButton()
        self.extention_info_button.setFixedWidth(70)
        self.extention_info_button.setText(self.extention)
        self.extention_info_button.setEnabled(False)
        if self.is_docx:
            self.extention_info_button.clicked.connect(lambda: self.create_docx_info_window())
            self.extention_info_button.setEnabled(True)

        buttnos.append(self.extention_info_button)

        self.replace_button = QPushButton()
        self.replace_button.setFixedWidth(50)
        self.replace_button.clicked.connect(lambda: self.accept_replace_dialog())

        buttnos.append(self.replace_button)

        for btn in buttnos:
            btn.setStyleSheet(st.button_style)
            btn.setFixedHeight(25)


        self.create_buttons()

    def rename_file_dialog(self):
        dialog = QInputDialog(self)
        dialog.setTextValue('s')
        new_name, ok = dialog.getText(self, 'Перименование файла', 'Новое имя:',QLineEdit.Normal, self.name)

        if not ok:
            return

        new_fullpath = self.fullpath[:self.fullpath.rfind('/')+1]+new_name
        os.rename(self.fullpath,new_fullpath)
        self.fullpath = new_fullpath
        self.name = new_name
        self.file_button.setText(new_name)


    def create_file_info_window(self):
        f = FileInfoWindow(self.fullpath)
        self.child_window.append(f)
        f.show()

    def create_docx_info_window(self):
        f = DocxInfoWindow(self.fullpath)
        self.child_window.append(f)
        f.show()
        pass

    def replace_file(self, target_path):
        if target_path.__contains__(self.fullpath):
            return
        try:
            os.rename(self.fullpath, target_path+'/'+self.name)
            self.parent_browser.main_parent.refresh_browsers()
            #print(self.fullpath, target_path)

        except OSError:
            return

    def accept_replace_dialog(self):
        side = self.parent_browser.side
        if side == en.Side.LEFT:
            target_browser = self.parent_browser.main_parent.right_browser
        else:
            target_browser = self.parent_browser.main_parent.left_browser

        target_path = target_browser.path
        current_path = self.parent_browser.path

        ret = QMessageBox.question(self, 'Перемещение файла', f"перенести файл {self.name}\nиз {current_path}\nв {target_path}",
                                   QMessageBox.Yes | QMessageBox.No )

        if ret == QMessageBox.Yes:
            self.replace_file(target_path)
        pass

    def go_dir_down(self):
        next = self.fullpath
        self.parent_browser.path_text_field.setText(next)

    def create_buttons(self):
        if self.parent_browser.side==en.Side.LEFT:
            self.layout.addWidget(self.file_button,0)
            self.layout.addWidget(self.info_button,1)
            self.layout.addWidget(self.extention_info_button, 2)
            self.layout.addWidget(self.down_dir_button,3)
            self.replace_button.setText('→')
            self.layout.addWidget(self.replace_button,4)
        elif self.parent_browser.side==en.Side.RIGHT:
            self.layout.addWidget(self.replace_button,0)
            self.layout.addWidget(self.down_dir_button,1)
            self.layout.addWidget(self.extention_info_button, 2)
            self.layout.addWidget(self.info_button,3)
            self.layout.addWidget(self.file_button,4)
            self.replace_button.setText('←')
        else:
            return






