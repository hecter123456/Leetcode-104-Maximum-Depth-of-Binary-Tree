import unittest

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

class Solution():
    def maxDepth(self, root):
        if root == None:
            return 0 

if __name__ == '__main__':
    unittest.main()
