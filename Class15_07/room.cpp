#include <GL/glut.h>

GLfloat rotation = 0.0;

void init();
void display();
void reshape(int width, int height);
void draw_room();
void draw_cube();

void init() {
    glClearColor(0.0, 0.0, 0.0, 1.0);
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_LIGHTING);
    glEnable(GL_COLOR_MATERIAL);

    // Enable and set up the first light source (directional light)
    glEnable(GL_LIGHT0);
    GLfloat light0_direction[] = { 1.0f, 1.0f, 1.0f, 0.0f }; // Directional light direction
    GLfloat light0_color[] = { 1.0f, 1.0f, 1.0f, 1.0f }; // White light color
    glLightfv(GL_LIGHT0, GL_POSITION, light0_direction);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_color);

    // Enable and set up the second light source (point light)
    glEnable(GL_LIGHT1);
    GLfloat light1_position[] = { 2.0f, 2.0f, 2.0f, 1.0f }; // Point light position
    GLfloat light1_color[] = { 0.0f, 1.0f, 0.0f, 1.0f }; // Green light color
    glLightfv(GL_LIGHT1, GL_POSITION, light1_position);
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light1_color);

    // Enable and set up the third light source (spotlight)
    glEnable(GL_LIGHT2);
    GLfloat light2_position[] = { 0.0f, 3.0f, 0.0f, 1.0f }; // Spotlight position
    GLfloat light2_direction[] = { 0.0f, -1.0f, 0.0f }; // Spotlight direction
    GLfloat light2_color[] = { 1.0f, 0.0f, 0.0f, 1.0f }; // Red light color
    glLightfv(GL_LIGHT2, GL_POSITION, light2_position);
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, light2_direction);
    glLightfv(GL_LIGHT2, GL_DIFFUSE, light2_color);
    glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 30.0f); // Spotlight cutoff angle
    glLightf(GL_LIGHT2, GL_SPOT_EXPONENT, 2.0f); // Spotlight exponent
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    gluLookAt(0.0, 0.0, 25.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0); // Adjust the viewing perspective

    glRotatef(30.0f, 1.0f, 0.0f, 0.0f); // Rotate around x-axis
    glRotatef(rotation, 0.0f, 1.0f, 0.0f); // Rotate around y-axis

    draw_room();

    glFlush();
    glutSwapBuffers();

    rotation += 0.03f;
}

void reshape(int width, int height) {
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0, static_cast<float>(width) / height, 0.1, 100.0);
    glMatrixMode(GL_MODELVIEW);
}

void draw_room() {
    // Draw the walls
    glPushMatrix();
    glTranslatef(0.0f, 2.5f, 0.0f);
    glScalef(5.0f, 5.0f, 5.0f); // Increase the scaling factor
    draw_cube();
    glPopMatrix();
}

void draw_cube() {
    glBegin(GL_QUADS);

    // Back wall
    glColor3f(0.5f, 0.5f, 0.5f); // Gray color
    glVertex3f(-1.0f, -1.0f, 1.0f);
    glVertex3f(1.0f, -1.0f, 1.0f);
    glVertex3f(1.0f, 1.0f, 1.0f);
    glVertex3f(-1.0f, 1.0f, 1.0f);

    // Left wall - Glossy
    glColor3f(1.0f, 1.0f, 1.0f); // White color
    GLfloat diffuse_color[] = { 0.5f, 0.5f, 0.5f, 1.0f };
    GLfloat specular_color[] = { 1.0f, 1.0f, 1.0f, 1.0f };
    GLfloat shininess[] = { 100.0f };
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse_color);
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular_color);
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess);
    glVertex3f(-1.0f, -1.0f, -1.0f);
    glVertex3f(-1.0f, -1.0f, 1.0f);
    glVertex3f(-1.0f, 1.0f, 1.0f);
    glVertex3f(-1.0f, 1.0f, -1.0f);

    // Right wall - Matte
    glColor3f(1.0f, 1.0f, 1.0f); // Gray color
    GLfloat matte_diffuse_color[] = { 0.5f, 0.5f, 0.5f, 1.0f };
    glMaterialfv(GL_FRONT, GL_DIFFUSE, matte_diffuse_color);
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular_color);
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess);
    glVertex3f(1.0f, -1.0f, -1.0f);
    glVertex3f(1.0f, -1.0f, 1.0f);
    glVertex3f(1.0f, 1.0f, 1.0f);
    glVertex3f(1.0f, 1.0f, -1.0f);

    // Top wall
    glColor3f(0.8f, 0.8f, 0.8f); // Gray color
    glVertex3f(-1.0f, 1.0f, -1.0f);
    glVertex3f(1.0f, 1.0f, -1.0f);
    glVertex3f(1.0f, 1.0f, 1.0f);
    glVertex3f(-1.0f, 1.0f, 1.0f);

    // Bottom wall
    glColor3f(0.5f, 0.5f, 0.5f); // Gray color
    glVertex3f(-1.0f, -1.0f, -1.0f);
    glVertex3f(1.0f, -1.0f, -1.0f);
    glVertex3f(1.0f, -1.0f, 1.0f);
    glVertex3f(-1.0f, -1.0f, 1.0f);

    glEnd();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(800, 600);
    glutCreateWindow("OpenGL Room");
    init();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutIdleFunc(display);
    glutMainLoop();
    return 0;
}
