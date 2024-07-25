from AnimationLibrary import Point
import math
import numpy as np

# NOTE: parts of this code are AI generated, they are not parts of library, only used for development testing






def normalize_angle_positive(angle):
    """
    Wrap the angle between 0 and 2 * pi.

    Args:
        angle (float): angle to wrap.

    Returns:
         The wrapped angle.

    """
    pi_2 = 2. * np.pi

    return math.fmod(math.fmod(angle, pi_2) + pi_2, pi_2)





class T_LINE():
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def get_angle(self):
        dx = self.B.x - self.A.x
        dy = self.B.y - self.A.y

        # Handle coincident points
        if dx == 0 and dy == 0:
            return None  # Indicate coincident points

        # Calculate angle in radians using arctangent
        angle = math.atan2(dy, dx)

        if angle < 0:
            angle = normalize_angle_positive(angle)

        # Convert to degrees if needed (optional)
        # degrees = math.degrees(angle)

        return angle
    def get_octant(self):
        angle = math.degrees(self.get_angle())

        # Handle coincident points (already checked in get_angle)
        if angle is None:
            return "Undefined (coincident points)"

        # Determine octant based on angle (considering computer screen)
        if angle >= 0 and angle < 45:
            return "I"
        elif angle >= 45 and angle < 90:
            return "II"
        elif angle >= 90 and angle < 135:
            return "III"  # Added check for octant III
        elif angle >= 135 and angle < 180:
            return "IV"  # Added check for octant IV
        elif angle >= 180 and angle < 225:
            return "V"
        elif angle >= 225 and angle < 270:
            return "VI"
        elif angle >= 270 and angle < 315:
            return "VII"  # Handles positive y-axis (special case)
        else:
            return "VIII"  # Handles negative y-axis (special case)


def do_all_transformations(line: T_LINE):

    line_trans = do_nothing(line)
    if line_trans.get_octant() == "I":
        print(f"1: L0: [({line.A.x}, {line.A.y}), ({line.B.x}, {line.B.y})] {line.get_octant()} {math.degrees(line.get_angle())}, L1: [({line_trans.A.x}, {line_trans.A.y}), ({line_trans.B.x}, {line_trans.B.y})] {line_trans.get_octant()} {math.degrees(line_trans.get_angle())}")

    line_trans = negate_x(line)
    if line_trans.get_octant() == "I":
        print(f"2: L0: [({line.A.x}, {line.A.y}), ({line.B.x}, {line.B.y})] {line.get_octant()} {math.degrees(line.get_angle())}, L1: [({line_trans.A.x}, {line_trans.A.y}), ({line_trans.B.x}, {line_trans.B.y})] {line_trans.get_octant()} {math.degrees(line_trans.get_angle())}")

    line_trans = negate_y(line)
    if line_trans.get_octant() == "I":
        print(f"3: L0: [({line.A.x}, {line.A.y}), ({line.B.x}, {line.B.y})] {line.get_octant()} {math.degrees(line.get_angle())}, L1: [({line_trans.A.x}, {line_trans.A.y}), ({line_trans.B.x}, {line_trans.B.y})] {line_trans.get_octant()} {math.degrees(line_trans.get_angle())}")

    line_trans = swap_x_with_y(line)
    if line_trans.get_octant() == "I":
        print(f"4: L0: [({line.A.x}, {line.A.y}), ({line.B.x}, {line.B.y})] {line.get_octant()} {math.degrees(line.get_angle())}, L1: [({line_trans.A.x}, {line_trans.A.y}), ({line_trans.B.x}, {line_trans.B.y})] {line_trans.get_octant()} {math.degrees(line_trans.get_angle())}")

    line_trans = negate_y(negate_x(line))
    if line_trans.get_octant() == "I":
        print(f"5: L0: [({line.A.x}, {line.A.y}), ({line.B.x}, {line.B.y})] {line.get_octant()} {math.degrees(line.get_angle())}, L1: [({line_trans.A.x}, {line_trans.A.y}), ({line_trans.B.x}, {line_trans.B.y})] {line_trans.get_octant()} {math.degrees(line_trans.get_angle())}")

    line_trans = swap_x_with_y(negate_x(line))
    if line_trans.get_octant() == "I":
        print(f"6: L0: [({line.A.x}, {line.A.y}), ({line.B.x}, {line.B.y})] {line.get_octant()} {math.degrees(line.get_angle())}, L1: [({line_trans.A.x}, {line_trans.A.y}), ({line_trans.B.x}, {line_trans.B.y})] {line_trans.get_octant()} {math.degrees(line_trans.get_angle())}")

    line_trans = swap_x_with_y(negate_x(negate_y(line)))
    if line_trans.get_octant() == "I":
        print(f"7: L0: [({line.A.x}, {line.A.y}), ({line.B.x}, {line.B.y})] {line.get_octant()} {math.degrees(line.get_angle())}, L1: [({line_trans.A.x}, {line_trans.A.y}), ({line_trans.B.x}, {line_trans.B.y})] {line_trans.get_octant()} {math.degrees(line_trans.get_angle())}")

    line_trans = swap_x_with_y(negate_y(line))
    if line_trans.get_octant() == "I":
        print(f"8: L0: [({line.A.x}, {line.A.y}), ({line.B.x}, {line.B.y})] {line.get_octant()} {math.degrees(line.get_angle())}, L1: [({line_trans.A.x}, {line_trans.A.y}), ({line_trans.B.x}, {line_trans.B.y})] {line_trans.get_octant()} {math.degrees(line_trans.get_angle())}")

def do_nothing(line: T_LINE):
    return line

def negate_x(line: T_LINE):
    A_x = -line.A.x
    A_y = line.A.y

    B_x = -line.B.x
    B_y = line.B.y

    return T_LINE(Point(A_x, A_y), Point(B_x, B_y))

def negate_y(line: T_LINE):
    A_x = line.A.x
    A_y = -line.A.y

    B_x = line.B.x
    B_y = -line.B.y

    return T_LINE(Point(A_x, A_y), Point(B_x, B_y))

def swap_x_with_y(line: T_LINE):
    A_x = line.A.y
    A_y = line.A.x

    B_x = line.B.y
    B_y = line.B.x

    return T_LINE(Point(A_x, A_y), Point(B_x, B_y))





#l1 = T_LINE(Point(0, 0), Point(10, 5))

p0 = Point(0, 0)

# Create lines and determine octants
print("1'st octant")
line_I = T_LINE(p0, Point(10, 5))
do_all_transformations(line_I)

print("\n2'nd octant")
line_II = T_LINE(p0, Point(5, 10))
do_all_transformations(line_II)

print("\n3'rd octant")
line_III = T_LINE(p0, Point(-5, 10))
do_all_transformations(line_III)

print("\n4'th octant")
line_IV = T_LINE(p0, Point(-10, 5))
do_all_transformations(line_IV)

print("\n5'th octant")
line_V = T_LINE(p0, Point(-10, -5))
do_all_transformations(line_V)

print("\n6'th octant")
line_VI = T_LINE(p0, Point(-5, -10))
do_all_transformations(line_VI)

print("\n7'th octant")
line_VII = T_LINE(p0, Point(5, -10))
do_all_transformations(line_VII)

print("\n8'th octant")
line_VIII = T_LINE(p0, Point(10, -5))
do_all_transformations(line_VIII)
