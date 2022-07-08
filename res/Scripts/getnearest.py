def getNearest(index):
    returning = [[[index[0] - 1, index[1] - 1], [index[0] - 1, index[1]], [index[0] - 1, index[1] + 1]],
                 [[index[0], index[1] - 1], [index[0], index[1]], [index[0], index[1] + 1]],
                 [[index[0] + 1, index[1] - 1], [index[0] + 1, index[1]], [index[0] + 1, index[1] + 1]]]
    return returning
