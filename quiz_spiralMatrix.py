# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def spiralMatrix(self, m, n, head):
        res = [[-1] * n for _ in range(m)]
        top, bottom, left, right = 0, m - 1, 0, n - 1
        node = head

        while node and top <= bottom and left <= right:
            for j in range(left, right + 1):
                if not node:
                    return res
                res[top][j] = node.val
                node = node.next
            top += 1

            for i in range(top, bottom + 1):
                if not node:
                    return res
                res[i][right] = node.val
                node = node.next
            right -= 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    if not node:
                        return res
                    res[bottom][j] = node.val
                    node = node.next
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if not node:
                        return res
                    res[i][left] = node.val
                    node = node.next
                left += 1

        return res
