class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        adj = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i+1:]
                adj[pat].append(word)
        path = 0
        q = deque([beginWord])
        visited = set([beginWord])

        while q:
            path+=1
            for i in range(len(q)):
                word = q.popleft()
                if word==endWord:
                    return path
                visited.add(word)
                for i in range(len(word)):
                    pat = word[:i] + "*" + word[i+1:]
                    for nei in adj[pat]:
                        if nei not in visited:
                            q.append(nei)
                            
                
        return 0