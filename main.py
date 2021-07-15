from PyQt5 import QtWidgets
from user_interface import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import os


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_select_folder.clicked.connect(self.select_folder)
        self.ui.btn_analyze.clicked.connect(self.analyze_files)

    def select_folder(self):
        folder_name = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку', '.')
        self.ui.le_folder_name.setText(folder_name)
        self.ui.btn_analyze.setEnabled(True)

    def analyze_files(self):
        self.ui.tb_information.clear()
        path = self.ui.le_folder_name.text()
        with os.scandir(path) as files:
            for file in files:
                if file.name.endswith('.csv') and file.is_file():
                    self.ui.tb_information.insertPlainText('Найден файл "' + file.name + '" ')
                    self.ui.tb_information.insertPlainText('Обработка... ')



                    self.ui.tb_information.insertPlainText('ОК' + '\n')
            if self.ui.tb_information.toPlainText() == '':
                self.ui.tb_information.insertPlainText('Файлы *.csv не найдены. Выберите другую папку')




app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
