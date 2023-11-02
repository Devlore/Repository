import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 1, 0)
    glColor3f(0, 1, 0)
    glVertex3f(-1, -1, 0)
    glColor3f(0, 0, 1)
    glVertex3f(1, -1, 0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(2, 0, 5, 0, 0, 0, 0, 1, 0)
    draw_triangle()
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, width / height, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    if key == '\033':
        sys.exit(0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow('3D Triangle')
glEnable(GL_DEPTH_TEST)
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMainLoop()