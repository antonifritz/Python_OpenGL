import sys
import random

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *

color_list = []

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)
    set_random_color()

def shutdown():
    pass

def set_random_color():
    for i in range(3):
        color_list.append(random.random())

def draw_rectangle(x, y, size_a, size_b, d = 0.0):
        glColor3f(color_list[0], color_list[1], color_list[2])
        glBegin(GL_TRIANGLES)
        glVertex2f(x, y)
        glVertex2f(x + size_a + d, y)
        glVertex2f(x, y + size_b + d)
        glEnd()
        glColor3f(color_list[0], color_list[1], color_list[2])
        glBegin(GL_TRIANGLES)
        glVertex2f(x + size_a + d, y)
        glVertex2f(x, y + size_b + d)
        glVertex2f(x + size_a + d, y + size_b + d)
        glEnd()

def draw_white_rectangle(x, y, size_a, size_b, d = 0.0):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x + size_a + d, y)
    glVertex2f(x, y + size_b + d)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x + size_a + d, y)
    glVertex2f(x, y + size_b + d)
    glVertex2f(x + size_a + d, y + size_b + d)
    glEnd()

def sierpinsky_carpet(x, y, size_a, size_b):
    draw_rectangle(x, y, size_a, size_b)
    draw_rectangle(x + size_a, y, size_a, size_b)
    draw_rectangle(x + 2 * size_a, y, size_a, size_b)
    draw_rectangle(x, y + size_b, size_a, size_b)
    draw_white_rectangle(x + size_a, y + size_b, size_a, size_b)
    draw_rectangle(x + 2 * size_a, y + size_b, size_a, size_b)
    draw_rectangle(x, y + 2 * size_b, size_a, size_b)
    draw_rectangle(x + size_a, y + 2 * size_b, size_a, size_b)
    draw_rectangle(x + 2 * size_a, y + 2 * size_b, size_a, size_b)

def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    #glBegin(GL_TRIANGLES)
    #glColor3f(1.0, 0.0, 0.2)
    #glVertex2f(-50.0, -25.0)
    #glColor3f(0.9, 1.0, 0.2)
    #glVertex2f(50.0, -25.0)
    #glColor3f(0.5, 0.3, 1.0)
    #glVertex(0.0, 70.0)
    #glEnd()

    #glColor3f(color_list[0], color_list[1], color_list[2])
    #draw_rectangle(-80.0, -50.0, 10.0, 10.0)
    
    sierpinsky_carpet(-80.0, -80.0, 30.0, 20.0)

    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()