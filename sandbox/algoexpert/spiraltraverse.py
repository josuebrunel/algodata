def spiralTraverse(matrix):
    result = []
    return result


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 15, 16, 6],
        [10, 9, 8, 7],
    ]
    assert spiralTraverse(matrix) == list(range(1, 17))
