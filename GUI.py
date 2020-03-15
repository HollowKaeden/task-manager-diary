# Интерфейс
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
import database as db


class main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.secondWin = None
        self.initUI()

    def initUI(self):
        db.connect()
        font = QFont('Comic sans', 14)
        self.setGeometry(1000, 600, 717, 600)
        self.setWindowTitle('Расписание')
        self.table = QTableWidget(self)
        self.table.setGeometry(0, 80, 717, 295)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Название', 'Домашнее задание', 'Заметки'])
        self.table.setRowCount(9)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 275)
        self.table.setColumnWidth(2, 275)
        self.btn = QPushButton(self)
        self.btn.setText('Добавить урок')
        self.btn.setGeometry(20, 10, 150, 30)
        self.btn.setFont(font)
        self.btn.clicked.connect(self.add_lesson)
        self.btn1 = QPushButton(self)
        self.btn1.setText('Добавить ДЗ')
        self.btn1.setGeometry(190, 10, 150, 30)
        self.btn1.setFont(font)
        self.btn2 = QPushButton(self)
        self.btn2.setText('Добавить заметку')
        self.btn2.setGeometry(360, 10, 170, 30)
        self.btn2.setFont(font)
        self.btn3 = QPushButton(self)
        self.btn3.setText('←')
        self.btn3.setGeometry(570, 10, 40, 30)
        self.btn3.setFont(font)
        self.btn4 = QPushButton(self)
        self.btn4.setText('→')
        self.btn4.setGeometry(640, 10, 40, 30)
        self.btn4.setFont(font)
        lessons = db.get_lessons('Понедельник')
        for i in range(9):
            self.table.setItem(i, 0, QTableWidgetItem(lessons.pop()))
        self.show()

    def add_lesson(self):
        print(1)

    def add_homework(self):
        pass

    def add_notes(self):
        pass

    def previous_day(self):
        pass

    def following_day(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main_window()
    sys.exit(app.exec_())
