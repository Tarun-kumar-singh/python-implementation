'''
Implmentation od graph using adjacency list
**  Adjacency list
'''


class Graph:

    def __init__(self):
        self.graph_dict = {}

    def create_graph(self):
        no_of_nodes = int(input('enter the no of nodes'))
        t = 1
        while t <= no_of_nodes:
            node = int(input('enter the {0}th node '.format(t)))
            neighbour_list = []
            while True:
                neighbour = int(input('enter the neighbour of {0} '.format(node)))
                if neighbour == -1:
                     break
                neighbour_list.append(neighbour)
            self.graph_dict[node] = neighbour_list
            t = t + 1

    def get_edges(self):
        edges = []
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                edges.append((node, neighbour))
        return edges

# g = Graph ()
# g.create_graph()
# print(g.get_edges())