
class Vertex:
    def __init__(self, value: str):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertices(self)

    def __repr__(self):
        return self.value


def create_graph_dict(steps: list) -> dict:
    vertices = {}
    for step in steps:
        vertices = add_graph_vertex(step[0], step[1], vertices)
        vertices = add_graph_vertex(step[1], step[0], vertices)
    return vertices


def add_graph_vertex(step1: str, step2: str, vertices: dict) -> dict:
    if step1 in vertices.keys():
        vertices[step1].append(step2)
    else:
        vertices[step1] = [step2]
    return vertices


def create_vertices(graph: dict) -> (dict, dict):
    vertices_by_name = {}
    visited_vertices = {}
    for node in graph.keys():
        vertex = Vertex(node)
        vertices_by_name[node] = vertex
        visited_vertices[node] = False
    return vertices_by_name, visited_vertices


def create_adjacent_vertices(graph: dict, vertices_by_name: dict) -> (dict, dict):
    vertices: list[Vertex] = []
    for step in graph.keys():
        vertex = vertices_by_name[step]
        for adj in graph[step]:
            vertex.adjacent_vertices.append(vertices_by_name[adj])
        vertices.append(vertex)
    return vertices


def traverse_graph_part1(start: Vertex, end: Vertex, visited_vertices: dict, path: list):
    global all_paths
    # Mark current vertex as visited and add it to the path
    visited_vertices[start.value] = True
    path.append(start.value)

    if start.value == end.value:
        # we have reached the end cave
        all_paths.append(path)
    else:
        for adjacent in start.adjacent_vertices:
            # traverse adjacent vertices if they have not been visited
            if adjacent.value.isupper() or not visited_vertices[adjacent.value]:
                traverse_graph_part1(adjacent, end, visited_vertices, path)

    # remove current vertex from the path and also set it to unvisited
    path.pop()
    visited_vertices[start.value] = False


# read in input data
with open("input12", "rb") as data:
    steps = [line.strip().decode("utf8").split("-") for line in data]

graph_dict = create_graph_dict(steps)
graph_vertices_by_name, graph_visited_vertices = create_vertices(graph_dict)
graph_vertices = create_adjacent_vertices(graph_dict, graph_vertices_by_name)
all_paths = []
traverse_graph_part1(graph_vertices_by_name["start"], graph_vertices_by_name["end"], graph_visited_vertices, [])
print(f"Part 1:number of generated paths: {len(all_paths)}")
