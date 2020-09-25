class shape_contour:
    def __init__(self, contours, hierarchy):
        self.contours = contours
        self.hierarchy = hierarchy[0]

    def __str__(self):
        return self.contours, self.hierarchy


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
