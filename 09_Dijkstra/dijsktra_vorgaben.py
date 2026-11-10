import heapq

graph = {
    'A': [('B', 3), ('C', 6)],
    'B': [('A', 3), ('C', 2), ('D', 8)],
    'C': [('A', 6), ('B', 2), ('D', 3)],
    'D': [('B', 8), ('C', 3)],
 }

def dijkstra(graph, start):
    distances = {node: (float('inf'), None) for node in graph}
    distances[start] = (0, None)
    priority_queue = [(0, start)]


    # Der Rückgabewert soll am Ende das aktualisierte Dictionary der Distanzen und Vorgänger sein.
    return distances

# print(dijkstra(graph, 'A'))



import heapq

# Creating an initial heap
h = [(20, "C"), (10, "A")]
heapq.heapify(h)

# Appending an element
heapq.heappush(h, (5, "B"))

# Heap before popping
print(h)
print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))
print(h)