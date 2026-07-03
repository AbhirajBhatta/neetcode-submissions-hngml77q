class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(endWord)
        adj = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i+1:]
                adj[pat].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        path = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return path
                
                for j in range(len(word)):
                    pat = word[:j] + "*" + word[j+1:]
                    for nei in adj[pat]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            path+=1
        return 0
