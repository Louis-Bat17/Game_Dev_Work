import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from random import randomInteger

# Maze dimensions
N = 10  # Number of rows
M = 10  # Number of columns
# Maze cell size
CELL_SIZE = 30
# Specify Window Size
WINDOW_WIDTH = M * CELL_SIZE
WINDOW_HEIGHT = N * CELL_SIZE
# Data Structure for the maze
maze = [[0 for _ in range(M)] for _ in range(N)]
# Entrance and exit coordinates
entrance = (0, 0)
exit = (N - 1, M - 1)

def generate_maze():
    # Initialize maze with all walls
    maze = [[1 for _ in range(M)] for _ in range(N)]
    # Generate maze using random depth-first search
    stack = [(0, 0)]  # Start at top-left corner
    visited = set([(0, 0)])

    while stack:
        current_cell = stack[-1]
        x, y = current_cell
        # Find unvisited neighbors
        neighbors = []
        if x > 0 and (x - 1, y) not in visited:  # Left neighbor
            neighbors.append((x - 1, y))
        if x < N - 1 and (x + 1, y) not in visited:  # Right neighbor
            neighbors.append((x + 1, y))
        if y > 0 and (x, y - 1) not in visited:  # Bottom neighbor
            neighbors.append((x, y - 1))
        if y < M - 1 and (x, y + 1) not in visited:  # Top neighbor
            neighbors.append((x, y + 1))
        if neighbors:
            # Choose a random neighbor
            next_cell = neighbors[randomInteger(0, len(neighbors) - 1)]
            nx, ny = next_cell
            # Remove wall between current cell and chosen neighbor
            if nx == x - 1:  # Left neighbor
                maze[x][y] &= ~2  # Remove right wall of current cell
                maze[nx][ny] &= ~8  # Remove left wall of next cell
            elif nx == x + 1:  # Right neighbor
                maze[x][y] &= ~8  # Remove left wall of current cell
                maze[nx][ny] &= ~2  # Remove right wall of next cell
            elif ny == y - 1:  # Bottom neighbor
                maze[x][y] &= ~4  # Remove top wall of current cell
                maze[nx][ny] &= ~1  # Remove bottom wall of next cell
            elif ny == y + 1:  # Top neighbor
                maze[x][y] &= ~1  # Remove bottom wall of current cell
                maze[nx][ny] &= ~4  # Remove top wall of next cell
            stack.append(next_cell)
            visited.add(next_cell)
        else:
            stack.pop()
    return maze

def draw_cell(row, col):
    x = col * CELL_SIZE
    y = row * CELL_SIZE

    glBegin(GL_QUADS)
    if maze[row][col] & 1:  # Bottom wall
        glVertex2f(x, y)
        glVertex2f(x + CELL_SIZE, y)
        glVertex2f(x + CELL_SIZE, y)
        glVertex2f(x, y)
    if maze[row][col] & 2:  # Right wall
        glVertex2f(x + CELL_SIZE, y)
        glVertex2f(x + CELL_SIZE, y + CELL_SIZE)
        glVertex2f(x + CELL_SIZE, y + CELL_SIZE)
        glVertex2f(x + CELL_SIZE, y)
    if maze[row][col] & 4:  # Top wall
        glVertex2f(x + CELL_SIZE, y + CELL_SIZE)
        glVertex2f(x, y + CELL_SIZE)
        glVertex2f(x, y + CELL_SIZE)
        glVertex2f(x + CELL_SIZE, y + CELL_SIZE)
    if maze[row][col] & 8:  # Left wall
        glVertex2f(x, y + CELL_SIZE)
        glVertex2f(x, y)
        glVertex2f(x, y)
        glVertex2f(x, y + CELL_SIZE)
    glEnd()

def draw_maze():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glLoadIdentity()
    # draw cells
    for i in range(N):
        for j in range(M):
            draw_cell(i, j)

    # Draw entrance and exit
    entrance_x = entrance[1] * CELL_SIZE
    entrance_y = entrance[0] * CELL_SIZE
    exit_x = exit[1] * CELL_SIZE
    exit_y = exit[0] * CELL_SIZE

    glColor3f(0.0, 1.0, 0.0)  # Green color for entrance
    glBegin(GL_QUADS)
    glVertex2f(entrance_x, entrance_y)
    glVertex2f(entrance_x + CELL_SIZE, entrance_y)
    glVertex2f(entrance_x + CELL_SIZE, entrance_y + CELL_SIZE)
    glVertex2f(entrance_x, entrance_y + CELL_SIZE)
    glEnd()

    glColor3f(1.0, 0.0, 0.0)  # Red color for exit
    glBegin(GL_QUADS)
    glVertex2f(exit_x, exit_y)
    glVertex2f(exit_x + CELL_SIZE, exit_y)
    glVertex2f(exit_x + CELL_SIZE, exit_y + CELL_SIZE)
    glVertex2f(exit_x, exit_y + CELL_SIZE)
    glEnd()
    glFlush()

def main():
    global maze, N, M
    maze = generate_maze()
    # Initialize OpenGL and generate maze
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Q2.4 Maze")
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, -1, 1)
    glutDisplayFunc(draw_maze)
    glutMainLoop()

if __name__ == "__main__":
    main() # initiate maze