#### [ kadane.py ]( kadane.py )

```python

def kadane(array):
    msum = float("-inf")
    csum = float("-inf")
    for i in array:
        csum = max(i, csum + i)
        msum = max(msum, csum)
        print(csum, msum)
    return msum

if __name__ == "__main__":
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert kadane(array) == 6 # with [4, -1, 2, 1]

    # max(-2, 0-2) = -2, -2 
    # max(1, 1-2) = 1, 1
    # max(-3, -3+1 ) = -2, 1
    # max(4, 4-2) = 4, 4 
    # max(-1, -1+4) = 3, 4
    # max(2, 2+3 ) = 5, 5
    # max(1, 1+5) = 6, 6
    # max(-5, -5+6) = 1, 6
    # max(4, 4+1) = 5, 6


```



