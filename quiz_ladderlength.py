from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
            
        q = deque([(beginWord, 1)])
        
        while q:
            word, length = q.popleft()
            
            if word == endWord:
                return length
                
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        q.append((next_word, length + 1))
                        
        return 0
