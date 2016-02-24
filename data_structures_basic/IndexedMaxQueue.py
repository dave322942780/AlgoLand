
class MaxBSTQueue(object):
    cur_path = []
    _reverse = False

    def _deep_right(self, node):
        cur = node
        while cur.right:
            cur = cur.right
            self.cur_path.append([cur, False])

    def __init__(self, tree):
        self.cur_path.append([tree, False])
        self._deep_right(tree)

    def get(self):
        # edge.right is either none or visited thus can be safely ignored,
        # next smallest is edge(node), then edge[.left[.right[.right...]]],
        # if right and left children are both visited, traverse up.
        edge = self.cur_path[-1]
        edge_node = self.cur_path[-1][0]
        visited = self.cur_path[-1][1]
        if (len(self.cur_path) == 1 and self.cur_path[0][1]) or len(self.cur_path) == 0:
            return None
        elif not visited:
            self.cur_path[-1][1] = True
            if edge_node.left:
                self.cur_path.append([edge_node.left, False])
                self._deep_right(edge_node.left)
                edge[1] = True
                return edge_node
            else:
                cur = len(self.cur_path) - 1
                while cur >= 0 and self.cur_path[cur][1]:
                    cur -= 1
                self.cur_path = self.cur_path[:cur + 1]
                edge[1] = True
                return edge_node
