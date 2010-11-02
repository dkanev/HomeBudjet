'''
Created on Oct 18, 2010

@author: dimitar
'''
import xml.dom.minidom,os
from com.dim.task.Task import Task
from com.dim.task.ExecuteProcessTask import ExecuteProcessTask
from com.dim.task.ShowImageTask import ShowImageTask

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
                     return self._parsShowImageXmlElement(operation)
                else:
                    raise TypeError("Incorrect task sub element: " + value)
                
    
    
                        
                    
                        
    def _parsExecuteXmlElement(self,executeXMLElment):
        argList=[]
        proccessName = executeXMLElment.getAttribute('process')
        stdOut = executeXMLElment.getAttribute('stdOut')
        stdError = executeXMLElment.getAttribute('stdErr')
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
        
        task =ExecuteProcessTask('execute',proccessName,argList,code)
        task.setOutputFile(stdOut)
        task.setErrorFile(stdError)    
        return task
    
    def _parsShowImageXmlElement(self,executeXMLElment):
        argList=[]
        imgSrc = executeXMLElment.getAttribute('src')
        altStr = executeXMLElment.getAttribute('alt')

        print("Img src: " + imgSrc)
        caption = self._getXMLContent(executeXMLElment.getElementsByTagName('caption')[0])
        description = self._getXMLContent(executeXMLElment.getElementsByTagName('description')[0])
        
                
        print("caption: " + caption)
        print("description: " + description)
        task =ShowImageTask('showimage',imgSrc,altStr,caption,description)
 
        return task
    
    
    def _getXMLContent(self,xmlElement):
        nodes=xmlElement.childNodes
        for node in nodes:
            if node.nodeType == xml.dom.minidom.Node.TEXT_NODE:
                return node.data
                 
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
   pass