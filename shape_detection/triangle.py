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
    a = get_distance(B, C)
    b = get_distance(A, C)
    c = get_distance(A, B)

    cosA = (math.pow(b, 2) + (math.pow(c, 2)) - (math.pow(a, 2))) / (2*b*c)
    angle = math.degrees(math.acos(cosA))

    return angle
