import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Додаємо вузол до графа
        if node.left:
            graph.add_edge(node.id, node.left.id)  # Додаємо ребро до лівого нащадка
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)  # Додаємо ребро до правого нащадка
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}  # Початкова позиція для кореневого вузла
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]  # Отримуємо кольори вузлів
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Отримуємо мітки вузлів

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap(arr):
    nodes = [Node(key) for key in arr]  # Створюємо вузли для кожного елемента масиву
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]  # Встановлюємо лівого нащадка
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]  # Встановлюємо правого нащадка
    return nodes[0] if nodes else None  # Повертаємо кореневий вузол

# Масив для побудови бінарної купи
heap_array = [10, 5, 3, 2, 4, 1]

# Побудова бінарної купи
heap_root = build_heap(heap_array)

# Відображення бінарної купи
draw_tree(heap_root)