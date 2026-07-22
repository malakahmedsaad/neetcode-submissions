class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = []
        res = []

        def backtrack(open, close):
            if open == close == n:
                return res.append("".join(s))

            if open < n:
                s.append("(")
                backtrack(open + 1, close)
                s.pop()

            if close < open:
                s.append(")")
                backtrack(open, close+1)
                s.pop()

        backtrack(0,0)
        return res

