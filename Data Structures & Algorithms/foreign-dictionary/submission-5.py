class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = defaultdict(set)
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            minLen = min(len(word1), len(word2))

            if word1[:minLen]==word2[:minLen] and len(word1)>len(word2):
                return ""
            
            for i in range(minLen):
                if word1[i]!=word2[i]:
                    adj[word1[i]].add(word2[i])
                    break
        res = []
        visited = {} # {true is cycle, false if just normally visited}
        def postOrderDFS(node):
            if node in visited:
                return visited[node]
            visited[node] = True
            for nei in adj[node]:
                if postOrderDFS(nei):
                    return True
            
            visited[node] = False
            res.append(node)
            return False
        for word in words:
            for c in word:
                if postOrderDFS(c):
                    return ""
        res.reverse()
        return "".join(res)


