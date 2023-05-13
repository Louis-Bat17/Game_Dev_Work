"""
    Find source of code here: ??
"""

import glfw
from OpenGL.GL import *

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, 0.5)
    glEnd()

def main():
    # Initialize glfw
    if not glfw.init():
        return

    # Create a window
    window = glfw.create_window(640, 480, "OpenGL Triangle", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Main loop
    while not glfw.window_should_close(window):
        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        # Draw the triangle
        glColor3f(1.0, 0.0, 0.0) # set color to red
        draw_triangle()

        # Swap buffers
        glfw.swap_buffers(window)

        # Poll for events
        glfw.poll_events()

    # Clean up
    glfw.terminate()

if __name__ == '__main__':
    main()
