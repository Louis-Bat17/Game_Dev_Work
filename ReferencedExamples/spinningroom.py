from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Global variables
rotation = 0.0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)

    # Enable and set up the first light source (directional light)
    glEnable(GL_LIGHT0)
    light0_direction = [1.0, 1.0, 1.0, 0.0]  # Directional light direction
    light0_color = [1.0, 1.0, 1.0, 1.0]  # White light color
    glLightfv(GL_LIGHT0, GL_POSITION, light0_direction)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_color)

    # Enable and set up the second light source (point light)
    glEnable(GL_LIGHT1)
    light1_position = [2.0, 2.0, 2.0, 1.0]  # Point light position
    light1_color = [0.0, 1.0, 0.0, 1.0]  # Green light color
    glLightfv(GL_LIGHT1, GL_POSITION, light1_position)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light1_color)

    # Enable and set up the third light source (spotlight)
    glEnable(GL_LIGHT2)
    light2_position = [0.0, 3.0, 0.0, 1.0]  # Spotlight position
    light2_direction = [0.0, -1.0, 0.0]  # Spotlight direction
    light2_color = [1.0, 0.0, 0.0, 1.0]  # Red light color
    glLightfv(GL_LIGHT2, GL_POSITION, light2_position)
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, light2_direction)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, light2_color)
    glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 30.0)  # Spotlight cutoff angle
    glLightf(GL_LIGHT2, GL_SPOT_EXPONENT, 2.0)  # Spotlight exponent

def display():
    global rotation

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0.0, 3.0, 8.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glRotatef(rotation, 0.0, 1.0, 0.0)

    # Draw the room
    draw_room()

    glFlush()
    glutSwapBuffers()

    rotation += 0.5

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width) / height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def draw_room():
    # Draw the walls
    glPushMatrix()
    glTranslatef(0.0, 2.5, 0.0)
    glScalef(5.0, 5.0, 0.1)
    draw_cube()
    glPopMatrix()

    # Draw the objects in the room
    glPushMatrix()
    glTranslatef(-1.5, 0.0, 0.0)
    glRotatef(45.0, 0.0, 1.0, 0.0)
    set_material(0.8, 0.8, 0.8, 1.0, 0.2)  # Matte material
    draw_cube()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1.5, 0.0, 0.0)
    glRotatef(45.0, 1.0, 0.0, 0.0)
    set_material(0.8, 0.8, 0.8, 1.0, 0.8)  # Glossy material
    draw_cube()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, 0.0, -1.5)
    set_material(1.0, 1.0, 1.0, 0.4, 1.0)  # Transparent material
    draw_sphere()
    glPopMatrix()

def set_material(r, g, b, alpha, shininess):
    material_color = [r, g, b, alpha]
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, material_color)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_color)
    glMaterialf(GL_FRONT, GL_SHININESS, shininess)

def draw_cube():
    # Draw a cube with unit dimensions
    glutSolidCube(1.0)

def draw_sphere():
    # Draw a sphere with radius 0.5
    glutSolidSphere(0.5, 50, 50)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"OpenGL Room")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
