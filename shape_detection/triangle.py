from .shape import Point, get_distance
import math


class Triange:
    def __init__(self, point_a: Point, point_b: Point, point_c: Point):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def __str__(self):
        return (f"{self.point_a} {self.point_b} {self.point_c}")

    def get_angle_A(self):
        return get_angle(self.point_a, self.point_b, self.point_c)

    def get_angle_B(self):
        return get_angle(self.point_b, self.point_c, self.point_a)

    def get_angle_C(self):
        return get_angle(self.point_c, self.point_a, self.point_b)

    def get_side_a(self):
        return get_distance(self.point_b, self.point_c)

    def get_side_b(self):
        return get_distance(self.point_a, self.point_c)

    def get_side_c(self):
        return get_distance(self.point_a, self.point_b)


def get_angle(point_a: Point, point_b: Point, point_c: Point):
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
    a = get_distance(point_b, point_c)
    b = get_distance(point_a, point_c)
    c = get_distance(point_a, point_b)

    cosA = (math.pow(b, 2) + (math.pow(c, 2)) - (math.pow(a, 2))) / (2*b*c)
    angle = math.degrees(math.acos(cosA))

    return angle
