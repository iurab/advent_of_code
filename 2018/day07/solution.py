from parse import parse
from collections import defaultdict, OrderedDict
import networkx as nx


def get_input():
    with open('input') as file:
        puzzle_input = file.read().splitlines()
    matcher = "Step {start} must be finished before step {stop} can begin."
    edges = []
    for line in puzzle_input:
        edges.append(parse(matcher, line))
    return edges


def part01(edges):
    # Create directional graph
    G = nx.DiGraph()
    for edge in edges:
        G.add_edge(edge['start'], edge['stop'])
    result = nx.lexicographical_topological_sort(G)
    print(''.join(result))


def part02(edges):
    # Create directional graph
    G = nx.DiGraph()
    for edge in edges:
        G.add_edge(edge['start'], edge['stop'])
    # Define number of workers
    n_workers = 5
    # Add time effort for each node
    for node in G.nodes:
        G.nodes[node]['work'] = ord(node) - ord('A') + 61
    elapsed_time = 0
    while G.nodes:
        # Get nodes without edges pointing to it
        availables_nodes = [node for node in G.nodes if G.in_degree(node) == 0]
        # Sort by effort
        availables_nodes.sort(key=lambda node: G.nodes[node]['work'])
        # Reduce effort
        for worker, node in zip(range(n_workers), availables_nodes):
            G.nodes[node]['work'] -= 1
            # If job done on the node, remove it
            if G.nodes[node]['work'] == 0:
                G.remove_node(node)
        elapsed_time += 1
    print(elapsed_time)


if __name__ == '__main__':
    edges = get_input()
    part01(edges)
    part02(edges)
