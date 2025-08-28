class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        roots = set(dictionary)

        def replace(word):
            for i in range(1, len(word) + 1):
                if word[:i] in roots:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))
