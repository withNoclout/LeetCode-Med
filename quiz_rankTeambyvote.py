class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        if not votes:
            return ""

        n = len(votes[0])
        teams = set("".join(votes))

        # score[team][pos] = number of votes that team got for position pos
        score = {team: [0] * n for team in teams}

        for vote in votes:
            for i, team in enumerate(vote):
                score[team][i] -= 1  # negative for easier sorting (higher rank = more votes)

        # Sort: by score first, then lexicographically
        res = sorted(teams, key=lambda x: (score[x], x))
        return "".join(res)
