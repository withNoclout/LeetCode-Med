class Solution:
    def numberOfWays(self, corridor: str) -> int:
        """Return number of ways to split `corridor` into sections each containing exactly two seats.

        This mirrors the typical LeetCode solution: find all seat indices and multiply the
        number of choices between adjacent pairs of seat-pairs. The result is taken modulo
        10**9 + 7 as required by the problem.
        """
        MOD = 10**9 + 7
        seats = [i for i, c in enumerate(corridor) if c == 'S']

        if not seats or len(seats) % 2 == 1:
            return 0

        res = 1
        for i in range(2, len(seats), 2):
            # number of places to split between the end of previous pair and start of next
            res = (res * (seats[i] - seats[i - 1])) % MOD

        return res


if __name__ == "__main__":
    examples = ["SS", "SPS", "SSPSS", "PPP"]
    sol = Solution()
    for s in examples:
        print(f"{s!r} -> {sol.numberOfWays(s)}")
