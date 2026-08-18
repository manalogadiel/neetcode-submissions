class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        for i in strs:
            c = [0] * 26
            for s in i:
                c[ord(s) - ord('a')] += 1
            g[tuple(c)].append(i)
        return list(g.values())
        