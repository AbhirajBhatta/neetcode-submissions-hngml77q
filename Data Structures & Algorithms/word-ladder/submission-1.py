class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nodesMap = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nodesMap[pattern].append(word)
        
        visited = set()
        visited.add(beginWord)
        q = deque([beginWord])

        dist = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word ==endWord:
                    return dist
                for j in range(len(word)):
                    pat = word[:j] + "*" + word[j+1:]
                    for nei in nodesMap[pat]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            dist+=1
        return 0