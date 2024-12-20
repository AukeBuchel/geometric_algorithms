class Operation:
    def __init__(self, name, function, function_on_equal, neutral_value=0):
        self.name = name
        self.f = function
        self.f_on_equal = function_on_equal


def add_multiple(x, count):
    return x * count


def min_multiple(x, count):
    return x


def max_multiple(x, count):
    return x


def count_multiple(x, count):
    return len(x) * count


count_operation = Operation("count", len, count_multiple, 0)
sum_operation = Operation("sum", sum, add_multiple, 0)
min_operation = Operation("min", min, min_multiple, 1e9)
max_operation = Operation("max", max, max_multiple, -1e9)


class SegmentTree:
    """
    SegmentTree class. Handles an underlying array as well as available
    operations and pointer to the root of a tree.
    """

    def __init__(self,
                 array,
                 operations=[sum_operation, min_operation, max_operation]):
        """
        Builds a segment tree based on the provided `array`. Supports operations
        of class Operation provided in the operations array.
        """
        
        
        # self.array = array
        if type(operations) != list:
            raise TypeError("operations must be a list")
        self.root = SegmentTreeNode(0, len(array) - 1, self)

    
    def pointQuery(self, point, root=None, res=None):
        if root is None:
            root = self.root
        if res is None: 
            res = set()
        
        if len(root.true_intervals) > 0:
            [res.add(x) for x in root.true_intervals]

        # not a leaf node
        if root.left or root.right:
            if root.left and root.left.range[0] <= point <= root.left.range[1]:
                self.pointQuery(point, root.left, res)
            elif root.right :
                self.pointQuery(point, root.right, res)
                
        return res
    
    def pointQuery2(self, point, root=None, unique_count=0):
        # apply some operation that counts the number of unique true intervals at a subtree 
        if root is None:
            root = self.root

        # Count the number of true_intervals at this node
        unique_count += len(root.true_intervals)

        # Traverse left or right based on the query point
        if root.left or root.right:  # If it's not a leaf node
            if root.left and root.left.range[0] <= point <= root.left.range[1]:
                unique_count = self.pointQuery2(point, root.left, unique_count)
            elif root.right:
                unique_count = self.pointQuery2(point, root.right, unique_count)

        return unique_count

        

    def summary(self):
        """
        Prints the summary for the whole array (values in the root node).
        """
        return self.root.values
    
    
    """Does interval S1 overlap S2?
    |---S1---|
        |---S2---|
    
    or 
    
        |---S1---|
    |---S2---|    
    """
    def __overlaps(self, i1, i2):
        s1, e1 = i1
        s2, e2 = i2
        
        if (s1 <= e2 and s1 >= s2) or (e1 <= e2 and e1 >= s2):
            return True
        elif (s2 <= e1 and s2 >= s1) or (e2 <= e1 and e2 >= s1):
            return True
        
        return False    
    
    """
    Associate a primitive interval with a true interval. This should only happen if the true interval is fully contained in the primitive interval.
    """
    def associate(self, start, end, id, node=None):
        if node is None:
            node = self.root
            
        # if Int(v) sub [start, end]:
        if node.range[0] >= start and node.range[1] <= end:
            node.true_intervals.add(id)
            # print(f"associated node {node.range} with {start} - {end}")            
        else:
            # if left node interval intersects with [start, end]
            if node.left and self.__overlaps(node.left.range, (start, end)):
                self.associate(start, end, id, node.left)
            if node.right and self.__overlaps(node.right.range, (start, end)):
                self.associate(start, end, id, node.right)
                
    def dissociate(self, start, end, id, node=None):
        if node is None:
            node = self.root

        if node.range[0] >= start and node.range[1] <= end:
            node.true_intervals.remove(id)
            # print(f"dissociated node {node.range} with {start} - {end}")            
        else:
            # if left node interval intersects with [start, end]
            if node.left and self.__overlaps(node.left.range, (start, end)):
                self.dissociate(start, end, id, node.left)
            if node.right and self.__overlaps(node.right.range, (start, end)):
                self.dissociate(start, end, id, node.right)

    def __repr__(self):
        return self.root.__repr__()


class SegmentTreeNode:
    """
    Internal SegmentTreeNode class represents a node of a segment tree. Each node
    stores the reference to the left and the right bound of a segment this
    node is responsible for.
    """

    def __init__(self, start, end, segment_tree):
        self.range = (start, end)
        self.parent_tree = segment_tree
        self.range_value = None
        # self.values = {}
        self.left = None
        self.right = None
        
        self.true_intervals = set()
        
        if start == end:
            # self._sync()
            return
        self.left = SegmentTreeNode(start, start + (end - start) // 2,
                                    segment_tree)
        self.right = SegmentTreeNode(start + (end - start) // 2 + 1, end,
                                     segment_tree)
        # self._sync()
