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
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()

        while q.size() > 0:
            current_node = q.dequeue()
            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node) 
                for neighbor in neighbors:
                    q.enqueue(neighbor)
                print(current_node)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            current_node = s.pop()
            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    s.push(neighbor)
                print(current_node)


    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            neighbors = self.get_neighbors(starting_vertex)
            print(starting_vertex)
            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest current_node from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])

        visited = set()

        if starting_vertex == destination_vertex:
            return
        while q.size() > 0:
            current_node = q.dequeue()
            node = current_node[-1]
            if node not in visited:
                neighbors = self.get_neighbors(node)
                for neighbor in neighbors:
                    new_current_node = list(current_node)
                    new_current_node.append(neighbor)
                    q.enqueue(new_current_node)
                    if neighbor == destination_vertex:
                        return new_current_node
                visited.add(node)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a current_node from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])

        visited = set()

        if starting_vertex == destination_vertex:
            return
        while s.size() > 0:
            current_node = s.pop()
            node = current_node[-1]
            if node not in visited:
                neighbors = self.get_neighbors(node)
                for neighbor in neighbors:
                    new_current_node = list(current_node)
                    new_current_node.append(neighbor)
                    s.push(new_current_node)
                    if neighbor == destination_vertex:
                        return new_current_node
                visited.add(node)


    def dfs_recursive(self, starting_vertex, destination_vertex, path = [], visited = set()):
        """
        Return a list containing a current_node from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        path = path + [starting_vertex]
        visited.add(starting_vertex)
        if starting_vertex == destination_vertex:
            return path
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, path, visited)
                if new_path:
                    return new_path

        ##################################
        # s = Stack()
        # s.push([starting_vertex])

        # visited = set()

        # if starting_vertex == destination_vertex:
        #     return
        # while s.size() > 0:
        #     current_node = s.pop()
        #     node = current_node[-1]
        #     if node not in visited:
        #         neighbors = self.get_neighbors(node)
        #         for neighbor in neighbors:
        #             new_current_node = list(current_node)
        #             new_current_node.append(neighbor)
        #             s.push(new_current_node)
        #             if neighbor == destination_vertex:
        #                 return new_current_node
        #         visited.add(node)

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
    Valid BFT current_nodes:
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
    Valid DFT current_nodes:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS current_node:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS current_nodes:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
