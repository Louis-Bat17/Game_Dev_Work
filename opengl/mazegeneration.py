import glfw
from OpenGL.GL import *
import random

# Maze dimensions
N = 10  # Number of rows
M = 10  # Number of columns

# Window dimensions
window_width = 800
window_height = 800

# Cell size
cell_size = min(window_width / N, window_height / M)

# Maze grid
maze = [[1] * M for _ in range(N)]  # 1 represents walls, 0 represents paths

# Generate the maze using depth-first search algorithm
def generate_maze(x, y):
    maze[x][y] = 0  # Mark the current cell as a path
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    random.shuffle(directions)  # Randomize the order of directions

    for dx, dy in directions:
        nx, ny = x + 2 * dx, y + 2 * dy
        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
            maze[x + dx][y + dy] = 0  # Remove the wall between current and next cell
            generate_maze(nx, ny)  # Recursively visit the next cell

# Initialize OpenGL and create the maze
def init():
    if not glfw.init():
        return

    window = glfw.create_window(window_width, window_height, "Maze", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glOrtho(0, window_width, 0, window_height, -1, 1)
    glClearColor(1, 1, 1, 1)

    generate_maze(0, 0)  # Generate the maze

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        draw_maze()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

# Draw the maze using OpenGL
def draw_maze():
    glColor3f(0, 0, 0)
    glLineWidth(2)

    for i in range(N):
        for j in range(M):
            x = j * cell_size
            y = i * cell_size

            if maze[i][j] == 1:
                glBegin(GL_LINES)
                glVertex2f(x, y)
                glVertex2f(x + cell_size, y)
                glVertex2f(x + cell_size, y)
                glVertex2f(x + cell_size, y + cell_size)
                glVertex2f(x + cell_size, y + cell_size)
                glVertex2f(x, y + cell_size)
                glVertex2f(x, y + cell_size)
                glVertex2f(x, y)
                glEnd()

    # Remove two sides for entrance and exit
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(cell_size, 0)
    glVertex2f(cell_size, cell_size)
    glVertex2f(0, cell_size)
    glEnd()

    glColor3f(0, 1, 0)
    glBegin(GL_QUADS)
    glVertex2f((M - 1) * cell_size, (N - 1) * cell_size)
    glVertex2f(M * cell_size, (N - 1) * cell_size)
    glVertex2f(M * cell_size, N * cell_size)
    glVertex2f
