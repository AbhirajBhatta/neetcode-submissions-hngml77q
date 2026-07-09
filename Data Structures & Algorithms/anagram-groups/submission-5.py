class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            hashed = [0]*26
            for c in s:
                idx = int(ord(c) - ord("a"))
                hashed[idx] += 1
            groups[tuple(hashed)].append(s)
        return list(groups.values())
        