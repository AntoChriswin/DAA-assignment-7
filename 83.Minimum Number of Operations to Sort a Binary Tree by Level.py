class Solution:
    def minOperations(self, root: TreeNode) -> int:
        def inorder(node, level, levels):
            if not node:
                return
            inorder(node.left, level + 1, levels)
            levels[level].append(node.val)
            inorder(node.right, level + 1, levels)

        def is_sorted(arr):
            return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

        def count_operations(arr):
            count = 0
            while not is_sorted(arr):
                for i in range(len(arr) - 1):
                    if arr[i] > arr[i + 1]:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        count += 1
            return count

        levels = defaultdict(list)
        inorder(root, 0, levels)
        operations = sum(count_operations(level) for level in levels.values())
        return operations
