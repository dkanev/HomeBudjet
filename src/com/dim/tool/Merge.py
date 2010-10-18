'''
Created on Oct 18, 2010

@author: dimitar
'''

import xml.dom.minidom, urllib,os,sys,io


class Merge:
    
    def _parsePredecesorXMLFile(self,path):
    
        if not os.path.exists(path):
            return
    
        item=[]
        map={}
        f = open(path,'r')
        doc = xml.dom.minidom.parse(f)
        elements = doc.getElementsByTagName('StringArray')
    
        for el in elements:
            stValuesNodes=el.getElementsByTagName('StringValue')
            item=[]
            for stValuesNodesEL in stValuesNodes:
                for inerEl in stValuesNodesEL.childNodes:
                    if stValuesNodesEL.firstChild.nodeType == inerEl.TEXT_NODE:
                        print('Node value' + stValuesNodesEL.firstChild.nodeValue)
                        item.append(stValuesNodesEL.firstChild.nodeValue)
    
            if not len(item) ==4 :
                raise(TypeError("Item do not have to elements"))
            print('Add element ' + item[0] + '@' + item[2]) 
            map[item[0] + '@' + item[2]]=item
        return map 
        
    def __init__(self, firstFile,secondFile):
        self.firstFile=firstFile
        self.secondFile=secondFile
    
    def mergePredecesorXMLFile(self,newFile):

        map1=self._parsePredecesorXMLFile(self.firstFile)
        map2=self._parsePredecesorXMLFile(self.secondFile)
        
        for key in map1:
            if key in map2:
                del map2[key] 
        
                       
        file = open(newFile, "w")
        file.write('<?xml version="1.0"?>\n')
        file.write('<VariableHandler name="ComponentPredecessors">\n')
        file.write('<StringTable name="APPL_PACK_PRED_LIST">\n')
        file.write('    <TableDefinition NumberKeyColumns="4" NumberColumns="4">\n')
        file.write('      <ColumnName>APPLICATION_PACKAGE</ColumnName>\n')
        file.write('      <ColumnName>VENDOR</ColumnName>\n')
        file.write('      <ColumnName>PRED_APPLICATION_PACKAGE</ColumnName>\n')
        file.write('      <ColumnName>PRED_VENDOR</ColumnName>\n')
        file.write('    </TableDefinition>\n')
        lines=self._loadFile(self.firstFile)
        self._saveXMLFile(file,map1,lines,'StringArray', 'StringValue','<!-- configurations from nw730 _er_630 -->')
        lines=self._loadFile(self.secondFile)
        self._saveXMLFile(file,map2,lines,'StringArray', 'StringValue','<!-- configurations from switch _er_630 -->')
    
        file.write('\n\n     </StringTable>\n')
        file.write('</VariableHandler>')
        file.close()
            
    def _loadFile(self,path):
        input = open(path)
        lines=[]
        if not isinstance(input,io.TextIOBase):
                raise(TypeError('Incorrect input parameter'))
        line=""
        lineNumber=0;
        while 1:
            line = input.readline()       # read line by line
            if not line: break
            lines.append(line)
                
    
        commentStart=False
        stringArray=False
        newComment=False
        commentText=''
        newlines=[]
        xmlElement=''
        for line in lines:
            if len(line)==0 and not commentStart :
                newlines.append(line)
                continue
    
            line = line.rstrip('\n').rstrip('\r').strip()
            
            if line.startswith('<!--'):
                commentStart=True
                commentText=''
               
            if commentStart and line.endswith('-->'):
                commentText= commentText + ' ' + line
                commentStart=False
                newlines.append(commentText)
                continue
            
            if commentStart : 
                commentText= commentText + ' ' + line
                continue
            
            if line.startswith('<StringArray>'):
                stringArray=True
            
            if line.endswith('</StringArray>'):
                xmlElement = xmlElement + line
                valuList=self._parsXmlElement(xmlElement)
                stringArray=False
                xmlElement=''
                newlines.append(valuList)
                continue
                
            if stringArray:
                xmlElement = xmlElement + line
            
        return newlines

    def _parsXmlElement(self,xmlElement):
    
        item=[]
        map={}
        doc = xml.dom.minidom.parseString(xmlElement)
        elements = doc.getElementsByTagName('StringArray')
    
        for el in elements:
            stValuesNodes=el.getElementsByTagName('StringValue')
            item=[]
            for stValuesNodesEL in stValuesNodes:
                for inerEl in stValuesNodesEL.childNodes:
                    if stValuesNodesEL.firstChild.nodeType == inerEl.TEXT_NODE:
                        print('Node value' + stValuesNodesEL.firstChild.nodeValue)
                        item.append(stValuesNodesEL.firstChild.nodeValue)
    
            if not len(item) ==4 :
                raise(TypeError("Item do not have to elements"))
            print('Add element ' + item[0] + '@' + item[2]) 
            map[item[0] + '@' + item[2]]=item
        return map


    def _saveXMLFile(self,file,map,lines,rootElement, subElement,comment):
       
    
        if len(map)==0:
            return
        
        file.write(comment+ '\n\n')
        
        for line in lines:
            if not  isinstance(line, dict):
                file.write(line +"\n")
                continue
            for key in line:
                if key in map:
                    file.write('<'+ rootElement +'>\n')
                    item=map[key]
                    for value in item:
                        file.write('   <'+ subElement +'>')
                        file.write(value)
                        file.write('</'+ subElement +'>\n')
                    file.write('</'+ rootElement +'>\n')

        