import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return(f"({self.x}, {self.y})")


def get_distance(point_a: Point, point_b: Point):
    """
    Get the distance between two points
    Distance = sqrt ( (x1-x2)^2 + (y1-y2)^2 )
    Source: https://www.mathsisfun.com/algebra/distance-2-points.html
    """

    distance = math.sqrt(
        (math.pow((point_a.x-point_b.x), 2) + math.pow((point_a.y-point_b.y), 2)))
    return distance


def value_approximation(point_a, point_b, value_threshold):
    """
    Compare two numbers to check if they are roughly the same
    """
    position = point_a/float(point_b)
    flag = True if position >= (
        1-value_threshold) and position <= (1+value_threshold) else False
    return flag
