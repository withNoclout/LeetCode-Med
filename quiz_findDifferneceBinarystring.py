class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        res = []
        
        # Iterate through the strings using their index
        for i in range(len(nums)):
            # Look at the i-th character of the i-th string
            curr_char = nums[i][i]
            
            # Flip the character: if '0' make it '1', if '1' make it '0'
            res.append("1" if curr_char == "0" else "0")
            
        return "".join(res)
