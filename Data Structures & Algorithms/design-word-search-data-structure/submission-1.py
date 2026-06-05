class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        tmp = self.root
        for c in word:
            if c not in tmp.children:
                tmp.children[c] = TrieNode()
            tmp = tmp.children[c]
        tmp.end = True

    def search(self, word: str) -> bool:
        def dfs(root, j):

            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c==".":
                    for c in cur.children:
                       if dfs(cur.children[c], i+1):
                        return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.end
        return dfs(self.root, 0)


