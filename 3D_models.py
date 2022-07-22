import sys
import math
import numpy
from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *

u_array = []
v_array = []

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

def shutdown():
    pass

def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)

def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()

def make_3D_array(N):
    return numpy.zeros((N, N, 3))

def fill_3D_array(N, array):
    for i in range(N):
        for j in range(N):
            array[i][j][0] = calculate_x(u_array[i], v_array[j])
            array[i][j][1] = calculate_y(u_array[i])
            array[i][j][2] = calculate_z(u_array[i], v_array[j])

def fill_arrays(N):
    value = 0.0
    step = 1/(N-1)
    for i in range(N):
        u_array.append(value)
        v_array.append(value)
        value = round(value + step, 4)

def calculate_x(u, v):
    return (-90 * pow(u, 5) + 225 * pow(u, 4) - 270 * pow(u, 3) + 180 * pow(u, 2) - 45 * u) * math.cos(math.pi * v)

def calculate_y(u):
    return (160 * pow(u, 4) - 320 * pow(u, 3) + 160 * pow(u, 2) - 5)

def calculate_z(u, v):
    return (-90 * pow(u, 5) + 225 * pow(u, 4) - 270 * pow(u, 3) + 180 * pow(u, 2) - 45 * u) * math.sin(math.pi * v)
    
def render(time, N, array):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    spin(time * 180 / 3.1415)
    axes()
    glBegin(GL_POINTS)
    for i in range(N):
        for j in range(N):
            glVertex(array[i][j][0], array[i][j][1], array[i][j][2])
    glEnd()
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
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    N = int(input("Enter legth of u and v arrays: "))
    fill_arrays(N)
    array = make_3D_array(N)
    fill_3D_array(N, array)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime(), N, array)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
