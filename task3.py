import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))
        # Додаємо зворотне ребро для неорієнтованого графа
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[to_node].append((from_node, weight))

def dijkstra(graph, start):
    # Ініціалізуємо відстані до всіх вершин як нескінченність
    distances = {vertex: float('infinity') for vertex in graph.edges}
    distances[start] = 0

    # Використовуємо бінарну купу для вибору вершини з найменшою відстанню
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо знайдена відстань більша за поточну, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Оновлюємо відстані до сусідів
        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight

            # Якщо знайдена коротша відстань, оновлюємо її
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def main():
    # Створюємо граф
    graph = Graph()
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 1)

    # Виконуємо алгоритм Дейкстри від початкової вершини 'A'
    start_vertex = 'A'
    shortest_paths = dijkstra(graph, start_vertex)

    # Виводимо найкоротші шляхи до всіх вершин
    for vertex, distance in shortest_paths.items():
        print(f"Відстань від {start_vertex} до {vertex} дорівнює {distance}")

if __name__ == "__main__":
    main()