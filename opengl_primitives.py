import sys

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass

def draw_rectangle(x, y, size_a, size_b, d = 0.0):
        glBegin(GL_TRIANGLES)
        glVertex2f(x, y)
        glVertex2f(x + size_a + d, y)
        glVertex2f(x, y + size_b + d)
        glEnd()
        glBegin(GL_TRIANGLES)
        glVertex2f(x + size_a + d, y)
        glVertex2f(x, y + size_b + d)
        glVertex2f(x + size_a + d, y + size_b + d)
        glEnd()

def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.2)
    glVertex2f(-50.0, -25.0)
    glColor3f(0.9, 1.0, 0.2)
    glVertex2f(50.0, -25.0)
    glColor3f(0.5, 0.3, 1.0)
    glVertex(0.0, 30.0)
    glEnd()

    glColor3f(1, 0.6, 0)
    draw_rectangle(-80.0, -80.0, 60.0, 40.0, 5)

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