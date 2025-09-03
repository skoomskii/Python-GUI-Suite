from aptDB import aptDB
from aptWX import aptWX
from tkinter import *
import tkinter as tk
import tkinter.scrolledtext as st

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.place()

        # Variables
        self.var0 = tk.StringVar()
        self.data = []
        self.wx = ''

        # Functions
        def getData(var):
            self.ent0.config(state='readonly')
            btn0.config(state='active')
            btn1.config(state='active')
            btn2.config(state='active')
            btn3.config(state='active')
            btn4.config(state='active')
            btn5.config(state='active')
            self.data = aptDB(0,var)
            self.wx = aptWX(var)
        
        def getInfo(txt):
            try:
                info = self.data[0]
                for i in range(0,len(info)):
                    txt.insert(tk.INSERT,info[i])
            except:
                txt.insert(tk.INSERT,'\n********** No Data **********')

        def getRwys(txt):
            try:
                rwys = self.data[1]
                for i in range(0,len(rwys)):
                    txt.insert(tk.INSERT,rwys[i][0])
            except:
                txt.insert(tk.INSERT,'\n********** No Data **********')

        def getFreq(txt):
            try:
                freq = self.data[2]
                for i in range(0,len(freq)):
                    txt.insert(tk.INSERT,freq[i][0])
            except:
                txt.insert(tk.INSERT,'\n********** No Data **********')
    
        def getNavs(txt):
            try:
                navs = self.data[3]
                for i in range(0,len(navs)):
                    txt.insert(tk.INSERT,navs[i][0])
            except:
                txt.insert(tk.INSERT,'\n********** No Data **********')

        def getWX(txt):
            txt.insert(tk.INSERT,self.wx)

        def Clear(txt):
            self.ent0.config(state='normal')
            btn0.config(state='disabled')
            btn1.config(state='disabled')
            btn2.config(state='disabled')
            btn3.config(state='disabled')
            btn4.config(state='disabled')
            btn5.config(state='disabled')
            self.data = aptDB(1,'')
            txt.delete('1.0',tk.END)

        # Widgets
            # Frames
        self.frm1= tk.Frame(master, bg="white", width=550, height=480, relief="raised", borderwidth=1)
            # Text Box
        self.txt1 = st.ScrolledText(self.frm1, bg="white", width=66, height=30, relief="raised", borderwidth=1)
            # Labels
        self.head = tk.Label(master, text="FlightBag", font=('Times',16,'bold'),bg="gray20")
        self.lbl0 = tk.Label(master, text='IDENT:', font=('Times',12,'bold'),bg="gray20")
            # Entries
        self.ent0 = tk.Entry(master,cursor='xterm',textvariable=self.var0,width=40,justify='center')
        self.ent0.insert(0,"--- ICAO ---")
        self.ent0.bind('<Return>',lambda event: getData(self.ent0.get()))
            # Buttons
        btn0= tk.Button(master, text="INFO", cursor='hand2', state='disabled', command=lambda: getInfo(self.txt1))
        btn1= tk.Button(master, text="RWYS", cursor='hand2', state='disabled', command=lambda: getRwys(self.txt1))
        btn2= tk.Button(master, text="FREQ", cursor='hand2', state='disabled', command=lambda: getFreq(self.txt1))
        btn3= tk.Button(master, text="NAVS", cursor='hand2', state='disabled', command=lambda: getNavs(self.txt1))
        btn4= tk.Button(master, text="METAR", cursor='hand2', state='disabled', command=lambda: getWX(self.txt1))
        btn5= tk.Button(master, text="CLEAR", cursor='hand2', state='disabled', command=lambda: Clear(self.txt1))

        # Placement
            # Frames
        self.frm1.place(x=80,y=70)
            # Text Boxes
        self.txt1.place(x=0,y=0)
            # Labels
        self.head.place(x=300,y=5)
        self.lbl0.place(x=180,y=31)
            # Entries
        self.ent0.place(x=240,y=35)
            # Buttons
        btn0.place(x=20,y=150)
        btn1.place(x=20,y=300)
        btn2.place(x=645,y=150)
        btn3.place(x=645,y=300)
        btn4.place(x=20,y=450)
        btn5.place(x=645,y=450)

# GUI Window
root = tk.Tk()
root.iconbitmap("icon.ico")
root.title('FlightBag')
root['bg'] = "gray20"
root.resizable(width=False, height=False)
root.geometry('700x600')
FlightBag = App(root)
FlightBag.mainloop()