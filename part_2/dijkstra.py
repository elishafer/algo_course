__author__ = 'Elisei Shafer'

import csv

def load_file(file_name):
    nodes = [[]]
    with open(file_name, 'r') as f:
        data_reader = csv.reader(f, delimiter='\t')
        for i, items in enumerate(data_reader):
            node = []
            for item in items[1:]:
                node += [[int(v) for v in item.split(',') if v.isdigit()]]
            node = list(filter(None, node))
            nodes.append(node)
    return nodes

def dijkstra(nodes):
    source = 1
    parents = [None] * len(nodes)
    cost = [None] * len(nodes)
    visited = [False] * len(nodes)
    current_node = source
    cost[current_node] = 0
    visited[current_node] = True
    i = 1
    while i < len(nodes)-1:
        min_cost = float('Inf')
        for v, node in enumerate(nodes):
            if visited[v]:
                for adj_node in node:
                    if not visited[adj_node[0]]:
                        if cost[v] + adj_node[1] < min_cost:
                            parent_node = v
                            min_cost = cost[v] + adj_node[1]
                            min_cost_node = adj_node[0]
        cost[min_cost_node] = min_cost
        visited[min_cost_node] = True
        parents[min_cost_node] = parent_node

        i +=1

    return cost


if __name__ == '__main__':
    file_name = 'dijkstraData.txt'
    v = load_file(file_name)
    costs = dijkstra(v)
    hw_nodes = [7,37,59,82,99,115,133,165,188,197]
    hw_costs = [cost for v,cost in enumerate(costs) if v in hw_nodes]
    print(hw_costs)