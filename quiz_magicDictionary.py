class MagicDictionary(object):

    def __init__(self):
        self.words = set()

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        self.words = set(dictionary)

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        for i, ch in enumerate(searchWord):
            for k in range(26):
                c = chr(ord('a') + k)
                if c == ch:
                    continue
                candidate = searchWord[:i] + c + searchWord[i+1:]
                if candidate in self.words:
                    return True
        return False
