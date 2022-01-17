import unittest


# O(n * m * 4^len(word)) | O(n * m) space
def word_search(board, word):
    rows, cols = len(board), len(board[0])
    visited = set()
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0, board, visited, word):
                return True
    return False


def dfs(r, c, i, board, visited, word):
    # if i is equal to len(word) it means that
    # we have found all characters
    if i == len(word):
        return True
    rows, cols = len(board), len(board[0])
    # if current row or column is out boundaries return False
    if not (0 <= r < rows) or not (0 <= c < cols):
        return False
    # if current row and columns are visited return False
    if (r, c) in visited:
        return False
    # if character at current row and column is diff
    # to word[i] return False
    if board[r][c] != word[i]:
        return False

    visited.add((r, c))
    res = (
        dfs(r, c - 1, i + 1, board, visited, word)
        or dfs(r, c + 1, i + 1, board, visited, word)  # left
        or dfs(r - 1, c, i + 1, board, visited, word)  # right
        or dfs(r + 1, c, i + 1, board, visited, word)  # up  # down
    )
    visited.remove((r, c))
    print(r, c, res, word[i])
    return res


class WordSearchTest(unittest.TestCase):
    def test_word_search(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        self.assertEqual(word_search(board, word), True)
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "SEE"
        self.assertEqual(word_search(board, word), True)
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCB"
        self.assertEqual(word_search(board, word), False)


if __name__ == "__main__":
    unittest.main()
