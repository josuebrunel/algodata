def productSum(array):
    return product(array, 1)

def product(array, m):
    psum = 0
    for e in array:
        if isinstance(e, (list,)):
            psum += m * product(e, m+1)
        else:
            psum += m * e
    print(m, " * ", array, " => ", psum)
    return psum

if __name__ == "__main__":
    array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    # 5 + 2 * 2 (7 - 1) + 3 * 2 ( 6 * 2 (-13 + 8) + 4)
    assert productSum(array) == 12
