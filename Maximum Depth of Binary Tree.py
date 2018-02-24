import unittest
import TreeSolution

class TreeNode(object):
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None

class unitest(unittest.TestCase):
    def testNone(self):
        Input = None
        Output = 0
        self.assertEqual(Solution().maxDepth(Input),Output);
    def testSample(self):
        row = [3,9,20,None,None,15,7]
        tree = TreeSolution.TreeSolution()
        Input = tree.AddBinaryTreeNode(row)
        Output = 3
        self.assertEqual(Solution().maxDepth(Input),Output);

class Solution():
    def maxDepth(self, root):
        if root == None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1

if __name__ == '__main__':
    unittest.main()
