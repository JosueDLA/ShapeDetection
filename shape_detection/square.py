import numpy as np
import cv2


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
