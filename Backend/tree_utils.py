import itertools
import networkx as nx
import matplotlib
matplotlib.use('Agg')  # prevents GUI errors on macOS
import matplotlib.pyplot as plt
import io
import base64



def prufer_to_tree(prufer):
    """Convert Prüfer code to tree edges"""
    m = len(prufer)
    n = m + 2
    degree = [1] * (n + 1)
    for v in prufer:
        degree[v] += 1
    edges = []
    import heapq
    leaves = [i for i in range(1, n + 1) if degree[i] == 1]
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


def all_prufer_sequences(n):
    """Generate all possible Prüfer sequences for given n"""
    if n < 2:
        return [[]]
    symbols = range(1, n + 1)
    return itertools.product(symbols, repeat=n - 2)


def get_all_trees(n):
    """Generate all distinct labeled trees for n"""
    trees = []
    for seq in all_prufer_sequences(n):
        edges = prufer_to_tree(list(seq))
        trees.append(edges)
    return trees


def edges_to_base64(n, edges):
    """Convert edges to image base64"""
    G = nx.Graph()
    G.add_nodes_from(range(1, n + 1))
    G.add_edges_from(edges)
    plt.figure(figsize=(3, 2))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=400)
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')


def get_all_tree_images(n):
    """Return list of base64 images for all labeled trees"""
    trees = get_all_trees(n)
    images = [edges_to_base64(n, edges) for edges in trees]
    return images
