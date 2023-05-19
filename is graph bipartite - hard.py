from collections import deque

def is_bipartite(graph):
    # Create a dictionary to store the colors assigned to each vertex
    colors = {}

    # Perform BFS on each vertex in the graph
    for vertex in graph:
        if vertex not in colors:
            # Assign the first vertex to Set A
            colors[vertex] = 'A'

            # Use a queue to perform BFS
            queue = deque()
            queue.append(vertex)

            # Continue BFS until the queue is empty
            while queue:
                current_vertex = queue.popleft()

                # Traverse the neighbors of the current vertex
                for neighbor in graph[current_vertex]:
                    if neighbor not in colors:
                        # Assign the neighbor to the opposite set of the current vertex
                        colors[neighbor] = 'B' if colors[current_vertex] == 'A' else 'A'
                        queue.append(neighbor)

                    # If the neighbor is already assigned to the same set as the current vertex, the graph is not bipartite
                    elif colors[neighbor] == colors[current_vertex]:
                        return False

    # If all vertices are visited without any conflicts, the graph is bipartite
    return True
