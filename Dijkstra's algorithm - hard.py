import heapq

def dijkstra(graph, start):
    # Create a dictionary to store the shortest distance to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Create a priority queue to keep track of the next node to visit
    pq = [(0, start)]
    
    while pq:
        # Pop the node with the smallest distance from the priority queue
        curr_dist, curr_node = heapq.heappop(pq)
        
        # If we've already visited this node, skip it
        if curr_dist > distances[curr_node]:
            continue
        
        # Update the distances to each neighbor of the current node
        for neighbor, weight in graph[curr_node].items():
            dist = curr_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))
    
    return distances
