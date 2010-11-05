'''
Created on Oct 16, 2010

@author: dimitar
'''
from tkinter import *
from tkinter.filedialog import askopenfilename
import os
from com.dim.tool.Merge import Merge
    

class App(object):
    
    def getNewFileName(self,dir,namePattern,fileExtension):
        fileNames=os.listdir(dir);
        checkFileName=namePattern + "." + fileExtension
        i=1
        notFound=False
        while 1:
            for fileName in fileNames:
                if checkFileName==fileName:
                    checkFileName=namePattern + str(i) + "." + fileExtension
                    i=i+1
                    notFound=True
                    break
                
            if not notFound:
                return dir + "/" + checkFileName
            else:
                notFound=False
        
    
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
        self.textBox2 = Entry(fm)
        self.textBox2.grid(row=3, column=1)
        Button(fm, text='Browse',command=(lambda : self.textBox1.delete(0, END) or self.textBox1.insert(0, askopenfilename())) ).grid(row=2, column=3)
        Button(fm, text='Browse',command=(lambda : self.textBox2.delete(0, END) or self.textBox2.insert(END, askopenfilename())) ).grid(row=3, column=3)
        self.saveLabel=Label(fm,text="")
        self.saveLabel.grid(row=4, column=1,sticky=W)
        frame=Frame(fm)
        Button(frame, text='Merge',command=self.mergeFile).pack(side=LEFT, fill=BOTH)
        Button(frame, text='Quit',command=master.quit).pack(side=LEFT, fill=BOTH)
        frame.grid(row=5, columnspan=2)
        fm.pack(fill=BOTH, expand=YES)
        print("test")

    def mergeFile(self):
        newFile=self.getNewFileName("./resource", "Merge", "xml")
        mergeTool=Merge(self.textBox1.get(),self.textBox2.get())
        mergeTool.mergePredecesorXMLFile(newFile)
        self.saveLabel.config(text=newFile) 
        
             
if __name__ == '__main__':
    root = Tk() 
    #root.option_add('*font', ('verdana', 12, 'bold'))
    root.title("Home Budget")
    saveFile=""
    if not os.path.exists("./resource"):
        os.makedirs("./resource")

    
    display = App(root)
    root.mainloop()


