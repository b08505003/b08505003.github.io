from tkinter import *
from tkinter import ttk
from tkinter.constants import *
from random import *


dataBase = []
data = {}
db_part = []
totalPoint = 0
numOfQuestion = 5   #題數
difficulty = 1
diff_part = [26,41,62,83]   #難度分部

def read_file():
    global dataBase
    f = open("UmaData.txt","r",encoding="utf-8")
    dataBase = f.readlines()
    f.close()


class app:
    
    def __init__(self, master):
        self.master = master
        self.master.geometry("700x500")
        self.master.title("ウマ娘クイズ")
        self.master.resizable(0,0)
        p1 = PhotoImage(file = 'Icon.png')
        self.master.iconphoto(True,p1)
        read_file()
        self.homePage()
    
    def homePage(self):
        global totalPoint, numOfQuestion

        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master)
        self.frame1.pack(fill="x")
        self.index = 0
        totalPoint = 0
        while len(db_part)!=0:
            db_part.pop(0)

        for i in range(diff_part[difficulty]):
            db_part.append(dataBase[i])
        
        self.gameStart = ttk.Button(self.frame1, text="開始", command=self.gamePage)
        self.gameStart.pack(fill="x")

        self.setDifficulty = ttk.Button(self.frame1, text="難易度", command=self.difficulty)
        self.setDifficulty.pack(fill="x")

        self.chooseNum = ttk.Button(self.frame1, text="選擇題數", command=self.chooseNumPage)
        self.chooseNum.pack(fill="x")

        self.dataBaseDisplay = ttk.Button(self.frame1, text="檢視題庫", command=self.dataDisplay)
        self.dataBaseDisplay.pack(fill="x")

        self.log = ttk.Button(self.frame1, text="更新日誌", command=self.logPage)
        self.log.pack(fill="x")

        self.finish = ttk.Button(self.frame1, text="結束", command=self.quit)
        self.finish.pack(fill="x")

    
    def gamePage(self):
        global dataBase
        global data
        global totalPoint
        self.index += 1
        for i in self.master.winfo_children():
            i.destroy()

        if self.index == 1:
            self.question = sample(range(len(db_part)),numOfQuestion)
        
        part = db_part[self.question[self.index-1]].split()
        data = {
        "名字" : part[0],
        "育成目標比賽" : part[1],
        "距離適性" : part[2],
        "稱號" : part[3],
        "騎手" : part[4],
        "年代" : part[5],
        "代表比賽" : part[6],
        "提示" : part[7]
        }
        
        
        self.f1 = Frame(self.master,borderwidth=1,relief=SOLID)
        self.f1.pack(side="left",fill="both",expand=1)
        self.f2 = Frame(self.master,borderwidth=1,relief=SOLID)
        self.f2.pack(side="left",fill="both",expand=1)
        self.f3 = Frame(self.f1)
        self.f3.pack(fill="x")
        self.f4 = Frame(self.f1)
        self.f4.pack(fill="x")
        self.f5 = Frame(self.f1)
        self.f5.pack(fill="x")
        self.f6 = Frame(self.f1)
        self.f6.pack(fill="x")
        self.f7 = Frame(self.f1)
        self.f7.pack(fill="x")
        self.f8 = Frame(self.f1)
        self.f8.pack(fill="x")

        self.txt1 = ttk.Label(self.f3, text="第"+str(self.index)+"題    請選擇下列其中一個提示開始")
        self.txt1.pack(anchor=W)
        self.btn1 = ttk.Button(self.f3, text="遊戲育成目標比賽",command=self.race)
        self.btn1.pack(side="left",anchor=W)
        self.btn2 = ttk.Button(self.f3, text="代表比賽(含年份)",command=self.representativeRace)
        self.btn2.pack(side="left",anchor=W)
        self.btn3 = ttk.Button(self.f4, text="主戰騎手",command=self.jockey, state=DISABLED)
        self.btn3.pack(side="left",anchor=W)
        self.btn4 = ttk.Button(self.f4, text="距離適性",command=self.ability, state=DISABLED)
        self.btn4.pack(side="left",anchor=W)
        self.btn5 = ttk.Button(self.f5, text="稱號",command=self.secondName, state=DISABLED)
        self.btn5.pack(side="left",anchor=W)
        self.btn6 = ttk.Button(self.f5, text="額外提示",command=self.lastHint, state=DISABLED)
        self.btn6.pack(side="left",anchor=W)
        self.btn7 = ttk.Button(self.f1, text="返回主畫面",command=self.homePage)
        self.btn7.pack(side="left",anchor=SW)
        self.txt2 = ttk.Label(self.f2, text="目前的提示")
        self.txt2.pack(anchor=W)

        self.btnpressed = [False,False,False,False,False,False]

        self.reply = StringVar()
        self.reply.set("")

        self.l1 = ttk.Label(self.f6, text="請輸入答案")
        self.l1.pack(side="left",anchor=NW)
        self.entry = ttk.Entry(self.f6, textvariable=self.reply)
        self.entry.pack(side="left",anchor=NW)
        self.submit = ttk.Button(self.f6, text="確認",width=10,command=self.submit_answer)
        self.submit.pack(side="left",anchor=NW)
        self.give_up = ttk.Button(self.f6, text="放棄",width=5,command=self.giveUp,state=DISABLED)
        self.give_up.pack(side="left",anchor=NW)

        self.answer_l1 = ttk.Label(self.f7, text="")
        self.answer_l1.pack(side="left",anchor=NW)
        

    def submit_answer(self):
        global data
        global totalPoint,numOfQuestion
        name = data["名字"].split("/")
        answer = self.reply.get()
        

        if answer == name[0] or answer == name[1]:
            point = self.btnpressed.count(False)
            self.submit.config(state=DISABLED)
            self.answer_l1.config(text="答案正確! +" + str(point) + "分")
            totalPoint += point
            
            if self.index < numOfQuestion:
                btn1 = ttk.Button(self.f7, text="下一題",command=self.gamePage)
                btn1.pack(side="left",anchor=NW)
            else:
                l1 = ttk.Label(self.f8, text="遊戲結束! 得分:" + str(totalPoint) + "/" + str(5*numOfQuestion))
                l1.pack(side="left",anchor=NW)
                btn1 = ttk.Button(self.f8, text="回到主畫面",command=self.homePage)
                btn1.pack(side="left",anchor=NW)
            self.btn1.config(state=DISABLED)
            self.btn2.config(state=DISABLED)
            self.btn3.config(state=DISABLED)
            self.btn4.config(state=DISABLED)
            self.btn5.config(state=DISABLED)
            self.btn6.config(state=DISABLED)
            
        else:
            self.answer_l1.config(text="答案錯誤!")

    def giveUp(self):
        global totalPoint
        self.answer_l1.config(text="放棄回答    -2分")
        totalPoint -= 2
        if self.index < numOfQuestion:
                btn1 = ttk.Button(self.f7, text="下一題",command=self.gamePage)
                btn1.pack(side="left",anchor=NW)
        else:
            l1 = ttk.Label(self.f8, text="遊戲結束! 得分:" + str(totalPoint) + "/" + str(5*numOfQuestion))
            l1.pack(side="left",anchor=NW)
            btn1 = ttk.Button(self.f8, text="回到主畫面",command=self.homePage)
            btn1.pack(side="left",anchor=NW)
        self.give_up.config(state=DISABLED)
    
    def race(self):
        txt = data["育成目標比賽"].replace("1","☆ ")
        txt = txt.replace("2","◯ ")
        txt = txt.replace("3","◾")
        txt = txt.split(",")
        s = ""
        for race in txt:
            s += (race + "\n")
        l1 = ttk.Label(self.f2, text="育成目標比賽(☆第一,◯第二,◾未出走或第三以後):")
        l1.pack(anchor=W)
        hint1 = ttk.Label(self.f2, text=s)
        hint1.pack(anchor=W)
        self.btn1.config(state=DISABLED)
        self.btnpressed[0] = True
        if self.btnpressed[2] == False and self.btnpressed[3] == False:
            self.btn3.config(state=ACTIVE)
            self.btn4.config(state=ACTIVE)
        self.lastHintCheck()
        

    def representativeRace(self):
        races = data["代表比賽"].split("/")
        race = choice(races)
        l1 = ttk.Label(self.f2, text="生涯代表比賽:")
        l1.pack(anchor=W)
        l2 = ttk.Label(self.f2, text=(race+"\n"))
        l2.pack(anchor=W)
        self.btn2.config(state=DISABLED)
        self.btnpressed[1] = True
        if self.btnpressed[2] == False and self.btnpressed[3] == False:
            self.btn3.config(state=ACTIVE)
            self.btn4.config(state=ACTIVE)
        self.lastHintCheck()
        

    def jockey(self):
        global data
        l1 = ttk.Label(self.f2, text="主戰騎手:")
        l1.pack(anchor=W)
        l2 = ttk.Label(self.f2, text=(data["騎手"]+"\n"))
        l2.pack(anchor=W)
        self.btn3.config(state=DISABLED)
        self.btnpressed[2] = True
        self.lastHintCheck()

    def ability(self):
        global data
        l1 = ttk.Label(self.f2, text="距離適性:")
        l1.pack(anchor=W)
        l2 = ttk.Label(self.f2, text=(data["距離適性"]+"\n"))
        l2.pack(anchor=W)
        self.btn4.config(state=DISABLED)
        self.btnpressed[3] = True
        self.lastHintCheck()

    def secondName(self):
        global data
        l1 = ttk.Label(self.f2, text="稱號:")
        l1.pack(anchor=W)
        l2 = ttk.Label(self.f2, text=(data["稱號"]+"\n"))
        l2.pack(anchor=W)
        self.btn5.config(state=DISABLED)
        self.btnpressed[4] = True
        if self.btnpressed.count(False) == 0:
            self.give_up.config(state=ACTIVE)

    def lastHint(self):
        global data
        hint = data["提示"].split("/")
        s = ""
        for l in hint:
            s += (l + "\n")
        l1 = ttk.Label(self.f2, text="最後提示:")
        l1.pack(anchor=W)
        l2 = ttk.Label(self.f2, text=l)
        l2.pack(anchor=W)
        self.btn6.config(state=DISABLED)
        self.btnpressed[5] = True
        if self.btnpressed.count(False) == 0:
            self.give_up.config(state=ACTIVE)

    def lastHintCheck(self):
        if self.btnpressed.count(True) == 4:
                self.btn5.config(state=ACTIVE)
                self.btn6.config(state=ACTIVE)

    def difficulty(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.easy = Button(self.master, text="簡單 (動畫常見角色+漫畫重要角色)", command=self.setEasy)
        self.easy.pack(fill="x")
        self.normal = Button(self.master, text="普通 (動畫配角+漫畫常見角色)", command=self.setNormal)
        self.normal.pack(fill="x")
        self.hard = Button(self.master, text="困難 (動畫漫畫邊緣角)", command=self.setHard)
        self.hard.pack(fill="x")
        self.veryHard = Button(self.master, text="超困難 (其他遊戲角)", command=self.setVeryHard)
        self.veryHard.pack(fill="x")
        self.origin = self.easy.cget("background")
        if difficulty == 0:
            self.easy.config(bg="#9C9C9C")
        elif difficulty == 1:
            self.normal.config(bg="#9C9C9C")
        elif difficulty == 2:
            self.hard.config(bg="#9C9C9C")
        elif difficulty == 3:
            self.veryHard.config(bg="#9C9C9C")
        f1 = Frame(self.master,height=20)
        f1.pack(fill="x")
        back = ttk.Button(self.master, text="返回", command=self.homePage)
        back.pack(fill="x")

    def setEasy(self):
        global difficulty
        difficulty = 0
        self.easy.config(bg="#9C9C9C")
        self.normal.config(bg=self.origin)
        self.hard.config(bg=self.origin)
        self.veryHard.config(bg=self.origin)
    def setNormal(self):
        global difficulty
        difficulty = 1
        self.easy.config(bg=self.origin)
        self.normal.config(bg="#9C9C9C")
        self.hard.config(bg=self.origin)
        self.veryHard.config(bg=self.origin)
    def setHard(self):
        global difficulty
        difficulty = 2
        self.easy.config(bg=self.origin)
        self.normal.config(bg=self.origin)
        self.hard.config(bg="#9C9C9C")
        self.veryHard.config(bg=self.origin)
    def setVeryHard(self):
        global difficulty
        difficulty = 3
        self.easy.config(bg=self.origin)
        self.normal.config(bg=self.origin)
        self.hard.config(bg=self.origin)
        self.veryHard.config(bg="#9C9C9C")

    def chooseNumPage(self):
        for i in self.master.winfo_children():
            i.destroy()
        back = ttk.Button(root, text="返回", command=self.homePage)
        back.pack(fill="x")
        self.num = StringVar()
        self.num.set(numOfQuestion)
        
        self.box = ttk.Combobox(root, values=list(range(3,11)),state="readonly",textvariable=self.num)
        self.box.pack()

        self.box.bind('<<ComboboxSelected>>', self.submit_num)

    def submit_num(self, event):
        global numOfQuestion
        numOfQuestion = int(self.num.get())

    def dataDisplay(self):
        
        root2 = Tk()
        root2.title("題庫")
        #back = ttk.Button(root2, text="返回", command=self.homePage)
        #back.pack(fill="x")

        
        scrollbar = Scrollbar(root2)
        scrollbar.pack( side = RIGHT, fill = Y )
        text = Text(root2, yscrollcommand=scrollbar.set)

        
        for i in range(len(db_part)):
                name = db_part[i].split()[0]
                text.insert(INSERT,name+"\n\n")
        scrollbar.config( command = text.yview )
        text.pack(fill="both",expand=1)
        text.config(state=DISABLED)
        root2.mainloop()
    
    def logPage(self):
        for i in self.master.winfo_children():
            i.destroy()
        back = ttk.Button(root, text="返回", command=self.homePage)
        back.pack(fill="x")
        
        l1 = ttk.Label(root, text="2023/08/19   著手開發第一版(純文字版)")
        l1.pack(anchor=W)
        l2 = ttk.Label(root, text="2023/08/23   嘗試轉換成第二版(GUI版)")
        l2.pack(anchor=W)
        l3 = ttk.Label(root, text="2023/09/04   第一版的功能大致重現完畢")
        l3.pack(anchor=W)
        l4 = ttk.Label(root, text="2023/09/10   新增其他功能及補完所有馬娘的資料")
        l4.pack(anchor=W)
        l4 = ttk.Label(root, text="2023/09/21   新增 凱斯奇蹟/ケイエスミラクル")
        l4.pack(anchor=W)
        l4 = ttk.Label(root, text="2023/10/27   新增 目白高峰/メジロラモーヌ")
        l4.pack(anchor=W)
        """f = open("log.txt","r",encoding="utf-8")
        log = f.readlines()
        f.close()
        for l in log:
            if l != "":
                part = l.split()
                update = part[0] + " 新增 " + part[1]
                if len(part) >= 3:
                    for i in range(2,len(part)):
                        update += (" 及 " + part[i])
                
                l1 = ttk.Label(root, text=update)
                l1.pack(anchor=W)"""
        

    def quit(self):
        root.destroy()

        

root = Tk()
app(root)
root.mainloop()