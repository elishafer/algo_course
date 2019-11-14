__author__ = 'Elisei Shafer'

import csv
import pickle


def load_txt_file(file_path):
    # node labels range from 1 to 875714. 875715 was used because of the range operator... range(875715) goes up to 875714.
    num_nodes = 875715

    # Adjacency representations of the graph and reverse graph
    gr = [[] for i in range(num_nodes)]
    r_gr = [[] for i in range(num_nodes)]
    with open(file_path, 'r') as f:
        data_reader = csv.reader(f, delimiter=' ')
        for items in data_reader:
            gr[int(items[0])] += [int(items[1])]
            r_gr[int(items[1])] += [int(items[0])]

    data = {"graph":gr, "graph_rev":r_gr}
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



def kosaraju_dfs_first(graph_rev, num_nodes):

    # The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
    visited = [False] * num_nodes

    # The list below holds info about sccs. The index is the scc leader and the value is the size of the scc.
    scc = [0] * num_nodes

    stack = []  # Stack for DFS
    order = []  # The finishing orders after the first pass

    ########################################################
    # DFS on reverse graph

    for node in range(num_nodes):
        if visited[node] or node == 0:
            continue
        stack.append(node)
        while stack:
            stack_node = stack[-1]
            for head in graph_rev[stack_node]:
                if not visited[head]:
                    stack.append(head)
                    visited[head] = True
                    break
                else:
                    continue

            if stack_node == stack[-1]:
                # If we've reached a dead end
                order.append(stack_node)
                stack_node = stack.pop()


    return order


def kosaraju_dfs_second(graph, num_nodes, order):

    # The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
    visited = [False] * num_nodes

    # The list below holds info about sccs. The index is the scc leader and the value is the size of the scc.
    scc = [0] * num_nodes

    stack = []  # Stack for DFS

    visited = [False] * len(visited)  # Resetting the visited variable

    for node in order:
        if visited[node]:
            continue
        s = node
        stack.append(node)
        visited[node] = True

        while stack:
            stack_node = stack[-1]

            for head in graph[stack_node]:
                if not visited[head]:
                    stack.append(head)
                    visited[head] = True
                    break
                else:
                    continue

            if stack_node == stack[-1]:
                # If we've reached a dead end
                stack.pop()
                scc[s] += 1

    return scc


def kosaraju_main(graph, graph_rev, num_nodes):

    order = kosaraju_dfs_first(graph_rev, num_nodes)
    order.reverse()
    scc = kosaraju_dfs_second(graph,num_nodes,order)

    return scc


if __name__ == '__main__':
    # data = load_txt_file('SCC.txt')
    data = load_pickle()
    num_nodes = 875715
    graph = data["graph"]
    graph_rev = data["graph_rev"]

    # print(data["graph"])

    # num_nodes = 11
    # graph_1_rev = [[], [7], [5], [9], [1], [8], [3, 8], [10, 9, 4], [2], [6], []]
    # graph_1 =     [[], [4], [8], [6], [7], [2], [9], [1], [5, 6], [7, 3], [7]]
    # kosaraju_dfs_first(graph_1_rev)
    scc = kosaraju_main(graph, graph_rev, num_nodes)
    scc.sort(reverse=True)
    print(scc[:5])