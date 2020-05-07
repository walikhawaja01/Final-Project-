import networkx as nx
from functions.drawings import draw_subtree
from functions.prims_functions import cost, min_prims_edge


def prims_algoritm(G, starting_node, draw= False, attrib = False):
    
    T= nx.Graph()
    T.add_nodes(starting_node)
    
    
    if draw == True:
        draw_subtree(G, T)
    while set(T.nodes()) != set(G.nodes()):
        e= min_prims_edge(G, T)
        T.add_edge([0], e[1], weight = cost(G,e))
        if draw == True:
            draw_subtree(G, T)
    if attrib == True:
       total_cost = sum(cost(G, e) for e in T.edges())
       print('')
       print('-----------------PROERTIES OF THE TREE T-----------')
       print('---------------------------------------------------')
       print(f'V(T) ={list(T.nodes())}')
       print(f'E(T) ={list(T.edges())}')
       print(f'Total Cost = {total_cost}')
       print('---------------------------------------------------')
    
    return T

# Function for Prim algorithm at the starting node. 
# imports from subtree as well as prim cost function and minumum node edge.