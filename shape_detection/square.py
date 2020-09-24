import numpy as np
import cv2


def get_distance(A, B):
    """
    Get the distance between two points
    Distance = sqrt ( (x1-x2)^2 + (y1-y2)^2 )
    Source: https://www.mathsisfun.com/algebra/distance-2-points.html
    """

    distance = math.sqrt((math.pow((A[0]-B[0]), 2) + math.pow((A[1]-B[1]), 2)))
    return distance


def get_angle(A, B, C):
    """
    Get the angle between three points
    Returns the angle at A formed by the triangle ABC

    cos(A) = (b^2 + c^2 - a^2) / 2bc
    A = cos^-1((b^2 + c^2 - a^2) / 2bc)

        /C\
       /   \
     b/     \a
     /       \
    A_________C
         c

    Source: https://www.mathsisfun.com/algebra/trig-solving-sss-triangles.html
            https://www.mathsisfun.com/algebra/trig-cosine-law.html
    """
    a = getDistance(B, C)
    b = getDistance(A, C)
    c = getDistance(A, B)

    cosA = (math.pow(b, 2) + (math.pow(c, 2)) - (math.pow(a, 2))) / (2*b*c)
    angle = math.degrees(math.acos(cosA))

    return angle


def remove_parent_contour:
    """
    Remove all contours with childs
    """
    # hierarchy [next, previous, firstChild, parent]
    newContour = []
    newHierarchy = []

    for c in zip(contours, hierarchy):
        if c[1][2] == -1:
            newContour.append(c[0])
            newHierarchy.append(c[1])
    newHierarchy = np.array(newHierarchy)
    return newContour, newHierarchy


def is_square:
    """
    Find the aspect ratio of the box
    Compare the asperct ratio of the box to a square with a threshold
    Source: https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
    """

    (_, _, w, h) = cv2.boundingRect(approx)
    area = w / float(h)
    flag = True if area >= (
        1-boxThreshold) and area <= (1+boxThreshold) else False
    return flag
