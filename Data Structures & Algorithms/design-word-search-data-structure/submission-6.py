
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.end=True
    def search(self, word: str) -> bool:
        def dfs(node, i):
            cur = node
            for j in range(i, len(word)):
                c = word[j]
                if c==".":
                    for c in cur.children:
                        if dfs(cur.children[c], j+1):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.end
        return dfs(self.root, 0)


                
