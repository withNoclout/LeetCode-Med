class TrieNode(object):

    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary(object):

    def __init__(self):
        
        self.root = TrieNode()
    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root 
        for ch in word : 
            node = node.children.setdefault(ch, TrieNode())
        node.end = True 
            

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(node , i ) :
            if i == len(word) :
                return node.end 
            ch = word[i] 
            if ch == '.' : 
                for nxt in node.children.values() : 
                    if dfs(nxt , i + 1):
                        return True
                return False 
            if ch not in node.children : 
                return False 
            return dfs(node.children[ch] , i +1 ) 
        return dfs( self.root , 0 )



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
