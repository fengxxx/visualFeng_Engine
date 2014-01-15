#!/usr/bin/env python
from PyQt4 import QtCore, QtGui, QtOpenGL
import sys
import settings
import mainWindow

# import math
xd = 0.24
yd = 0.008
gridN = 60

try:
    from OpenGL import GL
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "OpenGL hellogl",
                               "PyOpenGL must be installed to run this example.")
    sys.exit(1)

#print(str(mainWindow.settings.UISetF[0]))

class GLWidget(QtOpenGL.QGLWidget):

    xRotationChanged = QtCore.pyqtSignal(int)
    yRotationChanged = QtCore.pyqtSignal(int)
    zRotationChanged = QtCore.pyqtSignal(int)
    coords = (
        ( ( +1, -1, -1 ), ( -1, -1, -1 ), ( -1, +1, -1 ), ( +1, +1, -1 ) ),
        ( ( +1, +1, -1 ), ( -1, +1, -1 ), ( -1, +1, +1 ), ( +1, +1, +1 ) ),
        ( ( +1, -1, +1 ), ( +1, -1, -1 ), ( +1, +1, -1 ), ( +1, +1, +1 ) ),
        ( ( -1, -1, -1 ), ( -1, -1, +1 ), ( -1, +1, +1 ), ( -1, +1, -1 ) ),
        ( ( +1, -1, +1 ), ( -1, -1, +1 ), ( -1, -1, -1 ), ( +1, -1, -1 ) ),
        ( ( -1, -1, +1 ), ( +1, -1, +1 ), ( +1, +1, +1 ), ( -1, +1, +1 ) )
    )
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)

        self.object = 0
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        self.xT = 0
        self.yT = 0
        self.zT = -5
        self.vT = 0.1
        self.lastPos = QtCore.QPoint()

        self.trolltechGreen = QtGui.QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QtGui.QColor.fromCmykF(0.5, 0.5, 0.5, 0.18)
        self.myColor1 = QtGui.QColor.fromCmykF(0.1, 0.3, 0.2, 0.18)
        self.myColor2 = QtGui.QColor.fromCmykF(0.4, 0.3, 0.5, 0.4)
        self.myColor3 = QtGui.QColor.fromCmykF(0.3, 0.3, 0.6, 0.4)
        self.myColor4 = QtGui.QColor.fromCmykF(0, 0, 0, 0)

        self.backgrundColor = QtGui.QColor.fromCmykF(0, 0, 0, 0.85)

        # grid color
        self.red= QtGui.QColor.fromCmykF(0, 1, 1, 0)
        self.blue = QtGui.QColor.fromCmykF(1,0, 0, 0)
        self.green = QtGui.QColor.fromCmykF(1, 0, 1, 0)
        self.yellow = QtGui.QColor.fromCmykF(0,0, 1, 0)
        self.black = QtGui.QColor.fromCmykF(1, 1, 1, 1)
        self.gridColor3 = QtGui.QColor.fromCmykF(0.5, 0.5, 0.5, 0.18)
        self.gridColor2 = QtGui.QColor.fromCmykF(0.0, 0.9, 0.9, 0.1)

    def minimumSizeHint(self):
        return QtCore.QSize(50, 50)

    def sizeHint(self):
        return QtCore.QSize(900, 600)

    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = angle
            self.xRotationChanged.emit(angle)
            self.updateGL()

    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
            self.yRotationChanged.emit(angle)
            self.updateGL()

    def setZRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.zRot:
            self.zRot = angle
            self.zRotationChanged.emit(angle)
            self.updateGL()
    '''
    def initializeGL(self):
        self.qglClearColor(self.backgrundColor)
        self.object = self.makeObject()
        GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_CULL_FACE)
        GL.glEnable(GL.GL_TEXTURE_2D)
    '''
    def initializeGL(self):
        self.qglClearColor(self.backgrundColor)
        self.object = self.makeObject()
        #if not GLWidget.sharedObject:
            #GLWidget.sharedObject = self.makeObject()
        #GLWidget.refCount += 1

        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_CULL_FACE)
        GL.glEnable(GL.GL_TEXTURE_2D)
        
    def paintGL(self):
        
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glLoadIdentity()
        
        GL.glTranslated(self.xT, self.yT, self.zT)

        GL.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        GL.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        GL.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)
        GL.glCallList(self.object)

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0:
            return

        GL.glViewport((width - side) / 2, (height - side) / 2, side, side)

        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glFrustum(-0.15, +0.15, +0.15, -0.15, 1, 90.0)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        #lastPos.y())

        #if  QtCore.Qt.RightButton | QtCore.Qt.Key_Alt:

        #    self.setXRotation(self.xRot + 8 * )
        #    self.setYRotation(self.yRot + 8 * dx)
        #self.lastPos = event.pos()
    def mousePressEvent(self, event):
        self.lastPos = event.pos()

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & QtCore.Qt.LeftButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setYRotation(self.yRot + 8 * dx)
        elif event.buttons() & QtCore.Qt.RightButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setZRotation(self.zRot + 8 * dx)

        self.lastPos = event.pos()
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_B:
            print"BBBB"

    def makeObject(self):
        genList = GL.glGenLists(1)
        GL.glNewList(genList, GL.GL_COMPILE)
        

        #self.point(0, 1, 2,6)
        #self.cube(0.5,0.5,0.5,0.4,0.4,0.4)
        #self.qglColor(self.trolltechPurple)
        for i in range(6):
            self.bindTexture(QtGui.QPixmap(':/images/side%d.png' % (i + 1)))
            GL.glBegin(GL.GL_QUADS)
            for j in range(4):
                tx = {False: 0, True: 1}[j == 0 or j == 3]
                ty = {False: 0, True: 1}[j == 0 or j == 1]
                GL.glTexCoord2d(tx, ty)
                GL.glVertex3d(0.2 * GLWidget.coords[i][j][0],0.2 * GLWidget.coords[i][j][1],0.2 * GLWidget.coords[i][j][2])

            GL.glEnd()
        '''
        self.square(0,0,0,0.1)
        #GL.glRotatef()
        for iu in range(10):
            for iw in range(10):
                self.square(iu*0.1, iw*0.1, 0, 0.1)
        # GL.glBegin(GL.GL_QUAD_STRIP)
        # GL.glBegin(GL.GL_TRIANGLE_STRIP)
        GL.glTranslatef(0,0,0.3)
        '''
        GL.glBegin(GL.GL_LINES)
        self.xyz()
        
        self.grid()
        #self.gridCube()
        GL.glEnd()
        GL.glTranslatef(0,3,0.3)
        GL.glEndList()
        return genList
    def point(self,x,y,z,s):
        self.qglColor(self.red)
        GL.glBegin(GL.GL_QUAD_STRIP)
        for i in range(s):
            for ii in range(s):
                #GL.glVertex2d(0+x+0.01*i,0+0.01*ii+y)
                #GL.glVertex2d(0.01+0.01*i+x,0.01+0.01*ii+y)
                GL.glVertex2f(0.1,0.1)
                GL.glVertex2f(0.1,0.11)
                GL.glVertex2f(0.15,0.1)
                GL.glVertex2f(0.19,0.11)
        GL.glEnd()
    def cube(self, x, y, z, l, w, h):
        #face
        '''
        ca=(0,0,0)
        cb=(l,0,0)
        cc=(l,w,0)
        cd=(0,w,0)
        ce=(0,0,h)
        cf=(l,0,h)
        cg=(l,w,h)
        ch=(0,w,h)
        '''
        self.qglColor(self.trolltechPurple)
        GL.glBegin(GL.GL_QUAD_STRIP)
        GL.glVertex3d(0,0,0)
        GL.glVertex3d(l,0,0)
        GL.glVertex3d(0,w,0)
        GL.glVertex3d(l,w,0)
        GL.glEnd()
        self.qglColor(self.trolltechPurple)
        GL.glBegin(GL.GL_QUAD_STRIP)
        GL.glVertex3d(l,w,h)
        GL.glVertex3d(0,w,h)
        GL.glVertex3d(l,0,h)
        GL.glVertex3d(0,0,h)
        GL.glEnd()

    def xyz(self):
        self.qglColor(self.blue)
        GL.glVertex3d(0, 0, -10)
        GL.glVertex3d(0, 0, 10)
        self.qglColor(self.red)
        GL.glVertex3d(10, 0, 0)
        GL.glVertex3d(-10, 0, 0)
        self.qglColor(self.green)
        GL.glVertex3d(0, -10, 0)
        GL.glVertex3d(0, 10, 0)
    def square(self,x,y,z,h):
        self.qglColor(self.trolltechPurple)
        GL.glBegin(GL.GL_QUAD_STRIP)
        GL.glVertex3d(0+x, 0+y, 0+z)
        GL.glVertex3d(h+x, 0+y, 0+z)
        GL.glVertex3d(0+x, h+y, 0+z)
        GL.glVertex3d(h+x, h+y, 0+z)
        GL.glEnd()
        self.qglColor(self.red)
        GL.glBegin(GL.GL_LINES)
        GL.glVertex3d(0+x, 0+y, 0+z-0.002)
        GL.glVertex3d(h+x, 0+y, 0+z-0.002)
        GL.glVertex3d(0+x, h+y, 0+z-0.002)
        GL.glVertex3d(h+x, h+y, 0+z-0.002)
        GL.glVertex3d(0+x, 0+y, 0+z-0.002)
        GL.glVertex3d(0+x, h+y, 0+z-0.002)
        GL.glVertex3d(h+x, 0+y, 0+z-0.002)
        GL.glVertex3d(h+x, h+y, 0+z-0.002)
        GL.glEnd()
    def grid(self):
        for i in range(21):
            if i == 10:
                self.qglColor(self.myColor1)
            else:
                self.qglColor(self.trolltechPurple)
                GL.glVertex3d(-0.8, i * 0.08 - 0.8, 0)
                GL.glVertex3d(0.8, i * 0.08 - 0.8, 0)
                GL.glVertex3d(i * 0.08 - 0.8, 0.8, 0)
                GL.glVertex3d(i * 0.08 - 0.8, -0.8, 0)

    def gridCube(self):
        for i in range(gridN):
            for ii in range(gridN):
                self.qglColor(QtGui.QColor.fromCmykF(i * 0.00808, ii * 0.0086, 0, 0))
                GL.glVertex3d(-xd, i * yd - xd, 0 + ii * yd)
                GL.glVertex3d(xd, i * yd - xd, 0 + ii * yd)
                GL.glVertex3d(i * yd - xd, xd, 0 + ii * yd)
                GL.glVertex3d(i * yd - xd, -xd, 0 + ii * yd)
                GL.glVertex3d(-xd + 0 + ii * yd, i * yd - xd, 0)
                GL.glVertex3d(-xd + 0 + ii * yd, i * yd - xd, xd * 2)

    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle
