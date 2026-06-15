class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        res = 1
        nodesMap = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nodesMap[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word==endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in nodesMap[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            res+=1
        return 0
