'''
Created on Oct 18, 2010

@author: dimitar
'''
import xml.dom.minidom, urllib,os,sys,io

class TaskBuilder(object):
    '''
    classdocs
    '''


    def __init__(self,configFile):
        '''
        Constructor
        '''
    def createTask(self,xmlConfigFile,taskName):
         
        if not os.path.exists(xmlConfigFile):
            return
    
        item=[]
        map={}
        f = open(xmlConfigFile,'r')
        doc = xml.dom.minidom.parse(f)
        elements = doc.getElementsByTagName('StringArray')
    
