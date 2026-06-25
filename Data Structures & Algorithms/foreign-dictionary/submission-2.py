class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            if w1[:minLen]==w2[:minLen] and len(w1)>len(w2):
                return ""
            
            for c in range(minLen):
                if w1[c]!=w2[c]:
                    adj[w1[c]].add(w2[c])
                    break
        visited = {}
        res = []
        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True
            for neiChar in adj[char]:
                if dfs(neiChar):
                    return True
            visited[char] = False
            res.append(char)
        for c in adj:
            if dfs(c):
                return ""
        return "".join(reversed(res))