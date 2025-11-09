# backend/tree_utils.py
import random
import io
import base64
import networkx as nx
import matplotlib.pyplot as plt

def prufer_to_tree(prufer):
    """Decode Prüfer code to edge list"""
    m = len(prufer)
    n = m + 2
    degree = [1] * (n + 1)
    for v in prufer:
        degree[v] += 1
    leaves = [i for i in range(1, n + 1) if degree[i] == 1]
    leaves.sort()
    edges = []
    import heapq
    heapq.heapify(leaves)
    for v in prufer:
        u = heapq.heappop(leaves)
        edges.append((u, v))
        degree[u] -= 1
        degree[v] -= 1
        if degree[v] == 1:
            heapq.heappush(leaves, v)
    u = heapq.heappop(leaves)
    w = heapq.heappop(leaves)
    edges.append((u, w))
    return edges

def random_labeled_tree(n):
    if n < 2:
        return []
    prufer = [random.randint(1, n) for _ in range(n - 2)]
    return prufer_to_tree(prufer)

def get_tree_image_base64(n):
    edges = random_labeled_tree(n)
    G = nx.Graph()
    G.add_nodes_from(range(1, n + 1))
    G.add_edges_from(edges)
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(4, 3))
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    img_b64 = base64.b64encode(buf.read()).decode('utf-8')
    return img_b64
