import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return(f"({self.x}, {self.y})")


def get_distance(point_A: Point, point_B: Point):
    """
    Get the distance between two points
    Distance = sqrt ( (x1-x2)^2 + (y1-y2)^2 )
    Source: https://www.mathsisfun.com/algebra/distance-2-points.html
    """

    distance = math.sqrt(
        (math.pow((point_A.x-point_B.x), 2) + math.pow((point_A.y-point_B.y), 2)))
    return distance


def value_approximation(point_a, point_b, value_threshold):
    """
    Compare two numbers to check if they are roughly the same
    """
    position = point_a/float(point_b)
    flag = True if position >= (
        1-position_threshold) and position <= (1+position_threshold) else False
    return flag
