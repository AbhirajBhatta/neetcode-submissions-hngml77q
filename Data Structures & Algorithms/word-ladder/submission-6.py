class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        adj = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pat = word[:j] + "*" + word[j+1:]
                adj[pat].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word==endWord:
                    return res
                for j in range(len(word)):
                    pat = word[:j] + "*" + word[j+1:]
                    for nei in adj[pat]:
                        if nei not in visited:
                            visited.add(word)
                            q.append(nei)
            res+=1
        return 0


