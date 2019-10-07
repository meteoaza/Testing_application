from tkinter import *
import datetime
from tkinter.filedialog import askopenfilename

class TestMaint():
    def __init__(self, parent):

        #Variables
        self.day = datetime.datetime.today().strftime('%d.%m.%Y')
        self.clock = datetime.datetime.today().strftime('%H:%M')
        self.time = datetime.datetime.today()
        self.myfont = ("Helvetica", 20, "bold", "italic")
        self.myfont1 = ("Arial", 10, "bold")
        self.count = 0
        self.result = 0
        self.score = 0
        self.mark = "0"
        self.name = StringVar()
        self.selected = IntVar()
        self.parent = parent
        #launch
        self.window()
        
    def window(self):
        self.t = Text(root, font=self.myfont, bg="black", fg="lightgreen", height=5)
        self.e = Entry(root, textvariable=self.name, bg="grey", fg="black", width=40)
        self.b = Button(root, bg="green", fg="black", width=10)
        self.b1 = Radiobutton(root, activebackground="gray", indicatoron=0, cursor="hand2", fg="blue", value=1, variable=self.selected, font=self.myfont1)      
        self.b2 = Radiobutton(root, activebackground="gray", indicatoron=0, cursor="hand2", fg="blue", value=2, variable=self.selected, font=self.myfont1)      
        self.b3 = Radiobutton(root, activebackground="gray", indicatoron=0, cursor="hand2", fg="blue", value=3, variable=self.selected, font=self.myfont1)
        self.menubar = Menu(self.parent, tearoff=0)
        self.parent.config(menu=self.menubar)
        self.filemenu = Menu(self.menubar)
        self.filemenu.add_command(label="Открыть", command=self.openfile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Выход", command=self.end)
        self.menubar.add_cascade(label="Меню", menu=self.filemenu)
        self.menubar.add_cascade(label="Настройки", command=self.end)
        
    def openfile(self):
        filename = askopenfilename(filetypes =(("Text File", "*.txt"),("All Files","*.*")), title = "Choose a file.")
        self.test_f = open(filename, 'r', encoding='utf-8')
        self.test_name = self.test_f.readline().strip()
        self.start()
        
    def start(self):
        self.t.pack(fill=BOTH, expand=False)
        self.t.insert( INSERT, "Как Вас называть?")
        self.e.pack(anchor=N)
        self.e.focus()
        self.b.pack(anchor=S)
        self.b.config(text="Далее", command=self.hello)        
        
    def hello(self):
        self.name = self.name.get()       
        self.e.destroy()
        self.t.delete(1.0,  END)
        self.t.insert(INSERT, "Рад приветствовать, " + self.name.title() + "!\nЖелаю удачи в прохождении теста\n" + self.test_name + "!")
        self.b.config(text="Поехали", command=self.test_main)
        self.report()
        
    def analize(self):       
        i = self.selected.get()       
        if i == int(self.answer):
            self.result += 1
        else:
            self.test_fw = open('report.txt', 'a', encoding="utf-8")
            self.test_fw.write("\nВопрос: " + self.q + " Ответ: " + str(i))
            self.test_fw.close()              
        self.score = self.result*100/self.count
        if self.score <= 30:
            self.mark = "1"
        elif self.score >= 30:
            self.mark = "2"
        elif self.score >= 45:
            self.mark = "3"
        elif self.score >= 70:
            self.mark = "4"
        elif self.score >= 90:
            self.mark = "5"        
        self.test_main()
        
    def report(self):
        self.test_fw = open('report.txt', 'a', encoding="utf-8")
        self.test_fw.write("\n{:*^100}".format('тест-супер-тест') + "\nДата: " + self.day + "\nВремя " + self.clock + "\nТестируемый: "
                            + self.name.title() + "\nНазвание теста: " + self.test_name + "\n")
        self.test_fw.close()
        
    def report1(self):
        timediff = str(datetime.datetime.today() - self.time)
        self.desbtn()
        self.rep = ("\nВыполнено заданий: " + str(self.count) + "\nИз них правильно: " 
                    + str(self.result) + "\nЧто составляет " + str(self.score) + "% отвеченных вопросов " 
                    + "\nОценка " + self.mark + "\nЗатрачено времени " + timediff + "\n")
        self.t.delete(1.0, END)
        self.t.insert(INSERT, self.rep)
        self.test_fw = open('report.txt', 'a', encoding="utf-8")
        self.test_fw.write("\n" + self.rep)
        self.test_fw.close()             
    def end(self):
        root.destroy()
        
    def desbtn(self):
        self.b1.destroy()
        self.b2.destroy()
        self.b3.destroy()
        
    def test_main(self):
        self.b.destroy()
        self.b1.pack(anchor=W, fill=BOTH)
        self.b2.pack(anchor=W, fill=BOTH)
        self.b3.pack(anchor=W, fill=BOTH)
        self.q = self.test_f.readline().strip()
        self.t.delete(1.0, END)
        self.t.insert(1.0, self.q)
        if (not self.q):
            self.test_f.close()
            self.report1()
            self.b = Button(root, bg="red", fg="black", text="CLOSE", width=10, command=self.end)
            self.b.pack(anchor=S)
            self.desbtn()
        else:
            self.count += 1
            self.selected.set(0)
            self.b1.config(text=self.test_f.readline().strip(), command=self.analize)
            self.b2.config(text=self.test_f.readline().strip(), command=self.analize)
            self.b3.config(text=self.test_f.readline().strip(), command=self.analize)
            self.answer = self.test_f.readline().strip()
           
root = Tk()
root.title("Test Meteoaza")
root.geometry("1300x500")
app = TestMaint(root)
root.bind("<Escape>", TestMaint.end)
root.mainloop()
