class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output =[]
        map = {}
        for i in nums:
            map[i] = map.get(i,0) + 1

        for i, c in map.items():
            output.append([c, i])
        output.sort()

        res = []
        while len(res) < k:
            res.append(output.pop()[1])
        return res