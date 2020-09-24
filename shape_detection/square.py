import numpy as np
import cv2


class Square:
    def __init__(self, point_a: Point, point_b: Point, point_c: Point, point_d: Point):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d

    def __str__(self):
        return (f"{self.point_a} {self.point_b} {self.point_c} {self.poit_d}")


def is_square(approx, box_threshold=0.40):
    """
    Find the aspect ratio of the box
    Compare the asperct ratio of the box to a square with a threshold
    Source: https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
    """

    (_, _, w, h) = cv2.boundingRect(approx)
    area = w / float(h)
    flag = True if area >= (
        1 - bos_threshold) and area <= (1+bos_threshold) else False
    return flag
