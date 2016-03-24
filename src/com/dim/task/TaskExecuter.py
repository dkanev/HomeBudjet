'''
Created on Oct 18, 2010

@author: lele
'''
from com.dim.task.Task import Task
from com.dim.task.TaskBuilder import TaskBuilder
import subprocess
from tkinter import *

class TaskExecuter(object):

    def executeTask(self,task):

            
        if task.taskType == "execute":
            output = None
            errOutput = None
            if task.hasOutputFile() :
                output = open(task.getOutputFile(), 'w')
            if task.hasErrortFile() :
                errOutput = open(task.getErrortFile(), 'w')


            print(task.taskType)
            process = subprocess.Popen(task.command + " " + task.args, shell=True,stdout=output,stderr=errOutput)
            while True:
                process.poll()
                if process.returncode !=None:
                    break
            
            if task.code!=None and len(task.code)>0:
                if  int(task.code)==process.returncode:
                    print('Success. Return code: {0}'.format(process.returncode))
                else:
                    print("Error. Return code: {0}".format(process.returncode))
            else:
                print("Success")


        elif task.taskType=="showimage":
            root = Tk() 
            root.title(task.caption)
            fm = Frame(root)
            gif = PhotoImage(file=task.img)
            Label(fm,image=gif).grid(row=0, sticky=W)
            Label(fm, text=task.description).grid(row=1, sticky=W)
            fm.pack(fill=BOTH, expand=YES)
            root.mainloop()
        
            
if __name__ == '__main__':
    builder=TaskBuilder()
    task=builder.createTask("/home/main/python_worksapce/HomeBudjet/src/com/dim/app/resource/Task.xml", "RUN_EXTRACT_OPERATION1")
    TaskExecuter().executeTask(task)

    showTask=builder.createTask("/home/main/python_worksapce/HomeBudjet/src/com/dim/app/resource/Task.xml", "SHOW_IMAGE")
    TaskExecuter().executeTask(showTask)