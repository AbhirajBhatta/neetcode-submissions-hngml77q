class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)

        for s in strs:
            hashed = [0]*26

            for c in s:
                idx = ord(c) - ord("a")
                hashed[idx] += 1
            buckets[tuple(hashed)].append(s)
        return list(buckets.values())