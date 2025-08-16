import random 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head 


    def getRandom(self):
        """
        :rtype: int
        """
        result = None 
        node = self.head 
        count = 0 
        while node : 
            count += 1 
            if random.radint( 1, count  )== 1 : 
                result = node.val 
            node = node.next  
        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
