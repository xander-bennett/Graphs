"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited = set()

        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            current_node = queue.dequeue()

            if current_node not in visited:
                visited.add(current_node)
                print(current_node)
                edges = self.get_neighbors(current_node)
                for edge in edges:
                    queue.enqueue(edge)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()

        stack.push(starting_vertex)

        while stack.size() > 0:
            current_node = stack.pop()

            if current_node not in visited:
                visited.add(current_node)
                print(current_node)
                edges = self.get_neighbors(current_node)
                for edge in edges:
                    stack.push(edge)

    def dft_recursive(self, vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        print(vertex)
        visited.add(vertex)

        edges = self.get_neighbors(vertex)

        for edge in edges:
            if edge not in visited:
                self.dft_recursive(edge, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        queue = Queue()
        # make a set for visited
        visited = set()
        # enqueue a path to the starting vertex
        queue.enqueue([starting_vertex])
        # while the queue isn't empty,
        while queue.size() > 0:
            # dequeue the next path
            current_path = queue.dequeue()
            # current node is the next thing in the path
            current_node = current_path[-1]
            # check if it's the target, aka destination vertex
            if current_node == destination_vertex:
                # if so, return the path!
                return current_path
            else:
                # else if not, mark this as visited
                if current_node not in visited:
                    # copy the path, add the neighbor to the copy
                    visited.add(current_node)
                    edges = self.get_neighbors(current_node)
                    # for each one, add a PATH TO IT to our queue
                    for edge in edges:
                        new_path = list(current_path)
                        new_path.append(edge)
                        queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # make a stack
        stack = Stack()
        # make a set for visited
        visited = set()
        # stack up a path to the starting vertex
        stack.push([starting_vertex])
        # while the stack isn't empty,
        while stack.size() > 0:
            # pop off the next path from the stack
            current_path = stack.pop()
            # current node is the next thing in the path
            current_node = current_path[-1]
            # check if it's the target, aka destination vertex
            if current_node == destination_vertex:
                # if so, return the path!
                return current_path
            else:
                # else if not, mark this as visited
                if current_node not in visited:
                    # copy the path, add the neighbor to the copy
                    visited.add(current_node)
                    edges = self.get_neighbors(current_node)
                    # for each one, add a PATH TO IT to our stack
                    for edge in edges:
                        new_path = list(current_path)
                        new_path.append(edge)
                        stack.push(new_path)

    def dfs_recursive(self, vertex, target, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        visited.add(vertex)
        path = path + [vertex]
        if vertex == target:
            return path
        for child_vertex in self.vertices[vertex]:
            if child_vertex not in visited:
                new_path = self.dfs_recursive(
                    child_vertex, target, visited, path)
                if new_path:
                    return new_path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
	Should print:
		{1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
	'''
    print(graph.vertices)

    '''
	Valid BFT paths:
		1, 2, 3, 4, 5, 6, 7
		1, 2, 3, 4, 5, 7, 6
		1, 2, 3, 4, 6, 7, 5
		1, 2, 3, 4, 6, 5, 7
		1, 2, 3, 4, 7, 6, 5
		1, 2, 3, 4, 7, 5, 6
		1, 2, 4, 3, 5, 6, 7
		1, 2, 4, 3, 5, 7, 6
		1, 2, 4, 3, 6, 7, 5
		1, 2, 4, 3, 6, 5, 7
		1, 2, 4, 3, 7, 6, 5
		1, 2, 4, 3, 7, 5, 6
	'''
    graph.bft(1)

    '''
	Valid DFT paths:
		1, 2, 3, 5, 4, 6, 7
		1, 2, 3, 5, 4, 7, 6
		1, 2, 4, 7, 6, 3, 5
		1, 2, 4, 6, 3, 5, 7
	'''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
	Valid BFS path:
		[1, 2, 4, 6]
	'''
    print(graph.bfs(1, 6))

    '''
	Valid DFS paths:
		[1, 2, 4, 6]
		[1, 2, 4, 7, 6]
	'''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))