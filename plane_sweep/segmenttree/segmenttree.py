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
        
        
        self.array = array
        if type(operations) != list:
            raise TypeError("operations must be a list")
        self.operations = {}
        for op in operations:
            self.operations[op.name] = op
        self.root = SegmentTreeNode(0, len(array) - 1, self)

    def query(self, start, end, operation_name):
        """
        Returns the result of the operation execution with `operation_name`
        on the range from [start, end]
        """
        if self.operations.get(operation_name) == None:
            raise Exception("This operation is not available")
        return self.root._query(start, end, self.operations[operation_name])
    
    
    def pointQuery(self, point, root=None):
        if root is None:
            root = self.root
        
        if root.values["sum"] > 0:
            print(f"node is active? {root.values}, {root.range}")
            res = root.true_intervals
        else: res = set()

        if root.left or root.right:
            if root.left and root.left.range[0] <= point <= root.left.range[1]:
                [res.add(x) for x in self.pointQuery(point, root.left)]
            elif root.right :
                [res.add(x) for x in self.pointQuery(point, root.right)]
                
        return res

    def summary(self):
        """
        Prints the summary for the whole array (values in the root node).
        """
        return self.root.values
    
    
    def associate(self, start, end, node=None):
        if node is None:
            node = self.root
            
        # if Int(v) sub [start, end]:
        if node.range[0] >= start and node.range[1] <= end:
            node.true_intervals.add((start, end))
            
            print(f"associated node {node.range} with {start} - {end}")
            
            # node.true_intervals += 1
        else:
            # if left node interval intersects with [start, end]
            if node.left and (node.left.range[1] >= start or node.left.range[0] <= end):
                self.associate(start, end, node.left)
            if node.right and (node.right.range[1] >= start or node.right.range[0] <= end):
                self.associate(start, end, node.right)


    def update(self, position, value):
        """
        Updates an old value at `position` to a new `value`.
        """
        self.root._update(position, value)

    def update_range(self, start, end, value):
        """
        Updates old values old in the range [start, end], inclusively, to a new value.
        """
        self.root._update_range(start, end, value)

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
        self.values = {}
        self.left = None
        self.right = None
        
        self.true_intervals = set()
        # self.true_intervals = 0
        
        if start == end:
            self._sync()
            return
        self.left = SegmentTreeNode(start, start + (end - start) // 2,
                                    segment_tree)
        self.right = SegmentTreeNode(start + (end - start) // 2 + 1, end,
                                     segment_tree)
        self._sync()

    def _query(self, start, end, operation):
        if end < self.range[0] or start > self.range[1]:
            # this segment does not contain it
            print(f"range: {self.range} does not contain {start} - {end}")
            return None
        if start <= self.range[0] and self.range[1] <= end:
            print(f"range: {self.range} fully contained in {start} - {end}")
            # this segment is fully contained int the query range
            return self.values[operation.name]
        
        print(f"range: {self.range} partially contained in {start} - {end}")
        self._push()
        left_res = self.left._query(start, end,
                                    operation) if self.left else None
        right_res = self.right._query(start, end,
                                      operation) if self.right else None
        
        if left_res is None:
            return right_res
        if right_res is None:
            return left_res
        return operation.f([left_res, right_res])

    def _update(self, position, value):
        if position < self.range[0] or position > self.range[1]:
            return
        if position == self.range[0] and self.range[1] == position:
            self.parent_tree.array[position] = value
            self._sync()
            return
        self._push()
        self.left._update(position, value)
        self.right._update(position, value)
        self._sync()

    def _update_range(self, start, end, value):
        if end < self.range[0] or start > self.range[1]:
            return
        if start <= self.range[0] and self.range[1] <= end:
            self.range_value = value
            self._sync()
            return
        self._push()
        self.left._update_range(start, end, value)
        self.right._update_range(start, end, value)
        self._sync()

    def _sync(self):
        if self.range[0] == self.range[1]:
            for op in self.parent_tree.operations.values():
                current_value = self.parent_tree.array[self.range[0]]
                if self.range_value is not None:
                    current_value = self.range_value
                self.values[op.name] = op.f([current_value])
        else:
            for op in self.parent_tree.operations.values():
                result = op.f(
                    [self.left.values[op.name], self.right.values[op.name]])
                if self.range_value is not None:
                    bound_length = self.range[1] - self.range[0] + 1
                    result = op.f_on_equal(self.range_value, bound_length)
                self.values[op.name] = result

    def _push(self):
        if self.range_value is None:
            return
        if self.left:
            self.left.range_value = self.range_value
            self.right.range_value = self.range_value
            self.left._sync()
            self.right._sync()
            self.range_value = None

    def __repr__(self):
        ans = "({}, {}): {}\n".format(self.range[0], self.range[1],
                                      self.values)
        if self.left:
            ans += self.left.__repr__()
        if self.right:
            ans += self.right.__repr__()
        return ans