class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        res = [0] * len(vals)
        stack = []
        for i, v in enumerate(vals):
            while stack and vals[stack[-1]] < v:
                res[stack.pop()] = v
            stack.append(i)
        return res
