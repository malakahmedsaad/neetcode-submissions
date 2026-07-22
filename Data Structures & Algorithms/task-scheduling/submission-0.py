class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxfreq = max(freq.values())
        maxcount = 0
        for i in freq.values():
            if i == maxfreq:
                maxcount +=1

        return max(len(tasks), ((maxfreq-1) * (n+1) + maxcount))


        