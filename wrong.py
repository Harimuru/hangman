from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys 
import math

def Init():
    print("init")
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-150,150,-150,150)

def drawBAS(X1,Y1,X2,Y2):
    m_new = 2*(Y2-Y1)
    slope = m_new - (X2 - X1)
    y = Y1
    for x in range(X1,X2+1):
        glVertex2f(x,y)
        slope = slope + m_new
        if(slope >=0):
            y = y+1
            slope = slope - 2*(X2-X1)

def drawDDA(x1,y1,x2,y2):
    x,y =x1,y1
    if (x2 - x1) > (y2 - y1):
        length = abs(x2 - x1)
        print(" X = ")
        print(length)
    else:
        length = abs(y2 - y1)
        print ("Y  = ")
        print(length)
    dx = (x2 - x1)/float(length)
    dy = (y2 - y1)/float(length)
    x= x1
    y = y1
    for i in range (length) :
        glVertex2f(x,y)
        x  =x + dx
        y = y +dy


def plotpoints():
    print("plotpoints")
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,1.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    print("ploting points ")
    for i in range(1,5):
    	drawDDA(25*i,5,25*i,70)					#1
    	drawDDA(25*i,-70,25*i,-5)				#2
    drawDDA(15,60,110,15)
    drawDDA(15,-15,110,-60)
    glEnd()
    glFlush()

def main():
    print("main")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("linetest")
    Init()
    glutDisplayFunc(plotpoints)
    glutMainLoop()

main()
