class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_occ = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            if char in seen:
                continue
            
            while stack and char < stack[-1] and last_occ[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
            
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)
