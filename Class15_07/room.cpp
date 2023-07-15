#include <GL/glut.h>

 

void display()
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    // Set up viewing transformation
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0);

    // Enable lighting and depth testing
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_DEPTH_TEST);

    // Set up light position and properties
    GLfloat light_position[] = { 1, 1, 1, 0 };
    GLfloat light_color[] = { 1, 1, 1, 1 };
    glLightfv(GL_LIGHT0, GL_POSITION, light_position);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color);

    // Set material properties for the sphere
    GLfloat ambient[] = { 0.2, 0.2, 0.2, 1.0 };
    GLfloat diffuse[] = { 0.6, 0.6, 0.6, 1.0 };
    GLfloat specular[] = { 0.8, 0.8, 0.8, 1.0 };
    GLfloat shininess = 64.0;
    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient);
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse);
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular);
    glMaterialf(GL_FRONT, GL_SHININESS, shininess);

    // Draw a sphere
    glutSolidSphere(1.0, 50, 50);

    glFlush();
}

 

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(500, 500);
    glutCreateWindow("Metallic Sphere");

    glClearColor(0, 0, 0, 1);

    glutDisplayFunc(display);

    glutMainLoop();

    return 0;
}