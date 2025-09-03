import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# GUI Window
root = Tk()
root.iconbitmap("icon.ico")
root.title('Checklist')
root.resizable(width=False, height=False)
root.geometry('500x400')

# Window Canvas
canvas = Canvas(root,bg='navajo white', width = 500,height = 400)

# Scrollbar
vbar = Scrollbar(canvas, orient = VERTICAL)
vbar.config(command = canvas.yview)
vbar.pack(side = RIGHT, fill = Y)
canvas.config(yscrollcommand=vbar.set)
canvas.pack(side=LEFT, expand = True, fill = BOTH)

# Variables
var= []
var0= StringVar()
var1= StringVar()
var2= StringVar()
var3= StringVar()
var4= StringVar()
var5= StringVar()
var6= StringVar()
var7= StringVar()
var8= StringVar()
var9= StringVar()
var10= StringVar()
var= [var0,var1,var2,var3,var4,var5,var6,var7,var8,var9,var10]
bol= []
bol0= BooleanVar()
bol1= BooleanVar()
bol2= BooleanVar()
bol3= BooleanVar()
bol4= BooleanVar()
bol5= BooleanVar()
bol6= BooleanVar()
bol7= BooleanVar()
bol8= BooleanVar()
bol9= BooleanVar()
bol= [bol0,bol1,bol2,bol3,bol4,bol5,bol6,bol7,bol8,bol9]
filepath= ''

# Functions
def Save(var,bol):
    try:
        global filepath
        fn= (var[0].get()).strip()
        done= bool(True)
        if (filepath.count(fn) > 0):
            with open(filepath, 'w', encoding='utf-8') as file:
                file.writelines(f"{fn}\n")
                for i in range(0,len(bol)):
                    done = done and bol[i].get()
                    file.writelines(f"{(var[i+1].get()).strip()}\n{str(bol[i].get()).strip()}\n")
                file.closed
                if (done):
                    canvas.config(bg="pale green")
                filepath= ''
            True
        else:
            with open(f'{fn}.txt', 'w', encoding='utf-8') as file:
                file.writelines(f"{fn}\n")
                for i in range(0,len(bol)):
                    done = done and bol[i].get()
                    file.writelines(f"{(var[i+1].get()).strip()}\n{str(bol[i].get()).strip()}\n")
                file.closed
                if (done):
                    canvas.config(bg="pale green")
                filepath= ''
            True
        btn3.config(state=DISABLED)
    except:
        print('Error!')

def Load():
    done= bool(True)
    global filepath
    canvas.config(bg="navajo white")
    filepath= filedialog.askopenfilename(
        initialdir='./',
        filetypes=(('Text Files','*.txt'),('All Files','*.*')),
        title='Select File'
    )
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = file.readlines()
            var[0].set(data[0])
            i= 1
            j= 1
            k= 0
            while (i <= len(data)-1):
                if (i%2 != 0):
                    var[j].set(data[i])
                    j += 1
                else:
                    if data[i].strip() == "True":
                        bol[k].set(bool(True))
                        done= done and bool(True)
                        k += 1
                    else:
                        bol[k].set(bool(False))
                        done= done and bool(False)
                        k += 1
                i += 1
            file.closed
            if (done):
                canvas.config(bg="pale green")
        True
        btn3.config(state=NORMAL,cursor='hand2')

def Delete():
    global filepath
    os.remove(filepath)
    btn3.config(state=DISABLED)

def Clear(var,bol):
    var[0].set('')
    for i in range(0,len(bol)):
        var[i+1].set('')
        bol[i].set('FALSE')
    btn3.config(state=DISABLED)

# Widgets
    # Labels
head= ttk.Label(canvas, text="Checklist", font=("Arial",16,"bold"))
lbl0= ttk.Label(canvas, text="1.", font=('', 12,"bold"))
lbl1= ttk.Label(canvas, text="2.", font=('', 12,"bold"))
lbl2= ttk.Label(canvas, text="3.", font=('', 12,"bold"))
lbl3= ttk.Label(canvas, text="4.", font=('', 12,"bold"))
lbl4= ttk.Label(canvas, text="5.", font=('', 12,"bold"))
lbl5= ttk.Label(canvas, text="6.", font=('', 12,"bold"))
lbl6= ttk.Label(canvas, text="7.", font=('', 12,"bold"))
lbl7= ttk.Label(canvas, text="8.", font=('', 12,"bold"))
lbl8= ttk.Label(canvas, text="9.", font=('', 12,"bold"))
lbl9= ttk.Label(canvas, text="10.", font=('', 12,"bold"))
    # Entries
ent0= Entry(canvas,cursor='xterm',textvariable=var[0],width=40,justify='center')
ent0.insert(0,'--- TITLE ---')
ent1= Entry(canvas,cursor='xterm',textvariable=var[1],width=70,justify='center')
ent1.insert(0,'--- TASK #1 ---')
ent2= Entry(canvas,cursor='xterm',textvariable=var[2],width=70,justify='center')
ent2.insert(0,'--- TASK #2 ---')
ent3= Entry(canvas,cursor='xterm',textvariable=var[3],width=70,justify='center')
ent3.insert(0,'--- TASK #3 ---')
ent4= Entry(canvas,cursor='xterm',textvariable=var[4],width=70,justify='center')
ent4.insert(0,'--- TASK #4 ---')
ent5= Entry(canvas,cursor='xterm',textvariable=var[5],width=70,justify='center')
ent5.insert(0,'--- TASK #5 ---')
ent6= Entry(canvas,cursor='xterm',textvariable=var[6],width=70,justify='center')
ent6.insert(0,'--- TASK #6 ---')
ent7= Entry(canvas,cursor='xterm',textvariable=var[7],width=70,justify='center')
ent7.insert(0,'--- TASK #7 ---')
ent8= Entry(canvas,cursor='xterm',textvariable=var[8],width=70,justify='center')
ent8.insert(0,'--- TASK #8 ---')
ent9= Entry(canvas,cursor='xterm',textvariable=var[9],width=70,justify='center')
ent9.insert(0,'--- TASK #9 ---')
ent10= Entry(canvas,cursor='xterm',textvariable=var[10],width=70,justify='center')
ent10.insert(0,'--- TASK #10 ---')
    # Buttons
chk0= ttk.Checkbutton(canvas,cursor='dotbox',variable=bol[0]) 
chk1= ttk.Checkbutton(canvas,cursor='dotbox',variable=bol[1])
chk2= ttk.Checkbutton(canvas,cursor='dotbox',variable=bol[2])
chk3= ttk.Checkbutton(canvas,cursor='dotbox',variable=bol[3])
chk4= ttk.Checkbutton(canvas,cursor='dotbox',variable=bol[4])
chk5= ttk.Checkbutton(canvas,cursor='dotbox',variable=bol[5])
chk6= ttk.Checkbutton(canvas,cursor='dotbox',variable=bol[6])
chk7= ttk.Checkbutton(canvas,cursor='dotbox',variable=bol[7])
chk8= ttk.Checkbutton(canvas,cursor='dotbox',variable=bol[8])
chk9= ttk.Checkbutton(canvas,cursor='dotbox',variable=bol[9])
btn0= ttk.Button(canvas, text="Load", cursor='exchange', command=lambda: Load())
btn1= ttk.Button(canvas, text="Save", cursor='hand2', command=lambda: Save(var,bol))
btn2= ttk.Button(canvas, text="Clear", cursor='hand2', command=lambda: Clear(var,bol))
btn3= ttk.Button(canvas, text="Delete", state=DISABLED, command=lambda: Delete())

# Placement
    # Labels
canvas.create_window(250,0,window=head)
canvas.create_window(20,100,window=lbl0)
canvas.create_window(20,150,window=lbl1)
canvas.create_window(20,200,window=lbl2)
canvas.create_window(20,250,window=lbl3)
canvas.create_window(20,300,window=lbl4)
canvas.create_window(20,350,window=lbl5)
canvas.create_window(20,400,window=lbl6)
canvas.create_window(20,450,window=lbl7)
canvas.create_window(20,500,window=lbl8)
canvas.create_window(20,550,window=lbl9)
    # Entries
canvas.create_window(250,30,window=ent0)
canvas.create_window(250,100,window=ent1)
canvas.create_window(250,150,window=ent2)
canvas.create_window(250,200,window=ent3)
canvas.create_window(250,250,window=ent4)
canvas.create_window(250,300,window=ent5)
canvas.create_window(250,350,window=ent6)
canvas.create_window(250,400,window=ent7)
canvas.create_window(250,450,window=ent8)
canvas.create_window(250,500,window=ent9)
canvas.create_window(250,550,window=ent10)
    # Buttons
canvas.create_window(480,100,window=chk0)
canvas.create_window(480,150,window=chk1)
canvas.create_window(480,200,window=chk2)
canvas.create_window(480,250,window=chk3)
canvas.create_window(480,300,window=chk4)
canvas.create_window(480,350,window=chk5)
canvas.create_window(480,400,window=chk6)
canvas.create_window(480,450,window=chk7)
canvas.create_window(480,500,window=chk8)
canvas.create_window(480,550,window=chk9)
canvas.create_window(45,600,window=btn0)
canvas.create_window(180,600,window=btn1)
canvas.create_window(320,600,window=btn2)
canvas.create_window(450,600,window=btn3)

canvas.configure(scrollregio=canvas.bbox("all"))

root.mainloop()