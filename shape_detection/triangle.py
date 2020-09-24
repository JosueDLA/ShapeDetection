import shape
import math


class triange:
    def __init__(self, A: shape.Point, B: shape.Point, C: shape.Point):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        pass

    def get_angle_A(self):
        return get_angle(self.A, self.B, self.C)

    def get_angle_B(self):
        return get_angle(self.B, self.C, self.A)

    def get_angle_C(self):
        return get_angle(self.C, self.A, self.B)

    def get_side_a(self):
        return shape.get_distance(self.B, self.C)

    def get_side_b(self):
        return shape.get_distance(self.A, self.C)

    def get_side_c(self):
        return shape.get_distance(self.A, self.B)


def get_angle(A: shape.Poin, B: shape.Poin, C: shape.Poin):
    """
    Get the angle between three points
    Returns the angle at Aº formed by the triangle ABC

    cos(Aº) = (b^2 + c^2 - a^2) / 2bc
    Aº = cos^-1((b^2 + c^2 - a^2) / 2bc)

        /C\
       /   \
     b/     \a
     /       \
    A_________B
         c

    Source: https://www.mathsisfun.com/algebra/trig-solving-sss-triangles.html
            https://www.mathsisfun.com/algebra/trig-cosine-law.html
    """
    a = shape.get_distance(B, C)
    b = shape.get_distance(A, C)
    c = shape.get_distance(A, B)

    cosA = (math.pow(b, 2) + (math.pow(c, 2)) - (math.pow(a, 2))) / (2*b*c)
    angle = math.degrees(math.acos(cosA))

    return angle
