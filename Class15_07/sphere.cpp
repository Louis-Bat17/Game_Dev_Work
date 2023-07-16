#include <GL/glut.h>

GLfloat rotation = 0.0;

void init() {
    glClearColor(0.0, 0.0, 0.0, 1.0);
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_COLOR_MATERIAL);

    // Light source against the sphere as follows:
    GLfloat light_pos[] = { 1.0, 1.0, 1.0, 0.0 };
    GLfloat light_color[] = { 1.0, 1.0, 1.0, 1.0 };
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color);
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_color);

    // Set the metallic effects of the sphere
    GLfloat sphere_color[] = { 0.8, 0.8, 0.8, 1.0 };
    GLfloat sphere_shininess = 100.0;
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, sphere_color);
    glMaterialfv(GL_FRONT, GL_SPECULAR, sphere_color);
    glMaterialf(GL_FRONT, GL_SHININESS, sphere_shininess);
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
    glRotatef(rotation, 1.0, 1.0, 1.0);
    glutSolidSphere(1.0, 50, 50);
    glFlush();
    glutSwapBuffers();

    // Set the sphere to rotate
    rotation += 0.5;
}

void reshape(int width, int height) {
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0, static_cast<float>(width) / height, 0.1, 100.0);
    glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(500, 500);
    glutCreateWindow("OpenGL Sphere");
    init();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutIdleFunc(display);
    glutMainLoop();
    return 0;
}
