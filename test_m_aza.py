import subprocess
import sys
import time
import random
import os
import winreg

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QFileDialog, QFrame, QShortcut

from Test_design import Ui_MainWindow
from student_name import Ui_Frame as Stud
from Test_sett_design import Ui_Frame as Settings


class TestApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.studFrame = QFrame()
        self._s = Stud()
        self._s.setupUi(self.studFrame)
        self.settFrame = QFrame()
        self._set = Settings()
        self._set.setupUi(self.settFrame)
        self.q1 = self.ui.question
        self.a_dic = {
            1: self.ui.answer1, 2: self.ui.answer2,
            3: self.ui.answer3, 4: self.ui.answer4, 5: self.ui.answer5
        }
        self.ch_dic = {
            1: self.ui.checkBox1, 2: self.ui.checkBox2,
            3: self.ui.checkBox3, 4: self.ui.checkBox4, 5: self.ui.checkBox5
        }
        self.next = self.ui.next
        self.print = self.ui.print
        self.open = self.ui.open
        self.settings = self.ui.settings
        self.exit = self.ui.exit
        self.about = self.ui.about
        self.bar = self.ui.statusbar
        self.btnStud = self._s.buttonBox
        self.lineStud = self._s.student
        self.next.clicked.connect(self.fileOpen)
        self.print.clicked.connect(self.printer)
        self.open.triggered.connect(self.fileOpen)
        self.settings.triggered.connect(self.settFrameShow)
        self.about.triggered.connect(self.aboutMenu)
        self.exit.triggered.connect(sys.exit)
        self.q1.hide()
        self.print.hide()
        for a in self.a_dic.values():
            a.hide()
        for ch in self.ch_dic.values():
            ch.hide()
        self.rep_key = QShortcut(QtGui.QKeySequence("Ctrl+R"), self)
        self.rep_key.activated.connect(self.openRep)
        self.ui.centralwidget.setStyleSheet('background: url(bkgnd.png)')
        self.font1 = QFont("Comic Sans Ms", 20, QFont.DemiBold, QFont.AnyStyle)
        self.font2 = QFont("Arial Rounded MT Bold", 25, QFont.Bold)


    def fileOpen(self):
        # Open test file and create question-answer dictionary
        f_dialog = QFileDialog()
        f_dialog.setFileMode(QFileDialog.AnyFile)
        f_dialog.setNameFilter("Text (*.txt)")
        if f_dialog.exec_():
            self.file_name = f_dialog.selectedFiles()[0]
            self.test = {}
            try:
                with open(self.file_name, 'r', encoding='utf-8')as f:
                    lines = f.readlines()
            except Exception:
                with open(self.file_name, 'r', encoding='cp1251')as f:
                    lines = f.readlines()
                pass
            for line in lines:
                try:
                    if not 'Name' in lines[0]:
                        self.test_name = 'Не найдено название теста'
                    elif 'Name' in line[:5]:
                        self.test_name = line[6:]
                except Exception:
                    pass
            n = 0
            t = []
            test_dic = dict.fromkeys(('Qs', 'A1', 'A2', 'A3', 'A4', 'A5', 'An'), 0)
            for line in lines:
                for k in test_dic.keys():
                    if k in line[:3]:
                        t.append(line)
                        if 'An' in line[:3]:
                            self.test.update({n: t})
                            n += 1
                            t = []
            self.q1.show()
            self.q1.setText("\n\n" + self.test_name)
            self.q1.setStyleSheet("")
            self.q1.setFrameStyle(QFrame.NoFrame)
            self.next.clicked.disconnect()
            self.next.setText('Далее')
            self.next.clicked.connect(self.studSet)
            self.print.hide()
            self.ui.menubar.hide()
            self.ui.centralwidget.setStyleSheet('background: url(bkgnd.png)')
        else:
            self.close()

    def studSet(self):
        # Student name input frame
        self.studFrame.show()
        application.hide()
        self.next.clicked.disconnect()
        self.btnStud.accepted.connect(self.testInit)
        self.btnStud.rejected.connect(self.studFrame.hide)
        self.btnStud.rejected.connect(self.close)

    def testInit(self):
        self.settRead()
        # Define variables
        self.fin = True
        self.q_num_list = []
        self.result = 0
        self.percent = 0
        self.q_count = 0
        self.start_time = time.time()
        self.student = self.lineStud.text().title()
        # Check if questions in settings not exceed questions in self.test dictionary
        if self.q_try > len(self.test):
            self.q_try = len(self.test)
        # Vars for messagebar (random and color)
        if self.rand:
            self.ifrand = 'ВКЛ'
        else:
            self.ifrand = 'ОТКЛ'
        if self.color:
            self.ifcolor = 'ВКЛ'
        else:
            self.ifcolor = 'ОТКЛ'
        self.studFrame.hide()
        application.show()
        self.q1.setFont(self.font1)
        self.q1.setText("\n\n\n" + self.student + ", желаю удачи в прохождении теста:\n" + self.test_name)
        self.next.setText("Поехали!")
        self.next.clicked.connect(self.testMain)

    def testMain(self):
        self.timeSpent()
        if self.q_try:
            if not self.rand:
                self.q_num = self.q_count
            else:
                self.q_num = random.choice(list(self.test))
                if self.q_num in self.q_num_list:
                    while self.q_num in self.q_num_list:
                        self.q_num = random.choice(list(self.test))
                self.q_num_list.append(self.q_num)
            try:
                tek = self.test[self.q_num]
                question = tek[0][3:]
                frame = 1
                for k, a in self.a_dic.items():
                    try:
                        tek_a = tek[k]
                        if 'An' in tek_a:
                            pass
                        else:
                            a.setText(tek_a[3:])
                            frame += 1
                    except IndexError:
                        pass
                key = [int(i) for i in tek[-1][3:].split()]
                key.sort()
                for i in range(1, frame):
                    a = self.a_dic[i]
                    a.show()
                    ch = self.ch_dic[i]
                    ch.show()
                self.next.show()
                self.q1.setFont(self.font2)
                self.q1.setText(question)
                self.q1.setFrameShape(QFrame.WinPanel)
                self.q1.setStyleSheet("background-color:rgb(91, 213, 89)")
                self.ui.centralwidget.setStyleSheet(" ")
                self.next.setText("Далее")
                self.next.clicked.disconnect()
                self.next.clicked.connect(lambda: self.answerCheck(key))
            except KeyError:
                tek = ['*** No more question', '', '', '', '']
                self.finish()
        else:
            self.finish()

    def answerCheck(self, key):
        self.q_count += 1
        self.q_try -= 1
        answer = []
        for k, v in self.ch_dic.items():
            if v.isChecked():
                answer.append(k)
                v.setChecked(False)
        for a in self.a_dic.values():
            a.clear()
        if key == answer:
            self.result += 1
        else:
            if self.color == 1:
                self.q1.setStyleSheet("background-color: rgb(255, 0, 0)")
        if self.q_count == 0:
            p = 0
        else:
            p = self.result * 100 / self.q_count
        self.percent = float("%.1f" % p)
        for a in self.a_dic.values():
            a.hide()
        for ch in self.ch_dic.values():
            ch.hide()
        self.next.hide()
        QTimer.singleShot(100, self.testMain)

    def finish(self):
        self.fin = False
        self.day = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if self.percent >= self.mark_5:
            self.mark = '5'
        elif self.percent >= self.mark_4:
            self.mark = '4'
        elif self.percent >= self.mark_3:
            self.mark = '3'
        elif self.percent >= self.mark_2:
            self.mark = '2'
        else:
            self.mark = '1'
        if int(self.mark) > 3:
            self.q1.setStyleSheet("background-color:rgb(91, 213, 89)")
        else:
            self.q1.setStyleSheet("background-color: rgb(255, 0, 0)")
        self.rep = (
                "Дата: " + self.day +
                "\nТестируемый: " + self.student +
                "\nТема: " + self.test_name +
                "\nПравильных ответов: " + str(self.result) +
                "\nВсего вопросов: " + str(self.q_count) +
                "\nЗатрачено времени: " + str(self.spent_time) + " мин."
                                                                 "\nРезультативность: " + str(self.percent) + "%"
                                                                                                              "\nОценка: " + self.mark + "\n\n")
        with open('report.txt', 'a', encoding='utf-8') as f_rep:
            f_rep.write(self.rep)
        self.q1.setText(self.rep)
        self.next.show()
        self.print.show()
        self.next.clicked.disconnect()
        self.next.setText("Закончить")
        self.next.clicked.connect(self.close)
        self.ui.menubar.show()

    def openRep(self):
        try:
            subprocess.Popen(['notepad.exe', r'report.txt'])
        except Exception as e:
            self.q1.show()
            self.q1.setText(str(e))

    def settFrameShow(self):
        self.settRead()
        if self.color == 1:
            self._set.colBox.isChecked()
        if self.rand == 1:
            self._set.ranBox.isChecked()
        self._set.tryLine.setText(str(self.q_try))
        self._set.mark5Line.setText(str(self.mark_5))
        self._set.mark4Line.setText(str(self.mark_4))
        self._set.mark3Line.setText(str(self.mark_3))
        self._set.mark2Line.setText(str(self.mark_2))
        self.settFrame.show()
        self._set.buttonBox.accepted.connect(self.settWrite)
        self._set.buttonBox.rejected.connect(self.settFrame.close)

    def settWrite(self):
        if self._set.colBox.isChecked():
            self.color = 1
        else:
            self.color = 0
        if self._set.ranBox.isChecked():
            self.rand = 1
        else:
            self.rand = 0
        self.q_try = self._set.tryLine.text()
        self.mark_5 = self._set.mark5Line.text()
        self.mark_4 = self._set.mark4Line.text()
        self.mark_3 = self._set.mark3Line.text()
        self.mark_2 = self._set.mark2Line.text()
        settings = [
            self.color, self.rand, self.q_try, self.mark_5,
            self.mark_4, self.mark_3, self.mark_2
        ]
        with open("settings.ini", "w", encoding='utf-8')as f:
            for i in settings:
                f.write("%s " % i)
        self.settFrame.close()

    def settRead(self):
        # Settings read from ini file
        try:
            with open('settings.ini', 'r', encoding='utf-8')as f:
                line = f.readline().split()
                line = [int(l) for l in line]
        except FileNotFoundError:
            self.q1.setText("Нет файла настроек программы!!! Зайдите в настройки! ")
        self.color = line[0]
        self.rand = line[1]
        self.q_try = line[2]
        self.mark_5 = line[3]
        self.mark_4 = line[4]
        self.mark_3 = line[5]
        self.mark_2 = line[6]

    def timeSpent(self):
        if self.fin:
            t = int(time.time()) - int(self.start_time)
            if t >= 60:
                tm = int(t / 60)
                ts = t - tm * 60
            else:
                tm = 0
                ts = t
            if ts < 10:
                self.spent_time = str(tm) + ":0" + str(ts)
            else:
                self.spent_time = str(tm) + ":" + str(ts)
            self.bar.showMessage(
                "Время " + self.spent_time + "  Тест: " + self.test_name + "  Вопрос №" + str(self.q_count + 1)
                + "  Результат: " + str(self.percent) + "%  Студент " + self.student + "  Вопросов " +
                str(self.q_try) + "  Случайно " + self.ifrand + "  Контроль " + self.ifcolor
            )
            QTimer.singleShot(500, self.timeSpent)
        else:
            self.bar.showMessage(" ")

    def printer(self):
        with open('temp.txt', 'w', encoding='utf-8')as f:
            f.write(self.rep)
        os.startfile("temp.txt", "print")
        time.sleep(3)
        os.remove("temp.txt")


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            try:
                self.finish()
            except AttributeError:
                pass
            self.close()

    def aboutMenu(self):
        self.q1.setFont(self.font1)
        self.q1.show()
        self.q1.setText(
            'Программа для тестирования была написана для проведения проверки знаний у персонала ГП "Кыргызаэронавигация"\n'
            'Настройка и использование программы не должны вызвать каких-либо затруднений. Для настройки нажмите "Меню"'
            '-> "Настройки"\nВ случае возникновения вопросов прошу обращаться.\n\nРазработчик: Мамутов А'
        )


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = TestApp()
    application.show()
    sys.exit(app.exec_())
