'''
Created on Oct 18, 2010

@author: dimitar
'''
from com.dim.task.Task import Task
from com.dim.task.TaskBuilder import TaskBuilder
import subprocess


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
            pass
            
if __name__ == '__main__':
    builder=TaskBuilder()
    task=builder.createTask("/home/main/python_worksapce/HomeBudjet/src/com/dim/app/resource/Task.xml", "RUN_EXTRACT_OPERATION1")
    TaskExecuter().executeTask(task)

    showTask=builder.createTask("/home/main/python_worksapce/HomeBudjet/src/com/dim/app/resource/Task.xml", "SHOW_IMAGE")