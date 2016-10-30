def max_height(boxes):
    """ Calculates the maximum height of a stack of boxes.
    Boxes are orientated width x depth x height and are not rotatable.
    Returns the maximum height of a stack. """

    # Sort the boxes by floor area.
    boxes_sorted = sorted(boxes, key=lambda x: x[0] * x[1])
    num_boxes = len(boxes)

    # Setup a array with all boxes heights.
    max_height = []
    for box in boxes_sorted:
        max_height.append(box[2])

    for i in range(num_boxes):
        for j in range(0, i):
            # For all boxes test if a box with smaller area fits ontop
            # and thereby creating a new maximum height.
            if (boxes_sorted[i][0] >= boxes_sorted[j][0]) and \
               (boxes_sorted[i][1] >= boxes_sorted[j][1]) and \
               (max_height[i] < max_height[j] + boxes_sorted[i][2]):
                max_height[i] = max_height[j] + boxes_sorted[i][2]


    return max(max_height)

if __name__ == '__main__':
    # Individual box dimensions (width, depth, height) tuple
    boxes = [ (7, 7, 7), (10, 4, 7), (4, 4, 1), (2, 2, 2), (3, 4, 5), (6, 8, 5), (6, 1, 9), (8, 8, 4), (1, 1, 9), (10, 4, 6), (6, 2, 5), (2, 8, 1), (5, 1, 3), (8, 2, 6), (1, 8, 9), (10, 2, 4), (2, 1, 1), (9, 6, 8), (1, 4, 6), (7, 2, 8) ]
    print max_height(boxes)
