# -*- coding: utf-8 -*-

def cost(graph, e):
    return graph.edges()[e]['weight']
# Function for check cost on edges, acesses edges.


def is_spanning(graph, subgraph):
    return graph.nodes() == subgraph.nodes()
# Function to check nodes span.


def possible_prims_edges(graph, tree):
    possible_e = []
    for e in set(graph.edges()) - set(tree.edges()):
        for v in tree.nodes():
            if v in e:
                possible_e.append(e)
                
    return possible_e
# Function to check for all possible edges in the nodes, scrolls through the graphs.
    

def min_possible_prims_edge(G, T):
    possible_e = possible_prims_edges(G, T)
    min_e= possible_e[0]
    for e in possible_e:
        if cost(G, e) < cost(G, min_e):
            min_e =e
    return min_e
# function for minimum edges.