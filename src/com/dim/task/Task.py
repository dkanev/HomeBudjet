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
        
    def setName(self,taskName):
        self.taskName=taskName
     
    def getType(self):
        return self.taskType
    
    
    
    type = property(getType, doc='task type')

    
