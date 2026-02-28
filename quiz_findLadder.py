from collections import defaultdict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
            
        layer = {beginWord}
        parents = defaultdict(list)
        found = False
        
        while layer and not found:
            wordSet -= layer
            next_layer = set()
            
            for word in layer:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet:
                            next_layer.add(new_word)
                            parents[new_word].append(word)
                            if new_word == endWord:
                                found = True
            layer = next_layer
            
        res = []
        if found:
            def dfs(word, path):
                if word == beginWord:
                    res.append(path[::-1])
                    return
                for p in parents[word]:
                    dfs(p, path + [p])
                    
            dfs(endWord, [endWord])
            
        return res
