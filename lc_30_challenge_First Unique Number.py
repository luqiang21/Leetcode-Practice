class DLinkedNode():
    def __init__(self, value):
        self.value = value
        self.pre = None
        self.next = None

class FirstUnique(object):
    def _remove_node(self, value):
        # check if already removed
        node = self.map[value]
        if node is None:
            return
        
        nex = node.next
        pre = node.pre
        nex.pre = pre
        pre.next = nex
        
        node.pre = None
        node.next = None
        self.map[node.value] = None
        
    def _add_to_tail(self, node):
        node.pre = self.tail.pre
        node.next = self.tail
        
        # took a hour to fix this!!!!
        self.tail.pre.next = node
        self.tail.pre = node
        
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.map = {}
        self.head = DLinkedNode(0)
        self.tail = DLinkedNode(0)
        self.head.next = self.tail
        self.tail.pre = self.head
        
        for n in nums:
            if n not in self.map:
                self.add(n)
            else:
                self._remove_node(n)
            

    def showFirstUnique(self):
        """
        :rtype: int
        """
        if self.head.next == self.tail:
            return -1
        return self.head.next.value
        

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value in self.map:
            self._remove_node(value)
        else:
            node = DLinkedNode(value)
            self._add_to_tail(node)
            self.map[value] = node

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
