class Solution:        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resmap = defaultdict(list)
        for s in strs:
            key = [0 for i in range(26)]

            for c in s:
                key[ord(c)-ord("a")] += 1

            resmap[tuple(key)].append(s)
        
        return list(resmap.values())
        
            

        