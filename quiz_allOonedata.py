class Node(object):
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne(object):

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mapping = {}

    def _insert_after(self, prev_node, count):
        new_node = Node(count)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node
        return new_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        if key not in self.mapping:
            if self.head.next.count != 1:
                self._insert_after(self.head, 1)
            self.head.next.keys.add(key)
            self.mapping[key] = self.head.next
        else:
            curr_node = self.mapping[key]
            nxt_count = curr_node.count + 1
            if curr_node.next.count != nxt_count:
                self._insert_after(curr_node, nxt_count)
            curr_node.next.keys.add(key)
            self.mapping[key] = curr_node.next
            
            curr_node.keys.remove(key)
            if not curr_node.keys:
                self._remove(curr_node)

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        if key not in self.mapping:
            return
            
        curr_node = self.mapping[key]
        curr_node.keys.remove(key)
        prev_count = curr_node.count - 1
        
        if prev_count == 0:
            del self.mapping[key]
        else:
            if curr_node.prev.count != prev_count:
                self._insert_after(curr_node.prev, prev_count)
            curr_node.prev.keys.add(key)
            self.mapping[key] = curr_node.prev
            
        if not curr_node.keys:
            self._remove(curr_node)

    def getMaxKey(self):
        """
        :rtype: str
        """
        if self.tail.prev == self.head:
            return ""
        # iter().next() in Python 2, next(iter()) works for 2 and 3
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        """
        :rtype: str
        """
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
