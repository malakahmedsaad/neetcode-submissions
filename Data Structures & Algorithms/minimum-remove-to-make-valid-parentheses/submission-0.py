class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cnt = 0
        arr = []
        for c in s:
            if c == "(":
                cnt += 1
                arr.append(c)
            elif c == ")" and cnt > 0:
                cnt -= 1
                arr.append(c)
            elif c != ")":
                arr.append(c)
            
        arr_updated = []
        for c in reversed(arr):
            if c == "(" and cnt > 0:
                cnt -= 1
            else:
                arr_updated.append(c)

        return "".join(reversed(arr_updated))