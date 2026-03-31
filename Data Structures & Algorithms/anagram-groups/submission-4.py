class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)

        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c)- ord("a")] += 1
            k = tuple(key)
            buckets[k].append(s)
        return list(buckets.values())