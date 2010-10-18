'''
Created on Oct 18, 2010

@author: dimitar
'''

class Task(object):
    '''
    classdocs
    '''


    def __init__(self,taskType,processName,argList,returnCode):
        '''
        Constructor
        '''
        self.taskType=taskType
        self.processName=processName
        self.argList=argList
        self.returnCode=returnCode
    
    def setName(self,taskName):
        self.taskName=taskName