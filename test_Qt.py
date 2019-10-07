import sys, time, subprocess
from student_name import Ui_Frame
from Test_design import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog


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
        self.exit = self.ui.exit
        self.bar = self.ui.statusbar
        self.btnStud = self.ui_s.buttonBox
        self.lineStud = self.ui_s.student
        self.next.clicked.connect(self.fileOpen)
        self.open.triggered.connect(self.fileOpen)
        self.exit.triggered.connect(sys.exit)
        self.q1.hide()
        self.a1.hide()
        self.a2.hide()
        self.a3.hide()
        self.ch1.hide()
        self.ch2.hide()
        self.ch3.hide()
        self.count = 0
        self.result = 0
        self.percent = 0
        self.rep_key = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+R"), self)
        self.rep_key.activated.connect(self.openRep)

    def fileOpen(self):
        f_dialog = QFileDialog()
        f_dialog.setFileMode(QFileDialog.AnyFile)
        f_dialog.setNameFilter("Text (*.txt)")
        if f_dialog.exec_():
            self.file_name = f_dialog.selectedFiles()[0]
            try:
                f = open(self.file_name, 'r', encoding='cp1251')
            except Exception:
                f = open(self.file_name, 'r', encoding='utf-8')
                pass
            test_name = f.readline().strip()
            f.close()
            self.bar.showMessage(test_name)
            self.q1.show()
            self.q1.setText(test_name)
            self.next.clicked.disconnect()
            self.next.clicked.connect(self.studSet)
            self.makeTest()
        else:
            self.close()

    def makeTest(self):
        self.test_dic = {}
        try:
            with open(self.file_name, 'r', encoding='cp1251')as f:
                lines = len(f.readlines())
                test_name = f.readline()
                for i in range(lines):
                    buf = f.readline().split()
                    if buf[0] == 'Q':
                        self.test_dic[buf[1]]
        except Exception:
            pass

    def studSet(self):
        self.sFrame.show()
        self.btnStud.accepted.connect(self.studWrite)
        self.btnStud.rejected.connect(self.sFrame.hide)
        self.btnStud.rejected.connect(self.close)
        self.next.clicked.disconnect()
        # self.next.clicked.connect(self.testMain)

    def studWrite(self):
        # self.q1.show()
        self.ch1.show()
        self.ch2.show()
        self.ch3.show()
        self.a1.show()
        self.a2.show()
        self.a3.show()
        self.student = self.lineStud.text()
        self.sFrame.hide()
        self.start_time = time.time()
        self.testMain()

    def testMain(self):
        self.ch1.setChecked(False)
        self.ch2.setChecked(False)
        self.ch3.setChecked(False)

        # self.qst = self.f.readline().strip()
        # self.answ1 = self.f.readline().strip()
        # self.answ2 = self.f.readline().strip()
        # self.answ3 = self.f.readline().strip()
        # self.answ = self.f.readline().strip()
        # if not self.qst:
        #     self.a1.hide()
        #     self.a2.hide()
        #     self.a3.hide()
        #     self.ch1.hide()
        #     self.ch2.hide()
        #     self.ch3.hide()
        #     self.finish()
        # else:
        #     self.count += 1
        #     self.q1.setText(self.qst)
        #     self.a1.setText(self.answ1)
        #     self.a2.setText(self.answ2)
        #     self.a3.setText(self.answ3)
        #     self.bar.showMessage(self.testName + "                Вопрос №" \
        #                          + str(self.count) + "           Результат: " \
        #                          + str(self.percent))
        #     self.next.clicked.disconnect()
        #     self.next.clicked.connect(self.answ_check)

    def answerCheck(self):
        if self.ch1.isChecked():
            a = '1'
        elif self.ch2.isChecked():
            a = '2'
        elif self.ch3.isChecked():
            a = '3'
        else:
            a = '0'
        if a == self.answ:
            self.result += 1
        p = self.result * 100 / self.count
        self.percent = float("%.1f" % p)
        self.test_main()

    def finish(self):
        self.stopTime = time.time()
        self.spendTime = str(float("%.1f" % ((self.stopTime - self.starTime) / 60)))
        self.day = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if self.percent >= 90:
            self.mark = '5'
        elif self.percent >= 70:
            self.mark = '4'
        elif self.percent >= 45:
            self.mark = '3'
        elif self.percent >= 30:
            self.mark = '2'
        elif self.percent <= 29:
            self.mark = '1'
        self.rep = ("Дата: " + self.day +
                    "\nТестируемый: " + self.student.title() +
                    "\nТема: " + self.testName +
                    "\nПравильных ответов: " + str(self.result) +
                    "\nВсего вопросов: " + str(self.count) +
                    "\nЗатрачено времени: " + str(self.spendTime) + " мин."
                                                                    "\nРезультативность: " + str(self.percent) + "%"
                                                                                                                 "\nОценка: " + self.mark + "\n\n")
        self.q1.setText(self.rep)
        self.next.clicked.disconnect()
        self.next.setText("Закончить")
        self.next.clicked.connect(self.close)
        with open('report.txt', 'a', encoding='utf-8') as f_rep:
            f_rep.write(self.rep)

    def openRep(self):
        try:
            subprocess.Popen(['notepad.exe', r'report.txt'])
        except Exception as e:
            self.q1.show()
            e = str(e)
            self.q1.setText(e.title())
            pass

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.finish()
            self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = TestApp()
    application.show()
    sys.exit(app.exec_())
