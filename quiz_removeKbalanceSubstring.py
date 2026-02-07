class Solution(object):
    def removeSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Stack stores [character, count]
        stack = []
        
        for c in s:
            # If current char matches top of stack, increment count
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
                
            # Check if we formed a k-balanced substring: k '(' followed by k ')'
            # We trigger check only when we have exactly k ')' at the top
            if c == ')' and stack[-1][1] == k:
                # Check if strictly preceded by at least k '('
                if len(stack) >= 2 and stack[-2][0] == '(' and stack[-2][1] >= k:
                    # Remove the ')' group
                    stack.pop()
                    # Decrement the matching '(' count
                    stack[-1][1] -= k
                    # If '(' count drops to 0, remove the group entirely
                    if stack[-1][1] == 0:
                        stack.pop()
                        
        # Reconstruct the string
        return "".join(c * count for c, count in stack)
