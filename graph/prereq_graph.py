import json
# from course import Course
from graph.ADT import Graph

# Load data from the JSON file
with open('data2.json', 'r') as file:
    data = json.load(file)

if __name__ == "__main__":
    g = Graph()
    for course_id, course_info in data.items():
        if course_info['prerequisites']:
            for prereq in course_info['prerequisites']:
                g.add_edge(course_id, prereq)
        else:
            g.add_vertex(course_id)
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