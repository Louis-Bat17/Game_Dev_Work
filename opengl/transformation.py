import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dot_product(vector1, vector2):
    return vector1.x * vector2.x + vector1.y * vector2.y

def cross_product(vector1, vector2):
    return vector1.x * vector2.y - vector1.y * vector2.x

def rotate_point(point, angle):
    # Convert angle from degrees to radians
    angle = math.radians(angle)

    # Perform rotation
    x = point.x * math.cos(angle) - point.y * math.sin(angle)
    y = point.x * math.sin(angle) + point.y * math.cos(angle)

    return Point(x, y)

def translate_point(point, translation):
    x = point.x + translation.x
    y = point.y + translation.y

    return Point(x, y)

def scale_point(point, scaling):
    x = point.x * scaling.x
    y = point.y * scaling.y

    return Point(x, y)

def shear_point(point, shear):
    x = point.x + shear.x * point.y
    y = point.y + shear.y * point.x

    return Point(x, y)

def affine_transformation_2d(points_before, points_after):
    n = len(points_before)

    # Check if the number of points is sufficient
    if n < 3:
        raise ValueError("At least 3 points are required to uniquely specify a 2D affine transformation.")

    # Build the transformation matrix using the given points
    matrix = []
    for i in range(n):
        x_b, y_b = points_before[i].x, points_before[i].y
        x_a, y_a = points_after[i].x, points_after[i].y
        matrix.append([x_b, y_b, 1, 0, 0, 0, -x_a * x_b, -x_a * y_b, -x_a])
        matrix.append([0, 0, 0, x_b, y_b, 1, -y_a * x_b, -y_a * y_b, -y_a])
    return matrix

def affine_transformation_3d(points_before, points_after):
    n = len(points_before)

    # Check if the number of points is sufficient
    if n < 4:
        raise ValueError("At least 4 points are required to uniquely specify a 3D affine transformation.")

    # Build the transformation matrix using the given points
    matrix = []
    for i in range(n):
        # Get coordinates for points_before and points_after
        x_b, y_b, z_b = points_before[i].x, points_before[i].y, points_before[i].z
        x_a, y_a, z_a = points_after[i].x, points_after[i].y, points_after[i].z
        
        # Add the row for the x-axis transformation
        matrix.append([x_b, y_b, z_b, 1, 0, 0, 0, -x_a * x_b, -x_a * y_b, -x_a * z_b, -x_a])
        
        # Add the row for the y-axis transformation
        matrix.append([0, 0, 0, x_b, y_b, z_b, 1, -y_a * x_b, -y_a * y_b, -y_a * z_b, -y_a])
        
        # Add the row for the z-axis transformation
        matrix.append([0, 0, 0, 0, 0, 0, 0, z_b, y_b * z_b, -x_b * z_b, -z_a])
        
    return matrix

# Example usage
point = Point(1, 1)
vector = Vector(2, 3)
rotation_angle = 45 

# Rotate the point
rotated_point = rotate_point(point, rotation_angle)
print("Rotated point:", rotated_point.x, rotated_point.y)

# Translate the point
translation = Vector(3, 2)
translated_point = translate_point(point, translation)
print("Translated point:", translated_point.x, translated_point.y)

# Scale the point
scaling = Vector(2, 2)
scaled_point = scale_point(point, scaling)
print("Scaled point:", scaled_point.x, scaled_point.y)

# Shear the point
shear = Vector(0.5, 0.5)
sheared_point = shear_point(point, shear)
print("Sheared point:", sheared_point.x, sheared_point.y)

# Specify 2D affine transformation using points
points_before = [Point(1, 1), Point(2, 3), Point(4, 2)]
points_after = [Point(3, 4), Point(5, 6), Point(7, 5)]
transformation_matrix = affine_transformation_2d(points_before, points_after)
print("Transformation matrix:", transformation_matrix)