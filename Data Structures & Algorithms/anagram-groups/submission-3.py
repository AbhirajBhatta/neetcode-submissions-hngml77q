class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c)-ord("a")] += 1

            tup = tuple(key)
            if tup in res:
                res[tup].append(s)
            else:
                res[tup] = [s]
        return list(res.values())