'''
Created on Oct 18, 2010

@author: dimitar
'''
from com.dim.task.Task import Task
from com.dim.task.TaskBuilder import TaskBuilder
import subprocess

class TaskExecuter(object):
    x=10 
    def executeTask(self,task): 
        fsock = open('../app/resource/out.log', 'w')
        if task.taskType=="execute":
            print(task.taskType)
            process = subprocess.Popen(task.command + " " + task.args, shell=True,stdout=fsock)
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
    pass
#    print(str(TaskExecuter.x))
    builder=TaskBuilder()
    task=builder.createTask("../app/resource/Task.xml", "RUN_EXTRACT_OPERATION")
    TaskExecuter().executeTask(task)
#    print(str(TaskExecuter.x)+ " ")
#    rexec=TaskExecuter()
#    print(str(rexec.x)+ " ")
#    print(str(TaskExecuter.x)+ " ")
#    rexec.x=22
#    print(str(rexec.x)+ " ")
#    rexec.executeTask(task)
#    print(str(rexec.x)+ " ")
#    print(str(TaskExecuter.x)+ " ")