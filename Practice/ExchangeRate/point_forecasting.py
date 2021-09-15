
def line_by_least_squares_method(points):
    matrix = [[0, 0, 0], [0, 0, 0]]
    for i in range(len(points)):
        matrix[0][0] += points[i][1]**2
        matrix[0][1] += points[i][1]
        matrix[1][0] += points[i][1]
        matrix[1][1] += 1
        matrix[0][2] += int(points[i][0]) * points[i][1]
        matrix[1][2] += int(points[i][0])

    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det_k = matrix[0][2] * matrix[1][1] - matrix[0][1] * matrix[1][2]
    det_b = matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]
    k = det_k / det
    b = det_b / det

    return k, b



def forecast_next_point(k, b, x):
    return x * k + b
