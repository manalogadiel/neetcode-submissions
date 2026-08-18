class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = defaultdict(list)

        for i in strs:
            z = [0] * 26
            for j in i:
                z[ord(j) - ord("a")] += 1
            x[tuple(z)].append(i)
        return list(x.values())