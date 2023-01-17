# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder_list = []
        self.postorder(root, postorder_list)

        return postorder_list

    def postorder(self,
                  root: Optional[TreeNode],
                  postorder_list: List[int]):
        if root is None:
            return None

        self.postorder(root.left, postorder_list)
        self.postorder(root.right, postorder_list)
        postorder_list.append(root.val)



if __name__ == "__main__":
    from tree import TreeNode as TN

    root = [1, None, 2, 3]
    # root = [1]
    # root = []
    t = TN.create(root, 0)
    s = Solution()
    print(s.postorderTraversal(t))
