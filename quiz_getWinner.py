class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        winner = arr[0]
        win_count = 0

        for i in range(1, len(arr)):
            if winner > arr[i]:
                win_count += 1
            else:
                winner = arr[i]
                win_count = 1
            if win_count == k:
                return winner

        return winner
