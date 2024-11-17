import queue

def get_heuristics():
    heuristics = {}
    f = open("heuristics.txt")
    
    for i in f.readlines():
        node_val_heuristics = i.split()
        heuristics[node_val_heuristics[0]] = int(node_val_heuristics[1])
    
    return heuristics

def getCity():
    city = {}
    citiesCode = {}
    f = open("cities.txt")
    j = 1
    for i in f.readlines():
        node_city_val = i.split()
        city[node_city_val[0]] = [int(node_city_val[1]), int(node_city_val[2])]
        
        citiesCode[j] = node_city_val[0]
        j += 1
    
    return city, citiesCode

def create_graph():
    graph = {}
    f = open("citiesGraph.txt")
    for i in f.readlines():
        node_val = i.split()
        
        if node_val[0] in graph and node_val[1] in graph:
            c = graph.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            graph.update({node_val[0]: c})
            
            c = graph.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            graph.update({node_val[1]: c})
        
        elif node_val[0] in graph:
            c = graph.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            graph.update({node_val[0]: c})
            
            graph[node_val[1]] = [[node_val[0], node_val[2]]]
        
        elif node_val[1] in graph:
            c = graph.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            graph.update({node_val[1]: c})
            
            graph[node_val[0]] = [[node_val[1], node_val[2]]]
        
        else:
            graph[node_val[0]] = [[node_val[1], node_val[2]]]
            graph[node_val[1]] = [[node_val[0], node_val[2]]]
       
    return graph

def greedy_search(source, heuristics, graph, target="Bucharest"):
    pq = queue.PriorityQueue()
    pq.put((heuristics[source], source))
    
    path = []
    
    while pq.empty() == False:
        current = pq.get()[1]
        path.append(current)
        
        if current == target:
            break
        
        pq = queue.PriorityQueue()
        
        for i in graph[current]:
            if i[0] not in path:
                pq.put((heuristics[i[0]], i[0]))
    
    return path

def a_star(source, heuristics, graph, target="Bucharest"):
    pq = queue.PriorityQueue()
    distance = 0
    path = []
    
    pq.put((heuristics[source] + distance, [source, 0]))
    
    while pq.empty() == False:
        current = pq.get()[1]
        print(current)
        path.append(current[0])
        distance += int(current[1])
        
        if current[0] == target:
            break
        
        pq = queue.PriorityQueue()
        
        for i in graph[current[0]]:
            if i[0] not in path:
                pq.put((heuristics[i[0]] + int(i[1]) + distance, i))
    
    return path

def main():
    heuristics = get_heuristics()
    graph = create_graph()
    city, citiesCode = getCity()
    
    for i, j in citiesCode.items():
        print(i, j)
        
    while True:
        inputCode = int(input("Enter the code for the city's number (0 for exit): "))
        
        if inputCode == 0:
            break
        
        cityName = citiesCode[inputCode]
        
        gbfs = greedy_search(cityName, heuristics, graph)
        astar = a_star(cityName, heuristics, graph)
        
        print("greedy_search => ", gbfs)
        print("astar => ", astar)
        
main()