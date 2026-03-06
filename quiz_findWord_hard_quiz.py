class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the full word at the leaf node

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # 1. Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
            
        rows, cols = len(board), len(board[0])
        res = []

        # 2. Define Backtracking function
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            
            curr_node = node.children[char]
            # If we found a word, add it to results and clear it to avoid duplicates
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None 
            
            # Mark the cell as visited using a placeholder
            board[r][c] = "#"
            
            # Explore neighbors: up, down, left, right
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, curr_node)
            
            # Backtrack: restore the cell's original value
            board[r][c] = char
            
            # Optimization: prune the Trie leaf nodes
            if not curr_node.children:
                node.children.pop(char)

        # 3. Start DFS from every cell on the board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
                
        return res
