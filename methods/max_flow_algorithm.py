from Queue import LifoQueue


class Edge(object):
    def __init__(self, from_node, to_node, capacity=0):
        self.from_node = from_node
        self.to_node = to_node
        self.capacity = capacity

    def __repr__(self):
        return "{%s --(%s)--> %s}" % (self.from_node, self.capacity, self.to_node)

#
#   source --> 1 -------- 3/5 -------> 3
#              |                       |
#              |         sink          |
#             6/6          |          3/3
#              |           |           |
#              v           v           v
#              2---3/3---->4<---2/2----8
#              |           ^          /
#             3/3          |         /
#              |          4/4      1/1
#              |           |      /
#              v           |     /
#              7----3/5--->6 <--+

def get_max_flow(directed_graph, source, sink):
    residual = {edge: edge.capacity for edges in directed_graph.values() for edge in edges}
    flow_paths = []

    def flow_path(path):
        max_flow = float("inf")
        for edge in path:
            max_flow = min(max_flow, residual[edge])
        for edge in path:
            residual[edge] -= max_flow
        flow_paths.append((max_flow, path))

    bfs_queue = LifoQueue()
    bfs_queue.put([])
    while not bfs_queue.empty():
        path = bfs_queue.get()
        for edge in directed_graph[source if not path else path[-1].to_node]:
            if residual[edge] > 0:
                new_path = path[:]
                new_path.append(edge)
                if edge.to_node == sink:
                    flow_path(new_path)
                else:
                    bfs_queue.put(new_path)
    return flow_paths


if __name__ == "__main__":
    graph = [Edge(1, 3, 5),
             Edge(2, 4, 3),
             Edge(1, 2, 6),
             Edge(6, 4, 4),
             Edge(7, 6, 5),
             Edge(2, 7, 3),
             Edge(8, 4, 2),
             Edge(3, 8, 3),
             Edge(8, 6, 1)]

    directed_graph = {}
    for edge in graph:
        directed_graph.setdefault(edge.from_node, [])
        directed_graph[edge.from_node].append(edge)
    flow_paths = get_max_flow(directed_graph, 1, 4)

    total_flow = 0
    print "paths:"
    for flow_path in flow_paths:
        flow, path = flow_path[0], flow_path[1:]
        total_flow += flow
        print "\t", flow, path
    print "Total flow:", total_flow
