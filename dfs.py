# the searcher works on simple trees with no closed loops

# here are a couple of test graphs
test_graph = {
    'A': ['B', 'C'], 
    'B' : ['D', 'E', 'F'], 
    'C': ['G'], 
    'G': ['H'],  
}
# this one has a loop, so the searcher gets stuck
test_graph_2 = {
    'A': ['B', 'C', 'D'], 
    'B': ['E'],
    'C': ['E', 'F', 'G'], 
    'G': ['I', 'J'],
    'J': ['K', 'L'],
}

def depth_first_searcher(node_wanted, graph):
    """recursive left-first depth-first search function"""
    # initial condition
    connected_nodes = graph['A']

    def finder(connected_nodes): 
        for node in connected_nodes:
            if node == node_wanted:
                print node
            else:
                if graph.has_key(node):
                    connected_nodes = graph[node]
                    finder(connected_nodes)

    finder(connected_nodes)

# could figure out its path as well by appending the 
# nodes it visits to a list    
depth_first_searcher('D', test_graph)        
depth_first_searcher('M', test_graph)
depth_first_searcher('B', test_graph_2)