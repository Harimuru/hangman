from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys 
import math

def Init():
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
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,1.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    print("ploting points ")
    drawDDA(-75,-100,-25,-100)              # 1 
    drawDDA(-50,50,50,50)                   # 3
    drawDDA(-50,-100,-50,50)                # 2
    drawDDA(50,25,50,50)                    # 4
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("linetest")
    Init()
    glutDisplayFunc(plotpoints)
    glutMainLoop()

main()
