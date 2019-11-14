__author__ = 'Elisei Shafer'

import csv
import pickle


def load_txt_file(file_path):
    graph = []
    with open(file_path, 'r') as f:
        data_reader = csv.reader(f, delimiter=' ')
        graph = [row[:2] for row in data_reader]

    graph_rev = reverse_graph((graph))
    data = {"graph":graph, "graph_rev":graph_rev}
    pickle_out = open("SCC.pickle", "wb")
    pickle.dump(data, pickle_out)
    pickle_out.close()

    return data


def load_pickle():
    with open('SCC.pickle', 'rb') as f:
        data = pickle.load(f)
    return data


def reverse_graph(gr):
    return [pair.reverse() for pair in gr]

# def dfs(graph, s):



def kosaraju(graph, graph_rev):
    num_nodes = 875715
    # The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
    visited = [False] * num_nodes

    # The list below holds info about sccs. The index is the scc leader and the value is the size of the scc.
    scc = [0] * num_nodes

    stack = []  # Stack for DFS
    order = []  # The finishing orders after the first pass

    ########################################################
    # DFS on reverse graph

    for node in range(num_nodes):
        if visited[node]:
            continue
        stack.append(node)
        while stack:

            for head in graph_rev[stack_node]:
                if head

                current_node = stack.pop()

                visited[current_node] = True


if __name__ == '__main__':
    # data = load_txt_file('SCC.txt')
    data = load_pickle()
    print(data["graph"])