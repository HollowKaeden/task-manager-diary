# Интерфейс
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QInputDialog, QComboBox
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
import database as db


class main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.secondWin = None
        self.initUI()

    def initUI(self):
        global day
        db.connect()
        day = 1
        font = QFont('Comic sans', 14)
        self.setGeometry(300, 300, 900, 600)
        self.setWindowTitle('Расписание')
        self.label_day= QLabel(self)
        self.label_day.setText('Понедельник')
        self.label_day.setFont(font)
        self.label_day.move(280, 50)
        self.table = QTableWidget(self)
        self.table.setGeometry(0, 80, 900, 295)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Название', 'Домашнее задание', 'Заметки', 'Сделано/не сделано'])
        self.table.setRowCount(9)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 275)
        self.table.setColumnWidth(2, 275)
        self.table.setColumnWidth(3, 183)
        self.btn = QPushButton(self)
        self.btn.setText('Добавить урок')
        self.btn.setGeometry(20, 10, 150, 30)
        self.btn.setFont(font)
        self.btn.clicked.connect(self.add_lesson)
        self.btn1 = QPushButton(self)
        self.btn1.setText('Добавить ДЗ')
        self.btn1.setGeometry(190, 10, 150, 30)
        self.btn1.setFont(font)
        self.btn1.clicked.connect(self.add_homework)
        self.btn2 = QPushButton(self)
        self.btn2.setText('Добавить заметку')
        self.btn2.setGeometry(360, 10, 170, 30)
        self.btn2.setFont(font)
        self.btn2.clicked.connect(self.add_notes)
        self.btn3 = QPushButton(self)
        self.btn3.setText('←')
        self.btn3.setGeometry(570, 10, 40, 30)
        self.btn3.setFont(font)
        self.btn3.clicked.connect(self.previous_day)
        self.btn4 = QPushButton(self)
        self.btn4.setText('→')
        self.btn4.setGeometry(640, 10, 40, 30)
        self.btn4.setFont(font)
        self.btn4.clicked.connect(self.following_day)
        self.btn5 = QPushButton(self)
        self.btn5.setText('Изменить урок')
        self.btn5.setGeometry(20, 400, 150, 30)
        self.btn5.setFont(font)
        self.btn5.clicked.connect(self.name_lesson)

        hmrks = db.get_homework_lesson(day)
        for i in range(9):
            self.table.setItem(i, 1, QTableWidgetItem(hmrks.pop()))

        notes = db.get_comment_lesson(day)
        for i in range(9):
            self.table.setItem(i, 2, QTableWidgetItem(notes.pop()))

        lessons = db.get_lessons(1)
        for i in range(9):
            self.table.setItem(i, 0, QTableWidgetItem(lessons.pop()))
        self.show()

    def add_lesson(self):
        global day
        count = 0
        for i in db.get_lessons(day):
            if i != '':
                count += 1
        if count == 9:
            return
        text, ok = QInputDialog.getText(self, 'Урок',
                                        'Введите название урока')

        if ok:
            db.add_schedule(day, str(text))
            db.add_homework(db.take_lesson(day))
            db.add_comment(db.take_lesson(day))
            lessons = db.get_lessons(day)
            for i in range(9):
                self.table.setItem(i, 0, QTableWidgetItem(lessons.pop()))

    def add_homework(self):
        text, ok = QInputDialog.getText(self, 'Урок',
                                        'Введите номер урока')


        if ok:
            text1, ok1 = QInputDialog.getText(self, 'ДЗ',
                                              'Введите дз')
            if ok1:
                db.reset_homework(db.get_id_lesson(day)[-(int(text))], text1)
                hmrks = db.get_homework_lesson(day)
                for i in range(9):
                    self.table.setItem(i, 1, QTableWidgetItem(hmrks.pop()))


    def add_notes(self):
        text, ok = QInputDialog.getText(self, 'Урок',
                                        'Введите номер урока')

        if ok:
            text1, ok1 = QInputDialog.getText(self, 'Заметка',
                                              'Введите заметку')
            if ok1:
                db.reset_comment(db.get_id_lesson(day)[-(int(text))], text1)
                notes = db.get_comment_lesson(day)
                for i in range(9):
                    self.table.setItem(i, 2, QTableWidgetItem(notes.pop()))

    def previous_day(self):
        global day
        day -= 1
        if day == 0:
            day = 7
        lessons = db.get_lessons(day)
        for i in range(9):
            self.table.setItem(i, 0, QTableWidgetItem(lessons.pop()))
        hmrks = db.get_homework_lesson(day)
        for i in range(9):
            self.table.setItem(i, 1, QTableWidgetItem(hmrks.pop()))
        notes = db.get_comment_lesson(day)
        for i in range(9):
            self.table.setItem(i, 2, QTableWidgetItem(notes.pop()))
        self.label_day.setText(db.get_day(day))

    def following_day(self):
        global day
        day += 1
        if day == 8:
            day = 1
        lessons = db.get_lessons(day)
        for i in range(9):
            self.table.setItem(i, 0, QTableWidgetItem(lessons.pop()))
        hmrks = db.get_homework_lesson(day)
        for i in range(9):
            self.table.setItem(i, 1, QTableWidgetItem(hmrks.pop()))
        notes = db.get_comment_lesson(day)
        for i in range(9):
            self.table.setItem(i, 2, QTableWidgetItem(notes.pop()))
        self.label_day.setText(db.get_day(day))

    def name_lesson(self):
        text, ok = QInputDialog.getText(self, 'Урок',
                                        'Введите номер урока')

        if ok:
            text1, ok1 = QInputDialog.getText(self, 'Новое название',
                                              'Введите новое название урока')
            if ok1:
                db.reset_lesson(db.get_id_lesson(day)[-(int(text))], text1)
                lessons = db.get_lessons(day)
                for i in range(9):
                    self.table.setItem(i, 0, QTableWidgetItem(lessons.pop()))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main_window()
    sys.exit(app.exec_())