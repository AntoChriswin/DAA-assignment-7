class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        def merge(left, right):
            return (left + right)[:k]

        nums = inorder(root)
        return merge(sorted(nums, key=lambda x: abs(x - target)), [])
