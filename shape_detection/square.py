from .triangle import get_angle, Point
from . import contour
import numpy as np
import cv2


class Square:
    def __init__(self, point_a: Point, point_b: Point, point_c: Point, point_d: Point):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d

    def __str__(self):
        return (f"{self.point_a} {self.point_b} {self.point_c} {self.point_d}")

    def get_angle_a(self):
        print(self.point_a, self.point_b, self.point_d)
        return get_angle(self.point_a, self.point_b, self.point_d)

    def get_angle_b(self):
        return get_angle(self.point_b, self.point_c, self.point_a)

    def get_angle_c(self):
        return get_angle(self.point_c, self.point_d, self.point_b)

    def get_angle_d(self):
        return get_angle(self.point_d, self.point_a, self.point_c)


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


def line_approximation(square, angle_threshold=0.2):
    """
    Compare the size of 4 lines to check if they are the same length
    """
    RIGHT_ANGLE = 90

    flag1 = position_approximation(
        square.get_angle_a, RIGHT_ANGLE, position_threshold=angle_threshold)
    flag2 = position_approximation(
        square.get_angle_b, RIGHT_ANGLE, position_threshold=angle_threshold)
    flag3 = position_approximation(
        square.get_angle_c, RIGHT_ANGLE, position_threshold=angle_threshold)
    flag4 = position_approximation(
        square.get_angle_d, RIGHT_ANGLE, position_threshold=angle_threshold)

    if(flag1 and flag2 and flag3 and flag4):
        return True
    else:
        return False
    pass


def angle_approximation():
    """
    Get the four angles of a square and check if they are roughly the same
    """
    pass


def is_square():
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
    pass
