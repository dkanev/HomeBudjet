'''
Created on Nov 3, 2010

@author: main
'''
from com.dim.task.Task import Task


class ShowImageTask(Task):

    def __init__(self,taskType,imageSrc,altStr,caption,destion):
        '''
        Constructor
        '''
        self.taskType=taskType
        self.imgSrc=imageSrc
        self.altStr=altStr
        self.caption=caption
        self.destion=destion


if __name__ == "__main__":
    pass