#coding=utf-8
import sys
import os
import mainWindow
import mainEngine
from PyQt4 import QtCore, QtGui

#var settings things
UISet=[]
EngineSet=[]


def setting():
	UISet.append('grid'+'='+str(mainEngine.gridN))
	UISet.append('gridx'+'='+str(mainEngine.xd))
	UISet.append('gridy'+'='+str(mainEngine.yd))
	for i in range(10):
                EngineSet.append('gridy'+'='+str(mainEngine.yd))
                

	#create settings file
	if os.path.isdir("._settings")==False:
		os.mkdir("._settings") 
	#open settings file
	UISetF = open('._settings\.UISet'+'.fengx', 'w')
	EngineSetF=open('._settings\.EngineSet'+'.fengx', 'w')
	print(str(os.stat('._settings\.EngineSet.fengx')))
	
	for element1 in UISet:
		UISetF.write("搞点中文试试"+str(element1)+"\n")
		#UISetF.close()
	
	for element2 in EngineSet:
		EngineSetF.write("搞点中文试试"+str(element2)+"\n")
		#EngineSetF.close()
