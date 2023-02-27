import random



class Vertex:
    """
    A class that represents a node in the graph.

    Attributes:
    - value (str): The value of the node.
    - adjacent (dict): A dictionary of adjacent nodes and their weights.
    - neighbors (list): A list of adjacent nodes.
    - neighbors_weights (list): A list of weights of adjacent nodes.

    Methods:
    - add_edge_to(vertex, weight=0): Adds an edge to the given vertex with an optional weight.
    - increment_edge(vertex): Increments the weight of an edge to the given vertex.
    - get_adjacent_nodes(): Returns the adjacent nodes of the vertex.
    - get_probability_map(): Initializes the probability map of adjacent nodes.
    - next_word(): Returns the next word based on the probability map.
    """
    def __init__(self, value):
        """
        Initializes a Vertex object.

        Args:
        - value (str): The value of the node.
        """
        self.value = value
        self.adjacent = {}
        self.neighbors = []
        self.neighbors_weights = []

    def __str__(self):
        """
        Returns the string representation of the vertex.

        Returns:
        - A string representing the vertex.
        """
        return self.value + ' '.join([node.value for node in self.adjacent.keys()])

    def add_edge_to(self, vertex, weight=0):
        """
        Adds an edge to the given vertex with an optional weight.

        Args:
        - vertex (Vertex): The vertex to add an edge to.
        - weight (int): The weight of the edge.
        """
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        """
        Increments the weight of an edge to the given vertex.

        Args:
        - vertex (Vertex): The vertex to increment the weight of the edge to.
        """
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_adjacent_nodes(self):
        """
        Returns the adjacent nodes of the vertex.

        Returns:
        - A dictionary of adjacent nodes and their weights.
        """
        return self.adjacent.items()

    def get_probability_map(self):
        """
        Initializes the probability map of adjacent nodes.
        """
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        """
        Returns the next word based on the probability map.

        Returns:
        - The next word based on the probability map.
        """
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]

class Graph(object):
    """
    Graph class for building and manipulating graphs of Vertex objects.

    Attributes:
        vertices (dict): A dictionary of Vertex objects in the graph.

    """

    def __init__(self):
        """
        Initializes a new Graph object with an empty vertices dictionary.
        """
        self.vertices = {}

    def get_vertex_values(self):
        """
        Returns a set of the values of the vertices in the graph.
        """
        return set(self.vertices.keys())

    def add_vertex(self, value):
        """
        Adds a new Vertex object with the specified value to the graph.
        """
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        """
        Returns the Vertex object with the specified value, creating a new one if it does not exist in the graph.
        """
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]

    def get_next_word(self, current_vertex):
        """
        Returns the next word in the Markov chain, given the current vertex.

        Args:
            current_vertex (Vertex): The current vertex in the chain.

        Returns:
            Vertex: The next vertex in the chain.

        """
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        """
        Generates the probability mappings for all the vertices in the graph.
        """
        for vertex in self.vertices.values():
            vertex.get_probability_map()

    def print_graph(self):
        """
        Prints the vertices and edges of the graph.
        """
        for vertex in self.vertices.values():
            adjacent_vertices = vertex.get_adjacent_nodes()
            for adj_vertex, weight in adjacent_vertices:
                print(f"{vertex.value} -> {adj_vertex.value} ({weight})")