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
                if new_distance < current_distance:
                    distances[neighbor] = new_distance
                    heappush(pq, (new_distance, neighbor))
        
        predecessors = {node: None for node in self.graph}

        for node, distance in distances.items():
            for neighbor, weight in self.graph[node].items():
                if distances[neighbor] == distance + weight:
                    predecessors[neighbor] = node
        
        return distances, predecessors
    
    # TODO: Implement the shortest Path
    def shortest_path(self, source: Node, destiny: Node):
        continue