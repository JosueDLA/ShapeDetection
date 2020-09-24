import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return(f"({self.x}, {self.y})")


def get_distance(point_a, point_b):
    """
    Get the distance between two points
    Distance = sqrt ( (x1-x2)^2 + (y1-y2)^2 )
    Source: https://www.mathsisfun.com/algebra/distance-2-points.html
    """

    distance = math.sqrt((math.pow((A[0]-B[0]), 2) + math.pow((A[1]-B[1]), 2)))
    return distance


def position_approximation(A, B, position_threshold=0.30):
    """
    Compare positions of two points to check if they are orizontal or vertical lines
    """
    position = a/float(b)
    flag = True if position >= (
        1-position_threshold) and position <= (1+position_threshold) else False
    return flag


def remove_parent_contour(contours, hierarchy):
    """
    Remove all contours with childs
    """
    # hierarchy [next, previous, firstChild, parent]
    new_contour = []
    new_hierarchy = []

    for c in zip(contours, hierarchy):
        if c[1][2] == -1:
            new_contour.append(c[0])
            new_hierarchy.append(c[1])
    new_hierarchy = np.array(new_hierarchy)
    return new_contour, new_hierarchy


def remove_child_contour(contours, hierarchy):
    pass
