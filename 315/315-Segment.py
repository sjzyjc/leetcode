class SegmentTreeNode:
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.val = val
        self.left = self.right = None
        
class SegmentTree:
    def __init__(self, n):
        self.root = self.build(0, len(n) - 1, n)
        
    def build(self, start, end, n):
        if start > end:
            return None
        
        cur = SegmentTreeNode(start, end, n[start])
        if start == end:
            return cur
        
        mid = (start + end) // 2
        cur.left = self.build(start, mid, n)
        cur.right = self.build(mid + 1, end, n)
        
        if cur.left:
            cur.val = cur.left.val 
        
        if cur.right:
            cur.val += cur.right.val
            
        return cur
            
    
    def query(self, root, start, end):
        if not root:
            return 0
        
        if root.start == start and root.end == end:
            return root.val
        
        mid =  (root.start + root.end) // 2
        if end <= mid:
            return self.query(root.left, start, end)
        elif start > mid:
            return self.query(root.right, start, end)
        else:
            return self.query(root.left, start, mid) + self.query(root.right, mid+1, end)
        
    def update(self, root, index):
        if not root:
            return
        
        if root.start == root.end == index:
            root.val += 1
            return
        
        mid = (root.start + root.end) // 2
        if index <= mid:
            self.update(root.left, index)
        else:
            self.update(root.right, index)
        
        root.val = root.left.val + root.right.val
        
        
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        min_num = min(nums)
        size = max(nums) - min_num + 1
        count = [0 for _ in range(size)]
        st = SegmentTree(count)
        
        ans = []
        for index in range(len(nums) - 1, -1, -1):
            count_index = nums[index] - min_num
            st.update(st.root, count_index)
            ans.append(st.query(st.root, 0, count_index - 1))
            
        return ans[::-1]
