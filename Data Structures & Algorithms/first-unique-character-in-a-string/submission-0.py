class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = defaultdict(int)
        for c in s:
            hm[c] += 1

        for i, c in enumerate(s):
            if hm[c] == 1:
                return i
        return -1

