from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

rotation = 0.0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    #  Light source against the sphere as follows:
    light_pos = [1.0, 1.0, 1.0, 0.0]
    light_color = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_color)


    # Set the metallic effects of the sphere
    sphere_color = [0.8, 0.8, 0.8, 1.0]
    sphere_shininess = 100.0
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, sphere_color)
    glMaterialfv(GL_FRONT, GL_SPECULAR, sphere_color)
    glMaterialf(GL_FRONT, GL_SHININESS, sphere_shininess)

def display():
    global rotation

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glRotatef(rotation, 1.0, 1.0, 1.0)
    glutSolidSphere(1.0, 50, 50)
    glFlush()
    glutSwapBuffers()

    # set the sphere to rotate
    rotation += 0.5

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width) / height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"OpenGL Sphere")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
