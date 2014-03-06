'''
#----------main window --------------#
#----------created by fengx----------#
'''
#coding=utf-8
import sys
import os
from PyQt4 import QtCore, QtGui
import mainEngine
import settings
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        #------------------------------------------
        super(MainWindow, self).__init__()
        centralWidget = QtGui.QWidget()
        self.setCentralWidget(centralWidget)
        # gui
        self.frontSize=10
        #-------------------------------------------------------main scene
        # place some public variable
        # load some map
        mainBG = QtGui.QPixmap(self)
        mainBG.load('UI/M_mainBG.png')
        menuOn = True
        settings.setting()
        # initialize widget
        #---main windows
        self.mainWidget = mainEngine.GLWidget()
        self.toolWidget = QtGui.QWidget()
        def contextMenuEvent(self, event):          
            self.file.exec_(event.globalPos())

        #---menu
        if menuOn == True:
                self.createActions()
                self.createMenus()

        # tool view  Area
        self.toolArea = QtGui.QScrollArea()
        self.toolArea.setWidget(self.toolWidget)
        self.toolArea.setWidgetResizable(True)
        #self.toolArea.setMinimumSize(20,50)
        #self.toolArea.setMaximumSize(20, 900)

        # part of tool view
        label2 = QtGui.QLabel('xxx', self)
        label2.setAlignment(QtCore.Qt.AlignCenter)
        label3 = QtGui.QLabel('xxx', self)
        label3.setAlignment(QtCore.Qt.AlignCenter)
        label5 = QtGui.QLabel('xxx', self)
        label5.setAlignment(QtCore.Qt.AlignCenter)
        label6 = QtGui.QLabel('', self)
        label6.setAlignment(QtCore.Qt.AlignCenter)

        text1 = QtGui.QLineEdit('xxx')
        text2 = QtGui.QLineEdit('xxx')
        #file_obj = open("visual_fengx_information.txt")
        #file_obj_content = file_obj.read()
        #text3 = QtGui.QTextEdit(file_obj_content)

        # windows style change
        self.styleComboBox = QtGui.QComboBox()
        self.styleComboBox.addItems(QtGui.QStyleFactory.keys())
        self.styleLabel = QtGui.QLabel("&Style:")
        self.styleLabel.setBuddy(self.styleComboBox)
        #dock
        '''
        #dock1.setFeatures(QDockWidget.AllDockWidgetFeatures)
            # dock1.setFeatures(QDockWidget.DockWidgetMovable)
            # dock1.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        #self.addDockWidget(Qt.RightDockWidgetArea, dock1)
        '''
        # tool view layout
        self.toolLayout = QtGui.QGridLayout()
        self.toolLayout.addWidget(label5, 1, 0, 1, 1)
        self.toolLayout.addWidget(label2, 2, 0, 1, 1)
        self.toolLayout.addWidget(label3, 3, 0, 1, 1)
        self.toolLayout.addWidget(text1, 2, 1, 1, 1)
        self.toolLayout.addWidget(text2, 3, 1, 1, 1)
        #self.toolLayout.addWidget(text3, 6, 0, 1, 2)
        self.toolLayout.addWidget(self.styleComboBox, 1, 1, 1, 1)
        self.toolLayout.addWidget(label6, 5, 1, 1, 2)

        # main  scene windows
        self.glWidgetArea = QtGui.QScrollArea()
        self.glWidgetArea.setWidget(self.mainWidget)
        self.glWidgetArea.setWidgetResizable(True)
        self.glWidgetArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.glWidgetArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.glWidgetArea.setMinimumSize(150, 150)
        self.glWidgetArea.setMaximumSize(1440, 900)
        self.setWindowIcon(QtGui.QIcon('UI/icons/Spell_Shadow_DeathCoil.png'))
        
        #-------------------------------------------------------toolbar
        # def toolbar1(self):
        self.test1 = QtGui.QAction(QtGui.QIcon('UI/icons/Spell_Shadow_DeathCoil.png'), 'xxx', self)
        self.frame = QtGui.QAction(QtGui.QIcon('UI/icons/1 (1)'), 'frame all', self)
        self.test2 = QtGui.QAction(QtGui.QIcon('UI/icons/1 (2)'), 'frame all', self)
        self.test3 = QtGui.QAction(QtGui.QIcon('UI/icons/1 (3)'), 'frame all', self)
        self.test4 = QtGui.QAction(QtGui.QIcon('UI/icons/1 (4)'), 'frame all', self)
        
        self.exit = QtGui.QAction(QtGui.QIcon('UI/icons/Spell_Shadow_DeathCoil.png'), 'Exit', self)
        self.exit.setShortcut('Ctrl+Q')
        
        self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))   
        #self.connect(self.frame, QtCore.SIGNAL('triggered()'), QtCore.SLOT('self.frame))      
        self.toolbar = self.addToolBar('MainToolBar')
        self.toolbar.setIconSize(QtCore.QSize(40, 40))
        self.toolbar.addAction(self.frame)
        self.toolbar.addAction(self.exit)
        self.toolbar.addAction(self.test1)
        self.toolbar.addAction(self.test2)
        self.toolbar.addAction(self.test3)
        self.toolbar.addAction(self.test4)
        
        self.toolbar.setFloatable(False)
        self.toolbar.setOrientation(0x1)
        self.toolbar.setToolButtonStyle(4)

        #-------------------------------------------------------main layout
        mainLayout = QtGui.QGridLayout()
        mainLayout.addLayout(self.toolLayout, 1, 3, 3, 3)
        mainLayout.addWidget(self.glWidgetArea, 1, 0, 3, 1)
        centralWidget.setLayout(mainLayout)
        self.setWindowTitle("VisualFeng_1.0")
        self.setGeometry(100, 100, 900, 600)
        
        #style change combobox
        self.styleComboBox.activated[str].connect(self.changeStyle)

        #----------main window background
        self.palette1 = QtGui.QPalette(self)
        self.palette1.setBrush(self.backgroundRole(), QtGui.QBrush(mainBG))
        self.setPalette(self.palette1)
        self.setAutoFillBackground(0)
        
    def changeStyle(self, styleName):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(styleName))
        QtGui.QApplication.setPalette(QtGui.QApplication.style().standardPalette())
        # QtGui.QApplication.setPalette(self.originalPalette)

    def about(self):
        QtGui.QMessageBox.about(
            self, "about this", "--------VisualFeng 1.0-------- \n-An engine for visual things. - \n--------Creat by Fengx--------")

    def flieImport(self):
        QtGui.QFileDialog.getOpenFileNames(
            self, "Select OBJ Files", QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.DesktopLocation))

    def newWindow(self):
        QtGui.QMessageBox.warning(self, 'VisualFeng 1.0', 'Warning! not complite', QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
            
    def preference(self):
        QtGui.QMessageBox.warning(self, 'VisualFeng 1.0', 'Warning! not complite', QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        print('loading')
    def save(self):
        if os.path.isdir("onlyTest")==False:
            os.mkdir("onlyTest") 
        f = open('onlyTest\settings.fengx', 'w')
        f.write('d')
        f.close() 
    def frame(self):
        self.mainWidget.xT = 0
        self.mainWidget.yT = 0
        self.mainWidget.zT = -5
        self.mainWidget.zRot=0
        self.mainWidget.yRot=0
        self.mainWidget.xRot=0
        self.mainWidget.updateGL()
    def createActions(self):
        self.newWindows = QtGui.QAction("&New Window", self, shortcut="Ctrl+n", triggered=self.newWindow)
        self.frame = QtGui.QAction("&Reset view", self, shortcut="f", triggered=self.frame)
        self.Import = QtGui.QAction("&Import", self, shortcut="Ctrl+i", triggered=self.flieImport)
        self.exitAct = QtGui.QAction("&Exit", self, shortcut="Ctrl+Q", triggered=self.close)
        self.aboutAct = QtGui.QAction("&About", self, triggered=self.about)
        self.preference = QtGui.QAction("&Preference", self, shortcut="Ctrl+k", triggered=self.preference)
        # self.option=QtGui.QAction("&Options",self,shortcut="Alt+,",triggered=self.option)

    #---------------------------------------------------------------------------main menu
    def createMenus(self):
        self.fengxMenu = self.menuBar().addMenu("&Flie")
        self.fengxMenu.addSeparator()
        self.fengxMenu.addAction(self.Import)
        self.fengxMenu.addSeparator()
        self.fengxMenu.addAction(self.exitAct)

        self.viewMenu = self.menuBar().addMenu("&View")
        self.viewMenu.addAction(self.frame)
        self.viewMenu.addAction(self.newWindows)
        self.optionMenu = self.menuBar().addMenu("&Window")
        self.optionMenu.addAction(self.preference)
        self.helpMenu = self.menuBar().addMenu("&About")
        self.fengxMenu.addSeparator()
        self.helpMenu.addAction(self.aboutAct)
    #---------------------------------------------------------------------------main controller by keyboard

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_W:
            self.mainWidget.zT = self.mainWidget.zT + 0.2
            self.mainWidget.updateGL()
        if event.key() == QtCore.Qt.Key_S:
            self.mainWidget.zT = self.mainWidget.zT - 0.2
            self.mainWidget.updateGL()
        if event.key() == QtCore.Qt.Key_A:
            self.mainWidget.xT = self.mainWidget.xT + 0.012
            self.mainWidget.updateGL()
        if event.key() == QtCore.Qt.Key_D:
            self.mainWidget.xT = self.mainWidget.xT - 0.012
            self.mainWidget.updateGL()
        if event.key() == QtCore.Qt.Key_Q:
            self.mainWidget.yT = self.mainWidget.yT + 0.012
            self.mainWidget.updateGL()
        if event.key() == QtCore.Qt.Key_E:
            self.mainWidget.yT = self.mainWidget.yT - 0.012
            self.mainWidget.updateGL()
        if event.key() == QtCore.Qt.Key_F:
            self.mainWidget.xT = 0
            self.mainWidget.yT = 0
            self.mainWidget.zT = -5
            self.mainWidget.zRot=0
            self.mainWidget.yRot=0
            self.mainWidget.xRot=0
            self.mainWidget.updateGL()
     
if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    app.setFont(QtGui.QFont("Microsoft YaHei UI", 9))
    mainWin = MainWindow()
    mainWin.show()
    font  = app .font();
    font.setPointSize(mainWin.frontSize);
    app.setFont(font);
    sys.exit(app.exec_())
