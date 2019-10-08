import subprocess
import sys
import time

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QFileDialog

from Test_design import Ui_MainWindow
from student_name import Ui_Frame


class TestApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sFrame = QtWidgets.QFrame()
        self.ui_s = Ui_Frame()
        self.ui_s.setupUi(self.sFrame)
        self.q1 = self.ui.question
        self.a1 = self.ui.answer1
        self.a2 = self.ui.answer2
        self.a3 = self.ui.answer3
        self.ch1 = self.ui.checkBox1
        self.ch2 = self.ui.checkBox2
        self.ch3 = self.ui.checkBox3
        self.next = self.ui.next
        self.open = self.ui.open
        self.settings = self.ui.settings
        self.exit = self.ui.exit
        self.bar = self.ui.statusbar
        self.btnStud = self.ui_s.buttonBox
        self.lineStud = self.ui_s.student
        self.next.clicked.connect(self.fileOpen)
        self.open.triggered.connect(self.fileOpen)
        self.settings.triggered.connect(self.settShow)
        self.exit.triggered.connect(sys.exit)
        self.q1.hide()
        self.a1.hide()
        self.a2.hide()
        self.a3.hide()
        self.ch1.hide()
        self.ch2.hide()
        self.ch3.hide()
        self.answer_count = 0
        self.result = 0
        self.percent = 0
        self.q_count = 0
        self.fin = True
        self.rep_key = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+R"), self)
        self.rep_key.activated.connect(self.openRep)
        # Settings read from ini file
        try:
            with open('settings.ini', 'r', encoding='utf-8')as f:
                lines = f.readlines()
        except FileNotFoundError:
            with open('settings.ini', 'w', encoding='utf-8')as f:
                text = "SetCol 1\nSetM_5 90 %\nSetM_4 70 %\nSetM_3 45 %\nSetM_2 30 %\n"
                text1 = "Name - название теста\nQs  -  вопрос\nA1  -  ответ1\nA2  -  ответ2\nA3  -  ответ3\nAn  -  " \
                        "правильный ответ "
                f.write(text + '\n\n' + text1)
            time.sleep(0.5)
            with open('settings.ini', 'r', encoding='utf-8')as f:
                lines = f.readlines()
        try:
            for line in lines:
                if 'SetCol' in line[:7]:
                    self.color = int(line[7:])
                elif 'SetM_5' in line[:7]:
                    self.mark_5 = int(line[7:9])
                elif 'SetM_4' in line[:7]:
                    self.mark_4 = int(line[7:9])
                elif 'SetM_3' in line[:7]:
                    self.mark_3 = int(line[7:9])
                elif 'SetM_2' in line[:7]:
                    self.mark_2 = int(line[7:9])
        except Exception as e:
            self.q1.show()
            self.q1.setText('Settings error!!! ')
        pass

    def fileOpen(self):
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
                        self.test_name = line[5:]

                except Exception:
                    pass
            n = 0
            for line in lines:
                try:
                    if 'Qs' in line[:2]:
                        q = line
                        n += 1
                    elif 'A1' in line[:2]:
                        a1 = line
                    elif 'A2' in line[:2]:
                        a2 = line
                    elif 'A3' in line[:2]:
                        a3 = line
                    elif 'An' in line[:2]:
                        k = line
                    self.test[n - 1] = [q, a1, a2, a3, k]
                except NameError:
                    pass
            self.bar.showMessage(self.test_name)
            self.q1.show()
            self.q1.setText(self.test_name)
            self.next.clicked.disconnect()
            self.next.clicked.connect(self.studSet)
        else:
            self.close()

    def studSet(self):
        self.sFrame.show()
        self.btnStud.accepted.connect(self.studWrite)
        self.btnStud.rejected.connect(self.sFrame.hide)
        self.btnStud.rejected.connect(self.close)
        self.next.clicked.disconnect()
        application.hide()

    def studWrite(self):
        application.show()
        self.ch1.show()
        self.ch2.show()
        self.ch3.show()
        self.a1.show()
        self.a2.show()
        self.a3.show()
        self.student = self.lineStud.text().title()
        self.sFrame.hide()
        self.start_time = time.time()
        self.testMain()
        self.timeSpent()

    def testMain(self):
        try:
            tek = self.test[self.q_count]
            question = tek[0][3:]
            self.q1.setText(question)
            answer1 = tek[1][3:]
            self.a1.setText(answer1)
            answer2 = tek[2][3:]
            self.a2.setText(answer2)
            answer3 = tek[3][3:]
            self.a3.setText(answer3)
            key = tek[4][3:]
            self.next.clicked.connect(lambda: self.answerCheck(key))
        except KeyError:
            tek = ['*** No more question', '', '', '', '']
            self.finish()
        self.q1.setStyleSheet("background-color:rgb(0, 200, 0)")

    def answerCheck(self, key):
        self.q_count += 1
        self.next.clicked.disconnect()
        if self.ch1.isChecked():
            a = 1
        elif self.ch2.isChecked():
            a = 2
        elif self.ch3.isChecked():
            a = 3
        else:
            a = 0
        self.ch1.setChecked(False)
        self.ch2.setChecked(False)
        self.ch3.setChecked(False)
        if int(key) == a:
            self.result += 1
        else:
            if self.color == 1:
                self.q1.setStyleSheet("background-color: rgb(255, 0, 0)")
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

        self.rep = ("Дата: " + self.day +
                    "\nТестируемый: " + self.student +
                    "\nТема: " + self.test_name +
                    "\nПравильных ответов: " + str(self.result) +
                    "\nВсего вопросов: " + str(self.q_count) +
                    "\nЗатрачено времени: " + str(self.spent_time) + " мин."
                                                                     "\nРезультативность: " + str(self.percent) + "%"
                                                                                                                  "\nОценка: " + self.mark + "\n\n")
        with open('report.txt', 'a', encoding='utf-8') as f_rep:
            f_rep.write(self.rep)
        self.q_count = 0
        self.q1.setText(self.rep)
        self.a1.hide()
        self.a2.hide()
        self.a3.hide()
        self.ch1.hide()
        self.ch2.hide()
        self.ch3.hide()
        self.next.setText("Закончить")
        self.next.clicked.connect(self.close)

    def openRep(self):
        try:
            subprocess.Popen(['notepad.exe', r'report.txt'])
        except Exception as e:
            self.q1.show()
            self.q1.setText(str(e))
            pass

    def settShow(self):
        try:
            subprocess.Popen(['notepad.exe', r'settings.ini'])
        except Exception:
            pass

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
            if self.q_count == 0:
                p = 0
            else:
                p = self.result * 100 / self.q_count
            self.percent = float("%.1f" % p)
            self.bar.showMessage(
                "Время " + self.spent_time + "      " + "Тест:  " + self.test_name + "          Вопрос № " + str(
                    self.q_count + 1)
                + "          Результат: " + str(self.percent) + " %         Студент " + self.student)
            QTimer.singleShot(1000, self.timeSpent)
        else:
            pass

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            try:
                self.finish()
            except AttributeError:
                pass
            self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = TestApp()
    application.show()
    sys.exit(app.exec_())
