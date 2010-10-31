'''
Created on Oct 18, 2010

@author: dimitar
'''

class Task(object):
    '''
    classdocs
    '''

    errorFile=None
    outFile=None
    def __init__(self,taskType,processName,argList,returnCode):
        '''
        Constructor
        '''
        self.taskType=taskType
        self.processName=processName
        self.argList=argList
        self.returnCode=returnCode
    
    def setOutputFile(self,outFile):
        self.outFile=outFile
        
    def setErrorFile(self,errorFile):
        self.errorFile=errorFile
    
    def hasOutputFile(self):
        if self.outFile != None and len(self.outFile)>0: return True
        else: return False
        
    def hasErrortFile(self):
        if self.errorFile != None and len(self.outFile)>0: return True
        else: return False
    
    def getOutputFile(self):
        return self.outFile
        
    def getErrortFile(self):
        return self.errorFile
        
        
    def setName(self,taskName):
        self.taskName=taskName
     
    def getType(self):
        return self.taskType
    
    def getCommand(self):
        return self.processName
    
    def getArgs(self):
        args=""
        for arg in self.argList:
            args=args + " " + arg
        return args
    
    def getCode(self):
        return self.returnCode
    
    
    type = property(getType, doc='task type')
    command = property(getCommand, doc='command which to be executed')
    args = property(getArgs, doc='arguments of the command')
    code = property(getCode, doc='expected return code after command execution ')
    
