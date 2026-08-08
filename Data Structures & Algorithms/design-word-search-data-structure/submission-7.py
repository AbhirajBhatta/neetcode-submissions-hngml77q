class TrieNode:
    def __init__(self):
        self.neighbors = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.neighbors:
                cur.neighbors[c] = TrieNode()
            cur = cur.neighbors[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            for j in range(i, len(word)):
                c = word[j]
                if c==".":
                    for nei in node.neighbors:
                        if dfs(node.neighbors[nei], j+1):
                            return True
                    return False
                else:
                    if c not in node.neighbors:
                        return False
                    node = node.neighbors[c]
            return node.end
        return dfs(self.root, 0)

                
