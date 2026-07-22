class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            unique = set()
            for j in range (i, len(s)):
                if s[j] in unique:
                    break
                unique.add(s[j])
            res = max(res, len(unique))
        return res

        