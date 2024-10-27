import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

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

def generate_colors(n):
    """Генерує n кольорів від темних до світлих відтінків."""
    colors = []
    for i in range(n):
        shade = int(255 * (i / (n - 1)))
        colors.append(f'#{shade:02x}{shade:02x}{255 - shade:02x}')
    return colors

def dfs(tree_root):
    """Обхід дерева в глибину (DFS) з візуалізацією."""
    stack = [tree_root]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return visited

def bfs(tree_root):
    """Обхід дерева в ширину (BFS) з візуалізацією."""
    queue = deque([tree_root])
    visited = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return visited

def draw_tree(tree_root, traversal):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}  # Початкова позиція для кореневого вузла
    tree = add_edges(tree, tree_root, pos)

    visited_nodes = traversal(tree_root)
    colors = generate_colors(len(visited_nodes))

    for i, node in enumerate(visited_nodes):
        node.color = colors[i]

    node_colors = [node.color for node in visited_nodes]
    labels = {node.id: node.val for node in visited_nodes}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

# Приклад використання
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Візуалізація обходу в глибину (DFS)
draw_tree(root, dfs)

# Візуалізація обходу в ширину (BFS)
draw_tree(root, bfs)