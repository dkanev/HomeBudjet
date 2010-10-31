'''
Created on Oct 18, 2010

@author: dimitar
'''
import xml.dom.minidom, urllib,os,sys,io
from com.dim.task.Task import Task

class TaskBuilder(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def createTask(self,xmlConfigFile,taskName):
         
        if not os.path.exists(xmlConfigFile):
            return
        f = open(xmlConfigFile,'r')
        doc = xml.dom.minidom.parse(f)
        tasks = doc.getElementsByTagName('task')
        for sel in tasks:
            name=sel.getAttribute("name")
            if name==taskName:
                task=self._parsTask(sel)
                if not task==None:
                    task.setName(name)
                    print("Task name:"+name)
                    return task
        
        return None
    
    def _parsTask(self,taskXML):
        operations=taskXML.childNodes
        for operation in operations:
            if operation.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
                value=operation.tagName
                print(value)
                if value=="execute":
                    return self._parsExecuteXmlElement(operation)
                elif value=="showimage":
                    pass
                else:
                    raise TypeError("Incorrect task sub element: " + value)
                
    
    
                        
                    
                        
    def _parsExecuteXmlElement(self,executeXMLElment):
        argList=[]
        proccessName = executeXMLElment.getAttribute('process')
        print("Process name: " + proccessName)
        arguments = executeXMLElment.getElementsByTagName('arg')
        for arg in arguments:
            argument=self._parseArgument(arg)
            if argument != None:
                argList.append(argument)
        returnCode = executeXMLElment.getElementsByTagName('returnCode')[0]
        code="0"
        if returnCode != None:
            code=returnCode.getAttribute('value')
            print("Code:"+code)
        return Task('execute',proccessName,argList,code)
    
    def _parseArgument(self,xmlArgument):
        if xmlArgument.hasAttribute('name'):
            parameterName=xmlArgument.getAttribute('name')
            value=xmlArgument.getAttribute('value')
            print("Argument:"+parameterName + "=" + value)
            return parameterName + "=" + value
        elif xmlArgument.hasAttribute('value'):
            print("Argument:"+xmlArgument.getAttribute('value'))
            return xmlArgument.getAttribute('value')
        
        return None

if __name__ == '__main__':
    builder=TaskBuilder()
    task=builder.createTask("../app/resource/Task.xml", "RUN_EXTRACT_OPERATION")