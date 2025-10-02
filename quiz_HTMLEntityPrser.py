class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        mapping = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }
        
        for k, v in mapping.items():
            text = text.replace(k, v)
        
        return text
