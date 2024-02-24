class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, start, end):
        if start not in self.adj_list:
            self.add_vertex(start)
        if end not in self.adj_list:
            self.add_vertex(end)
        self.adj_list[start].append(end)

    def get_neighbors(self, vertex):
        if vertex in self.adj_list:
            return self.adj_list[vertex]
        else:
            return []

    def __str__(self):
        return str(self.adj_list)

class Tree:
    def __init__(self, node, child=None):
        self.name = node
        self.child = child
        self.parent = None

    def add_child(self, child_node):
        self.child = Tree(child_node)
        self.child.parent = self

    def get_parent(self):
        if not self.parent:
            return 'This is the root node'
        return self.parent
    
    def get_child(self):
        if not self.name:
            return "This node doesn't have any children"
        return self.child
    
    def __str__(self):
        return f'node: {self.name}'

# new_tree = Tree('root node')

# new_tree.add_child('child node')
# new_child = new_tree.get_child()
# new_child_child = new_child.get_child()
# new_child_child_child = new_child_child.get_child()
# print(new_child_child)

# print(new_tree.name, new_tree.child)
# print(new_tree.child.name)
# print(new_tree.child.parent.name)
