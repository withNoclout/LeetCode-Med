from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)
        radiant = deque()
        dire = deque()

        # Put indices of R and D senators into separate queues
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # Simulate rounds
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                # R acts first, bans D, requeue R to next round
                radiant.append(r + n)
            else:
                # D acts first, bans R, requeue D
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"
