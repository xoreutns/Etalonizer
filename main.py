from PyQt5 import QtWidgets
from user_interface import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import os
import csv
from datetime import datetime
import pandas as pd


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
            common_data_list = []  # Для хранения данных из всех файлов
            emitter_number = 1  # Номер излучателя (порядковый номер файла)
            rig_first_number = 1  # Первая цифра номера оснастки
            rig_second_number = 1  # Вторая цифра номера оснастки
            for file in files:
                if file.name.endswith('.csv') and file.is_file():
                    self.ui.tb_information.insertPlainText('Найден файл "' + file.name + '" ')
                    self.ui.tb_information.insertPlainText('Обработка... \n')

                    with open(file.path, encoding='utf8') as current_file:  # Открываем файл
                        csv_reader = csv.reader(current_file, delimiter=';')  # Считываем содержимое
                        counter = 0
                        rig_number = f'{rig_first_number}-{rig_second_number}'
                        file_data_list = [emitter_number, rig_number]  # Для хранения данных из файла
                        for record in csv_reader:  # Для каждой записи в файле
                            # print(record[1])
                            file_data_list.append(record[1])  # Вносим данные в список данных файла

                            counter += 1  # Увеличиваем счетчик записей
                            if counter > 10:  # Если записей больше 10
                                break  # Выходим из цикла
                        # print(file_data_list)
                        for elem in file_data_list:
                            self.ui.tb_information.insertPlainText('"' + str(elem) + '" ')

                        common_data_list.append(file_data_list)  # Вносим данные из списка текущего файла в общий список
                        emitter_number += 1
                        rig_second_number += 1
                        if rig_second_number > 12:
                            rig_first_number += 1
                            rig_second_number = 1

                    self.ui.tb_information.insertPlainText('\nОК' + '\n')
            if self.ui.tb_information.toPlainText() == '':
                self.ui.tb_information.insertPlainText('Файлы *.csv не найдены. Выберите другую папку')
        if common_data_list:
            # print(common_data_list)
            field_emitter_number = []
            field_rig_number = []
            field_date = []
            field_time = []
            field_t_source = []
            field_current = []
            field_pulse_duration = []
            field_pulse_period = []
            field_power = []
            field_power_comp = []
            field_snr = []
            field_rise_time = []
            field_fall_time = []
            field_emitting_power = []
            field_emitting_power_norm_on_23 = []
            # counter = 0
            # Для каждой записи в списке заполняем столбцы
            for file_data in common_data_list:
                field_emitter_number.append(file_data[0])
                field_rig_number.append(file_data[1])
                field_date.append(datetime.strptime(file_data[2], '%Y.%m.%d').date())
                field_time.append(datetime.strptime(file_data[3], '%H:%M:%S').time())
                field_t_source.append(float(file_data[4]))
                field_current.append(int(file_data[5]))
                field_pulse_duration.append(int(file_data[6]))
                field_pulse_period.append(int(file_data[7]))
                field_power.append(float(file_data[8]))
                field_power_comp.append(float(file_data[9]))
                field_snr.append(float(file_data[10]))
                field_rise_time.append(float(file_data[11]))
                field_fall_time.append(float(file_data[12]))
                field_emitting_power.append(float(file_data[8])/10)
                field_emitting_power_norm_on_23.append(float(file_data[9])/10)
                # Заносим в переменную данные по каждому столбцу Excel
            # print('Формирование файла Excel...')
            df = pd.DataFrame(
                {
                    '№ п.п.': field_emitter_number,
                    '№': field_rig_number,
                    'DATE': field_date,
                    'TIME': field_time,
                    'T_SOURCE[C]': field_t_source,
                    'CURRENT[mA]': field_current,
                    'PULSE_DURATION[us]': field_pulse_duration,
                    'PULSE_PERIOD[us]': field_pulse_period,
                    'POWER[uW]': field_power,
                    'POWER COMP.[uW]': field_power_comp,
                    'SNR': field_snr,
                    'RiseTime[ns]': field_rise_time,
                    'FallTime[ns]': field_fall_time,
                    'Сила излучения [мВт/ср]': field_emitting_power,
                    'Сила излучения норм. на 23° [мВт/ср]': field_emitting_power_norm_on_23,
                }
            )
            result_file_name = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохранить как...', path,
                                                                     'Файлы Excel (*.xlsx)')
            # Create a Pandas Excel writer using XlsxWriter as the engine.
            writer = pd.ExcelWriter(result_file_name[0], engine='xlsxwriter')

            # Convert the dataframe to an XlsxWriter Excel object.
            df.to_excel(writer, sheet_name='Sheet1', index=False)

            # Get the xlsxwriter workbook and worksheet objects.
            workbook = writer.book
            worksheet = writer.sheets['Result']

            # Add some cell formats.
            num_format = workbook.add_format({'num_format': '#.###############'})
            align_right_format = workbook.add_format({'align': 'right'})
            # format2 = workbook.add_format({'num_format': '0%'}

            # Note: It isn't possible to format any cells that already have a format such
            # as the index or headers or any cells that contain dates or datetimes.

            # Set the column width and format.
            worksheet.set_column('A:A', 10)
            worksheet.set_column('B:B', 10, cell_format=align_right_format)
            worksheet.set_column('C:C', 10)
            worksheet.set_column('D:D', 8)
            worksheet.set_column('E:E', 12)
            worksheet.set_column('F:F', 14)
            worksheet.set_column('G:G', 20)
            worksheet.set_column('H:H', 17)
            worksheet.set_column('I:I', 16, cell_format=num_format)
            worksheet.set_column('J:J', 19, cell_format=num_format)
            worksheet.set_column('K:K', 16, cell_format=num_format)
            worksheet.set_column('L:L', 12)
            worksheet.set_column('M:M', 16, cell_format=num_format)
            worksheet.set_column('N:N', 24, cell_format=num_format)
            worksheet.set_column('O:O', 36, cell_format=num_format)

            # Set the format but not the column width.
            # worksheet.set_column('C:C', None, format2)
            writer.save()
            # input('Завершено. Нажмите Enter для выхода')
            os.startfile(result_file_name[0])


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
