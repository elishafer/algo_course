__author__ = 'Elisei Shafer'

import csv
from random import choice
from copy import deepcopy

def load_file(file_name):
    nodes = {}
    with open(file_name, 'r') as f:
        data_reader = csv.reader(f, delimiter='\t')
        for i, items in enumerate(data_reader):
            node = []
            for item in items[1:]:
                node += [int(v) for v in item.split(',') if v.isdigit()]
            node = list(filter(None, node))
            nodes[i+1] = node
    return nodes


def karger(vertices):
    cut = len(vertices)
    nodes = deepcopy(vertices)

    while len(nodes) > 2:
        # pick (u,v) edge at random
        u, vs = choice(list(nodes.items()))
        v = choice(vs)
        # merge u and v into single node
        nodes[u] += nodes.pop(v)
        # Update edges to new single node:
        for key in nodes.keys():
            nodes[key] = [w if w != v else u for w in nodes[key]]
        # remove self-loops
        nodes[u] = [v for v in nodes[u] if v != u]


    cut = len(nodes[u])
    return cut


if __name__ == '__main__':
    nodes = load_file('kargerMinCut.txt')
    # nodes = {1: [2,3],
    #          2: [1,3,4],
    #          3: [1,2,4],
    #          4: [2,3]}
    min_cut = 200
    for x in range(100):
        cut = karger(nodes)
        min_cut = min(cut, min_cut)
    print(min_cut)