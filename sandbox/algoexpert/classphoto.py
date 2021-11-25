def classPhotos(a, b):
    a.sort()
    b.sort()
    firstRow = True if a[0] > b[0] else False

    for i in range(1, len(a)):
        if (a[i] >= b[i]) is not firstRow:
            return False
    return True


if __name__ == "__main__":
    a = [5, 8, 1, 3, 4]
    b = [6, 9, 2, 4, 5]
    assert classPhotos(a, b) == True
    a = [6, 9, 2, 4, 4]
    b = [5, 8, 1, 3, 4]
    assert classPhotos(a, b) == True
    assert classPhotos([6], [6]) == False
