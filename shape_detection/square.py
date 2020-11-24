from .triangle import get_angle, Point
from . import shape
import numpy as np
import cv2

RIGHT_ANGLE = 90


class Square:
    """Four-sided poligon.\n
    A______B  \r
    |      |  \r
    |      |  \r
    D______C  \r
    """

    def __init__(self, point_a: Point, point_b: Point, point_c: Point, point_d: Point, array: np.ndarray = []):
        """Square formed by four given points."""
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d
        self.array = array

    def __str__(self):
        return (f"{self.point_a} {self.point_b} {self.point_c} {self.point_d}")

    def get_angle_a(self):
        """Angle A°."""
        return get_angle(self.point_a, self.point_b, self.point_d)

    def get_angle_b(self):
        """Angle B°."""
        return get_angle(self.point_b, self.point_c, self.point_a)

    def get_angle_c(self):
        """Angle C°."""
        return get_angle(self.point_c, self.point_d, self.point_b)

    def get_angle_d(self):
        """Angle D°."""
        return get_angle(self.point_d, self.point_a, self.point_c)

    def get_line_ab(self):
        """Line AB length."""
        return shape.get_distance(self.point_a, self.point_b)

    def get_line_bc(self):
        """Line BC length."""
        return shape.get_distance(self.point_b, self.point_c)

    def get_line_cd(self):
        """Line CD length."""
        return shape.get_distance(self.point_c, self.point_d)

    def get_line_ad(self):
        """Line AD length."""
        return shape.get_distance(self.point_a, self.point_d)


def size_approximation(contour, box_threshold=0.40):
    """Compare the size of a bound contour to the contour.

    Args:
        contour (np.ndarray): OpenCV contour.
        box_threshold (float, optional): Approximation threshold. 

    Returns: 
        bool: Whether or not the contours are the same size.

    Notes: See https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/ for  more info.
    """
    (_, _, w, h) = cv2.boundingRect(contour)
    area = w / float(h)
    flag = True if area >= (
        1 - box_threshold) and area <= (1+box_threshold) else False
    return flag


def line_approximation(square: Square, line_threshold: float = 0.30):
    """Compare the size of 4 lines to check if they are the same length.

    Args:
        square (Square): Square object.
        line_threshold (float, optional): Approximation threshold. 

    Returns:
        bool: Whether or not the lines are the same length.
    """

    average = (square.get_line_ab() + square.get_line_bc() +
               square.get_line_cd() + square.get_line_ad())/4

    flag1 = shape.value_approximation(
        square.get_line_ab(), average, value_threshold=line_threshold)
    flag2 = shape.value_approximation(
        square.get_line_bc(), average, value_threshold=line_threshold)
    flag3 = shape.value_approximation(
        square.get_line_cd(), average, value_threshold=line_threshold)
    flag4 = shape.value_approximation(
        square.get_line_ad(), average, value_threshold=line_threshold)

    if(flag1 and flag2 and flag3 and flag4):
        return True
    else:
        return False


def angle_approximation(square: Square, angle_threshold: float = 0.20):
    """ Get the four angles of a square and check if they are roughly the same.

    Args:
        square (Square): Square object.
        angle_threshold (float, optional): Approximation threshold. 

    Returns:
        bool: Whether or not the angles are the same.
    """

    flag1 = shape.value_approximation(
        square.get_angle_a(), RIGHT_ANGLE, value_threshold=angle_threshold)
    flag2 = shape.value_approximation(
        square.get_angle_b(), RIGHT_ANGLE, value_threshold=angle_threshold)
    flag3 = shape.value_approximation(
        square.get_angle_c(), RIGHT_ANGLE, value_threshold=angle_threshold)
    flag4 = shape.value_approximation(
        square.get_angle_d(), RIGHT_ANGLE, value_threshold=angle_threshold)

    if(flag1 and flag2 and flag3 and flag4):
        return True
    else:
        return False


def is_square(contour, arc_threshold=0.05, min_area=300):
    """Find if a contour is a square.

    Rules:
        1 - There must be four corners.
        2 - All four lines must be the same length.
        3 - All four corners must be 90°.
        4 - AB and CD must be horizontal lines.
        5 - AC and BC must be vertical lines.
        6 - The contour must be concave.

    Args: 
        contour (np.ndarray): OpenCV contour.
        arc_threshold (float, optional): Contour arc threshold.
        min_area (float, optional): Minimal area threshold.

    Returns:
        Square: Square object.
    """

    perimeter = cv2.arcLength(contour, True)
    approximation = cv2.approxPolyDP(contour, arc_threshold*perimeter, True)

    rect = cv2.minAreaRect(approximation)
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    if (len(approximation) != 4):
        # Poligon has 4 courners
        return False
    if not size_approximation(approximation):
        # Size Approximation
        return False
    if cv2.contourArea(approximation) < min_area:
        # Min Area
        return False

    # Sort corner of square
    corners = [tuple(approximation[0][0]), tuple(approximation[1][0]),
               tuple(approximation[2][0]), tuple(approximation[3][0])]
    corners.sort(key=lambda p: p[1])

    top_points = corners[2:]
    buttom_points = corners[:2]

    top_points.sort(key=lambda p: p[0])
    buttom_points.sort(key=lambda p: p[0], reverse=True)

    corners = top_points + buttom_points

    point_a = shape.Point(corners[0][0], corners[0][1])
    point_b = shape.Point(corners[1][0], corners[1][1])
    point_c = shape.Point(corners[2][0], corners[2][1])
    point_d = shape.Point(corners[3][0], corners[3][1])

    square = Square(point_a, point_b, point_c, point_d, approximation)

    # print("Corners:", corners)
    # print("top", top_points)
    # print("buttom", buttom_points)
    # print("Square:", square)

    if not shape.value_approximation(square.get_line_ab(), square.get_line_cd(), value_threshold=0.20):
        # Is Horizontal
        return False
    if not shape.value_approximation(square.get_line_ad(), square.get_line_bc(), value_threshold=0.20):
        # Is Vertical
        return False
    if not line_approximation(square):
        # Lines Same Length
        return False
    if not angle_approximation(square):
        # Right Angle
        return False

    return square
