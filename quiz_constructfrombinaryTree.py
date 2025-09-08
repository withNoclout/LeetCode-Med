# ...existing code...
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Recursive reconstruction: root is preorder[0]; preorder[1] is left child root if left exists.
        def helper(pre, post):
            if not pre:
                return None
            root = TreeNode(pre[0])
            if len(pre) == 1:
                return root
            # find size of left subtree using the next preorder value in postorder
            left_root = pre[1]
            idx = post.index(left_root)
            left_size = idx + 1
            root.left = helper(pre[1:1 + left_size], post[:left_size])
            root.right = helper(pre[1 + left_size:], post[left_size:-1])
            return root

        return helper(preorder, postorder)
# ...existing code...
