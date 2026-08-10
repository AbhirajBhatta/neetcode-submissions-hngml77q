class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            if len(w1)>len(w2) and w1[:minLen]==w2[:minLen]:
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
            for nei in adj[char]:
                if dfs(nei):
                    return True
            visited[char] = False
            res.append(char)
        for word in words:
            for c in word:
                if dfs(c):
                    return ""
        res.reverse()
        return "".join(res)
