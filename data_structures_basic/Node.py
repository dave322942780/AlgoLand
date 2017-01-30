class Node:
    def __init__(self, node_rep, next_node=None):
        if type(node_rep) == list:
            self.value = node_rep.pop(0)
            self.next_node = Node(node_rep) if node_rep else None
        else:
            self.value = node_rep
            self.next_node = next_node

    def __repr__(self):
        res = []
        cur = self
        while cur:
            res.append(cur.value)
            cur = cur.next_node
        return str(res)

    def __eq__(self, other):
        cur1 = self
        cur2 = other
        while cur1 and cur2:
            if cur1.value != cur2.value:
                return False
            cur1 = cur1.next_node
            cur2 = cur2.next_node
        return cur1 is None and cur2 is None
