import unittest
import collections
import heapq


def topKFrequent(words, k):
    counter = collections.Counter(words)
    maxHeap = []
    for wd, ct in counter.items():
        heapq.heappush(maxHeap, (-ct, wd))

    res = []
    for _ in range(k):
        _, wd = heapq.heappop(maxHeap)
        res.append(wd)

    return res


class TopKFrequentWordsTest(unittest.TestCase):

    def test_top_k_frequent_words(self):
        self.assertCountEqual(
            topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2),
            ["i", "love"])
        self.assertCountEqual(
            topKFrequent([
                "the", "day", "is", "sunny", "the", "the", "the", "sunny",
                "is", "is"
            ], 4), ["the", "is", "sunny", "day"])


if __name__ == "__main__":
    unittest.main()
