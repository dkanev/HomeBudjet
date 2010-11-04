'''
Created on Nov 3, 2010

@author: main
'''
from com.dim.task.Task import Task


class ShowImageTask(Task):

    def __init__(self,taskType,imageSrc,altStr,caption,description):
        '''
        Constructor
        '''
        self.taskType=taskType
        self.imgSrc=imageSrc
        self.altStr=altStr
        self._caption=caption
        self._description=description
    
    def getCaption(self):
        return self._caption
    
    def getIMG(self):
        return self.imgSrc
    
    def getDescription(self):
        return self._description
    
    caption = property(getCaption, doc='arguments of the command')
    img = property(getIMG, doc='expected return code after command execution ')
    description = property(getDescription, doc='expected return code after command execution ')

if __name__ == "__main__":
    pass