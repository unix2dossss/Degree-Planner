import json
from course import Course

# Load data from the JSON file
with open('data2.json', 'r') as file:
    data = json.load(file)


for course_id, course_info in data.items():
    print(f"ID: {course_id}")
    print(f"Code: {course_info['code']}")
    print(f"Name: {course_info['name']}")
    print(f"Description: {course_info['description']}")
    print(f"Prerequisites: {', '.join(str(p) for p in course_info['prerequisites'])}" if course_info['prerequisites'] else "Prerequisites: None")
    print(f"Restrictions: {', '.join(course_info['restrictions'])}" if course_info['restrictions'] else "Restrictions: None")
    print(f"Stage: {course_info['stage']}")
    print()

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

if __name__ == "__main__":
    g = Graph()
    for course_id, course_info in data.items():
        print(f"ID: {course_id}")
        if course_info['prerequisites']:
            for p in course_info['prerequisites']:
                g.add_edge(course_id, p)

    print(g)


# if __name__ == "__main__":
    # Create a graph
    # g = Graph()
# 
    # Add vertices
    # g.add_vertex('110')
    # g.add_vertex('120')
    # g.add_vertex('130')
    # g.add_vertex('210')
# 
    # Add edges
    # g.add_edge('210', '110')
    # g.add_edge('210', '130')
# 
    # g.add_edge('220', '120')
    # g.add_edge('220', '130')
# 
    # g.add_edge('230', '130')
# 
# 
    # Print the graph
    # print("Graph:")
    # print(g)
# 
    # Get neighbors of a vertex
    # print("Neighbors of 130:", g.get_neighbors('210'))
# 