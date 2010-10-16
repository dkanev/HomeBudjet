'''
Created on Oct 16, 2010

@author: dimitar
'''
from tkinter import *
from tkinter.filedialog import askopenfilename
def showResult():
    print("Test")



    
class App:
    
    textBox1=None
    
    def __init__(self, master):
        #master.geometry("300x200")
        fm = Frame(master)
        Label(fm, text="Host:").grid(row=0, sticky=W)
        Label(fm, text="Port:").grid(row=1, sticky=W)
        Label(fm, text="First file:").grid(row=2, sticky=W)
        Label(fm, text="Second file:").grid(row=3, sticky=W)
        Label(fm, text="Result file:").grid(row=4, sticky=W)
        Entry(fm).grid(row=0, column=1)
        Entry(fm).grid(row=1, column=1)
        self.textBox1 = Entry(fm)
        self.textBox1.grid(row=2, column=1)
        Button(fm, text='Browse',command=openfile).grid(row=2, column=3)
        
        self.textBox2=Entry(fm).grid(row=3, column=1)
        Button(fm, text='Browse',command=openfile).grid(row=3, column=3)
        self.textBox3=Entry(fm,state='disabled')
        self.textBox3.grid(row=4, column=1)
        frame=Frame(fm)
        Button(frame, text='Connect',command=showResult).pack(side=LEFT, fill=BOTH)
        Button(frame, text='Quit',command=master.quit).pack(side=LEFT, fill=BOTH)
        frame.grid(row=5, columnspan=2)
        fm.pack(fill=BOTH, expand=YES)
        
def openfile():
    file_name = askopenfilename()
    print(file_name)
    display.textBox1.insert(END, file_name)
        
root = Tk() 
#root.option_add('*font', ('verdana', 12, 'bold'))
root.title("Home Budget")
display = App(root)
root.mainloop()


