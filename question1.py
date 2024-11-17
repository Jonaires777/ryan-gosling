# Question 1 of list of excercises
from heapq import heapify, heappop, heappush

type Node = str

class Graph:    
    def __init__(self, graph: dict = {}):
        self.graph = graph
    
    def add_edge(self, inode: Node, fnode: Node, weight: float):
        if inode not in self.graph:
            self.graph[inode] = {}
        self.graph[inode][fnode] = weight
    
    def shortest_distances(self, source: Node):
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0
        
        pq = [(0, source)]
        heapify(pq)
        
        visited = set()
        
        while pq:
            current_distance, current_node = heappop(pq)
            
            if current_node in visited:
                continue
            visited.add(current_node)
            
            for neighbor, weight in self.graph[current_node].items():
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heappush(pq, (new_distance, neighbor))
        
        predecessors = {node: None for node in self.graph}

        for node, distance in distances.items():
            for neighbor, weight in self.graph[node].items():
                if distances[neighbor] == distance + weight:
                    predecessors[neighbor] = node
        
        return distances, predecessors
    
    def shortest_path(self, source: Node, destiny: Node):
        _, predecessors = self.shortest_distances(source)
        
        path = []
        current_node = destiny
        
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]
        
        path.reverse()
        
        return path

class main():
    G = Graph()
    
    # source A
    G.add_edge("A", "B", 3)
    G.add_edge("A", "C", 1)
    G.add_edge("A", "D", 7)
    
    # source B
    G.add_edge("B", "A", 3)
    G.add_edge("B", "C", 1)
    G.add_edge("B", "E", 6)

    # source C
    G.add_edge("C", "B", 5)
    G.add_edge("C", "A", 1)
    G.add_edge("C", "D", 2)
    
    # source D
    G.add_edge("D", "E", 2)
    G.add_edge("D", "A", 7)
    G.add_edge("D", "C", 2)
    
    # srouce E
    G.add_edge("E", "D", 2)
    G.add_edge("E", "F", 1)
    
    # source F
    G.add_edge("F", "E", 1)
    
    distances, _ = G.shortest_distances("A")
    path = G.shortest_path("A", "D")
    
    print(f"As distancias de A até os outros nos sao: {distances}")
    print(f"O menor caminho de A a D eh: {path}")
    