class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        losses = defaultdict(int)
        players = set()

        for w, l in matches:
            players.add(w)
            players.add(l)
            losses[l] += 1

        zero_loss = []
        one_loss = []

        for p in players:
            if losses[p] == 0:
                zero_loss.append(p)
            elif losses[p] == 1:
                one_loss.append(p)

        zero_loss.sort()
        one_loss.sort()
        return [zero_loss, one_loss]
