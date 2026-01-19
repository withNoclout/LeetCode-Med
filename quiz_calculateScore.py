class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def calculateScore(self, instructions, values):
        """
        :type instructions: List[str]
        :type values: List[int]
        :rtype: int
        """
        n = len(instructions)
        visited = [False] * n
        score = 0
        i = 0
        
        while 0 <= i < n and not visited[i]:
            visited[i] = True
            if instructions[i] == "add":
                score += values[i]
                i += 1
            else:
                # instructions[i] == "jump"
                i += values[i]
                
        return score
