import subprocess
import sys
import time
import random

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
        self.a_dic = {
            1: self.ui.answer1, 2: self.ui.answer2,
            3: self.ui.answer3, 4: self.ui.answer4, 5: self.ui.answer5
        }
        self.ch_dic = {
            1: self.ui.checkBox1, 2: self.ui.checkBox2,
            3: self.ui.checkBox3, 4: self.ui.checkBox4, 5: self.ui.checkBox5
        }
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
        for a in self.a_dic.values():
            a.hide()
        for ch in self.ch_dic.values():
            ch.hide()
        self.rep_key = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+R"), self)
        self.rep_key.activated.connect(self.openRep)

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
                        self.test_name = line[5:]
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
            self.q1.setStyleSheet('background: url(bkgnd.png)')
            self.q1.show()
            # self.q1.clear()
            self.q1.setText(self.test_name)
            self.next.clicked.disconnect()
            self.next.setText('Далее')
            self.next.clicked.connect(self.studSet)
        else:
            self.close()

    def studSet(self):
        # Student name input frame
        self.sFrame.show()
        application.hide()
        self.next.clicked.disconnect()
        self.btnStud.accepted.connect(self.testInit)
        self.btnStud.rejected.connect(self.sFrame.hide)
        self.btnStud.rejected.connect(self.close)

    def testInit(self):
        # Settings read from ini file
        try:
            with open('settings.ini', 'r', encoding='utf-8')as f:
                lines = f.readlines()
        except FileNotFoundError:
            with open('settings.ini', 'w', encoding='utf-8')as f:
                text = "SetCol 0\nRandom 0\nSetTry 20\nSetM_5 90 %\nSetM_4 70 %\nSetM_3 45 %\nSetM_2 30 %\n"
                text1 = "S etCol - (1:вкл, 0:отк) для отображения ошибок красным цветом\nR andom - (1:вкл, 0:отк) " \
                        "перемешать вопросы\nS etTry - количество вопросов в тесте\nS et_M  - критерии для оценок\n " \
                        "\n\nПодсказка для создания файла 'ваш_тест.txt':\nName - название теста\nQs  -  вопрос\nA1  -" \
                        "  ответ1\nA2  -  ответ2\nA3  -  ответ3\nA4  -  ответ4\nA5  -  ответ5\nAn  -  правильный ответ "
                f.write(text + '\n\n' + text1)
            time.sleep(0.5)
            with open('settings.ini', 'r', encoding='utf-8')as f:
                lines = f.readlines()
        try:
            for line in lines:
                if 'SetCol' in line[:7]:
                    self.color = int(line[7:9])
                elif 'Random' in line[:7]:
                    self.rand = int(line[7:9])
                elif 'SetTry' in line[:7]:
                    self.q_try = int(line[7:9])
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
        self.sFrame.hide()
        application.show()
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
                self.q1.setText(question)
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
                self.next.clicked.disconnect()
                self.next.setText("Далее")
                self.next.clicked.connect(lambda: self.answerCheck(key))
            except KeyError:
                tek = ['*** No more question', '', '', '', '']
                self.finish()
            self.q1.setStyleSheet("background-color:rgb(91, 213, 89)")
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
        self.next.clicked.disconnect()
        self.next.setText("Закончить")
        self.next.clicked.connect(self.close)

    def openRep(self):
        try:
            subprocess.Popen(['notepad.exe', r'report.txt'])
        except Exception as e:
            self.q1.show()
            self.q1.setText(str(e))

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
            self.bar.showMessage(
                "Время " + self.spent_time + "      " + "Тест:  " + self.test_name + "          Вопрос № " + str(
                    self.q_count + 1)
                + "          Результат: " + str(self.percent) + " %         Студент " + self.student + "         " +
                " Вопросов " + str(self.q_try) + "             Случайно  " + self.ifrand + "           Контроль  "
                + self.ifcolor
            )
            QTimer.singleShot(500, self.timeSpent)
        else:
            self.bar.showMessage(" ")

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
