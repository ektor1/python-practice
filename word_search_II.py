# time: m * n * 4 ^ k: dimensions of the matrix * 4 directions we can take ^ max length of a word
# space: s - the sum of length of the words


class trieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = ""

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
               cur.children[c] = trieNode()
            cur = cur.children[c]
        cur.isWord = True
        cur.word = word

def findWords(board, words):
    root = trieNode()

    # Create a Trie with the words given
    for word in words:
        root.addWord(word)


    ROWS = len(board)
    COLS = len(board[0])
    path, res = set(), set()

    def dfs(r, c, node):
        if node.isWord == True:
            res.add(node.word)

        if (min(r, c) < 0 or 
            r == ROWS or c == COLS or
            (r, c) in path or
            board[r][c] not in node.children):
            return 
        
        path.add((r, c))
        node = node.children[board[r][c]]
        dfs(r + 1, c, node)  
        dfs(r - 1, c, node) 
        dfs(r, c + 1, node)
        dfs(r, c - 1, node)
             
        path.remove((r, c))

    for r in range(ROWS):
        for c in range(COLS):
            dfs(r, c, root)

    return list(res)

if __name__ == "__main__":
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]

    print(findWords(board, words))
