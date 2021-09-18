
def line_by_least_squares_method(points: [[]]):
    matrix = [[0, 0, 0], [0, 0, 0]]
    for i in range(len(points[0])):
        matrix[0][0] += points[0][i]**2
        matrix[0][1] += points[0][i]
        matrix[1][0] += points[0][i]
        matrix[1][1] += 1
        matrix[0][2] += float(points[1][i]) * float(points[0][i])
        matrix[1][2] += float(points[1][i])

    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det_k = matrix[0][2] * matrix[1][1] - matrix[0][1] * matrix[1][2]
    det_b = matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]
    k = det_k / det
    b = det_b / det

    return k, b
