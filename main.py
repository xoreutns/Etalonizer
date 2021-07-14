from PyQt5 import QtWidgets
from user_interface import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_select_folder.clicked.connect(self.select_folder)

    def select_folder(self):
        folder_name = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку', '.')
        self.ui.le_folder_name.setText(folder_name)



app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())

