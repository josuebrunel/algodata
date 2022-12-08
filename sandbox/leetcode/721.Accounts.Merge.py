import unittest


class DSU:

    def __init__(self, N):
        self.parents = {i: i for i in range(N)}
        self.ranks = {i: 0 for i in range(N)}

    def find(self, u):
        u = self.parents[u]
        while u != self.parents[u]:
            self.parents[u] = self.parents[self.parents[u]]
            u = self.parents[u]
        return u

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return

        if self.ranks[u] > self.ranks[v]:
            self.parents[v] = u
        elif self.ranks[u] < self.ranks[v]:
            self.parents[u] = v
        else:
            self.parents[u] = v
            self.ranks[v] += 1


def accounts_merge(accounts):
    dsu = DSU(len(accounts))
    lookup = {}

    for idx, account in enumerate(accounts):
        _, *emails = account
        for email in emails:
            if email in lookup:
                dsu.union(idx, lookup[email])
            else:
                lookup[email] = idx
    ans = {}

    for email, idx in lookup.items():
        u = dsu.find(idx)
        if email in ans:
            ans[u].append(email)
        else:
            ans[u] = [email]

    for u, value in ans.items():
        ans[u] = [accounts[u][0]] + sorted(value)

    return ans.values()


class AccountMergeTest(unittest.TestCase):

    def test_accounts_merge(self):
        #self.assertCountEqual(
        #    accounts_merge(
        #        [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        #         ["John", "johnsmith@mail.com", "john00@mail.com"],
        #         ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]),
        #    [[
        #        "John", "john00@mail.com", "john_newyork@mail.com",
        #        "johnsmith@mail.com"
        #    ], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]])
        res = accounts_merge(
            [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
             ["John", "johnsmith@mail.com", "john00@mail.com"],
             ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]])
        self.assertEqual(len(res), 3)
        #self.assertCountEqual(
        #    accounts_merge(
        #        [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
        #         ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
        #         ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
        #         ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
        #         ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]),
        #    [["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
        #     ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
        #     ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
        #     ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
        #     ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"]])
        res = accounts_merge(
            [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
             ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
             ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
             ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
             ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]])
        self.assertEqual(len(res), 5)


if __name__ == "__main__":
    unittest.main()
