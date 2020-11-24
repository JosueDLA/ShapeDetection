from .shape import Point, get_distance
import math


class Triangle:
    """Three-sided Poligon.
        /C\       \r
       /   \      \r
     b/     \\a   \r
     /       \    \r
    A__________B  \r
         c
    """

    def __init__(self, point_a: Point, point_b: Point, point_c: Point):
        """Triangle formed by 3 given points.

        Args: 
            point_a (Point): Point A
            point_b (Point): Point B
            point_c (Point): Point C
        """
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def __str__(self):
        return (f"{self.point_a} {self.point_b} {self.point_c}")

    @property
    def angle_a(self):
        """Angle A° (alpha)."""
        return self.get_angle(self.point_a, self.point_b, self.point_c)

    @property
    def angle_b(self):
        """Angle B° (beta)."""
        return self.get_angle(self.point_b, self.point_c, self.point_a)

    @property
    def angle_c(self):
        """Angle C° (gama)."""
        return self.get_angle(self.point_c, self.point_a, self.point_b)

    @property
    def side_a(self):
        """Line a length"""
        return get_distance(self.point_b, self.point_c)

    @property
    def side_b(self):
        """Line b length"""
        return get_distance(self.point_a, self.point_c)

    @property
    def side_c(self):
        """Line c length"""
        return get_distance(self.point_a, self.point_b)

    @staticmethod
    def get_angle(point_a: Point, point_b: Point, point_c: Point):
        """Get the angle between three points.

        cos(A°) = (b^2 + c^2 - a^2) / 2bc

        A° = cos^-1((b^2 + c^2 - a^2) / 2bc)

        Args:
            point_a (Point): Point A
            point_b (Point): Point B
            point_c (Point): Point C

        Returns:
            float: angle at A° (alpha) formed by the triangle ABC

        Notes: 
            For more information go to:
            https://www.mathsisfun.com/algebra/trig-solving-sss-triangles.html
            https://www.mathsisfun.com/algebra/trig-cosine-law.html
        """
        a = get_distance(point_b, point_c)
        b = get_distance(point_a, point_c)
        c = get_distance(point_b, point_a)

        cosA = (math.pow(b, 2) + (math.pow(c, 2)) - (math.pow(a, 2))) / (2*b*c)
        angle = math.degrees(math.acos(cosA))

        return angle
