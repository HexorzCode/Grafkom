from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_D(x_offset):
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    # Vertical bar
    glVertex2f(x_offset + 0.0, 0.0)
    glVertex2f(x_offset + 0.1, 0.0)
    glVertex2f(x_offset + 0.1, 0.8)
    glVertex2f(x_offset + 0.0, 0.8)
    # Curved body
    glVertex2f(x_offset + 0.1, 0.0)
    glVertex2f(x_offset + 0.4, 0.0)
    glVertex2f(x_offset + 0.4, 0.8)
    glVertex2f(x_offset + 0.1, 0.8)
    glEnd()


def draw_D_hole(x_offset):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(x_offset + 0.2, 0.1)
    glVertex2f(x_offset + 0.35, 0.1)
    glVertex2f(x_offset + 0.35, 0.7)
    glVertex2f(x_offset + 0.2, 0.7)
    glEnd()


def draw_A(x_offset):
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    # Left leg
    glVertex2f(x_offset + 0.0, 0.0)
    glVertex2f(x_offset + 0.1, 0.0)
    glVertex2f(x_offset + 0.2, 0.8)
    glVertex2f(x_offset + 0.1, 0.8)
    # Right leg
    glVertex2f(x_offset + 0.3, 0.0)
    glVertex2f(x_offset + 0.4, 0.0)
    glVertex2f(x_offset + 0.3, 0.8)
    glVertex2f(x_offset + 0.2, 0.8)
    # Middle bar
    glVertex2f(x_offset + 0.1, 0.4)
    glVertex2f(x_offset + 0.3, 0.4)
    glVertex2f(x_offset + 0.3, 0.5)
    glVertex2f(x_offset + 0.1, 0.5)
    glEnd()


def draw_F(x_offset):
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    # Vertical bar
    glVertex2f(x_offset + 0.0, 0.0)
    glVertex2f(x_offset + 0.1, 0.0)
    glVertex2f(x_offset + 0.1, 0.8)
    glVertex2f(x_offset + 0.0, 0.8)
    # Top bar
    glVertex2f(x_offset + 0.1, 0.7)
    glVertex2f(x_offset + 0.4, 0.7)
    glVertex2f(x_offset + 0.4, 0.8)
    glVertex2f(x_offset + 0.1, 0.8)
    # Middle bar
    glVertex2f(x_offset + 0.1, 0.4)
    glVertex2f(x_offset + 0.3, 0.4)
    glVertex2f(x_offset + 0.3, 0.5)
    glVertex2f(x_offset + 0.1, 0.5)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    spacing = 1.0
    start_x = -2.5

    # Draw letters
    draw_D(start_x + spacing * 0)
    draw_A(start_x + spacing * 1)
    draw_F(start_x + spacing * 2)
    draw_F(start_x + spacing * 3)
    draw_A(start_x + spacing * 4)

    # Draw holes
    draw_D_hole(start_x + spacing * 0)

    glFlush()


def init():
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-3.0, 3.5, -1.0, 1.5)
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 600)
    glutCreateWindow(b"DAFFA - OpenGL Primitives")
    init()
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
grafkom