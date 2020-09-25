from .triangle import get_angle, Point
from . import contour, shape
import numpy as np
import cv2

RIGHT_ANGLE = 90


class Square:
    def __init__(self, point_a: Point, point_b: Point, point_c: Point, point_d: Point):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d

    def __str__(self):
        return (f"{self.point_a} {self.point_b} {self.point_c} {self.point_d}")

    def get_angle_a(self):
        return get_angle(self.point_a, self.point_b, self.point_d)

    def get_angle_b(self):
        return get_angle(self.point_b, self.point_c, self.point_a)

    def get_angle_c(self):
        return get_angle(self.point_c, self.point_d, self.point_b)

    def get_angle_d(self):
        return get_angle(self.point_d, self.point_a, self.point_c)

    def get_line_ab(self):
        return shape.get_distance(self.point_a, self.point_b)

    def get_line_bc(self):
        return shape.get_distance(self.point_b, self.point_c)

    def get_line_cd(self):
        return shape.get_distance(self.point_c, self.point_d)

    def get_line_ad(self):
        return shape.get_distance(self.point_a, self.point_d)


def size_approximation(contour, box_threshold=0.40):
    """
    Compare the size of a bound contour to the contour
    Source: https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
    """
    (_, _, w, h) = cv2.boundingRect(contour)
    area = w / float(h)
    flag = True if area >= (
        1 - box_threshold) and area <= (1+box_threshold) else False
    return flag


def line_approximation(square, line_threshold=0.30):
    """
    Compare the size of 4 lines to check if they are the same length
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


def angle_approximation(square, angle_threshold=0.20):
    """
    Get the four angles of a square and check if they are roughly the same
    """

    print(square.get_angle_a(), RIGHT_ANGLE)

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
    """
    Find if a contour is a square
    Rules:
    1 - There must be four corners
    2 - All four lines must be the same length
    3 - All four corners must be 90°
    4 - AB and CD must be horizontal lines
    5 - AC and BC must be vertical lines
    6 - The contour must be concave

    A______B
    |      |
    |      |
    D______C
    """

    perimeter = cv2.arcLength(contour, True)
    approximation = cv2.approxPolyDP(contour, arc_threshold*perimeter, True)

    rect = cv2.minAreaRect(approximation)
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    if (len(approximation) != 4):
        return False
    if not size_approximation(approximation):
        return False
    if cv2.contourArea(approximation) < min_area:
        return False

    # Sort corner of square
    print(type(approximation))
    corners = [tuple(approximation[0][0]), tuple(approximation[1][0]),
               tuple(approximation[2][0]), tuple(approximation[3][0])]
    corners.sort(key=lambda x: x[0] + (x[1]/2))

    # Sort returns square BDAC
    point_a = shape.Point(corners[1][0], corners[1][1])
    point_b = shape.Point(corners[3][0], corners[3][1])
    point_c = shape.Point(corners[2][0], corners[2][1])
    point_d = shape.Point(corners[0][0], corners[0][1])

    square = Square(point_a, point_b, point_c, point_d)

    print(square)

    if True:
        # Is Horizontal
        pass
    if True:
        # Is Vertical
        pass
    if not line_approximation(square):
        # Lines Same Length
        return False
    if not angle_approximation(square):
        # Right Angle
        return False

    return True
