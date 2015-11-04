# the searcher works on simple trees with no closed loops
import sys

# here is a test tree
test_tree = {
    'A': ['B', 'C'],
    'B' : ['D', 'E', 'F'],
    'C': ['G'],
    'G': ['H'],
}


def depth_first_searcher(node_wanted, graph):
    """A recursive left-first depth-first search function.
     Uncomment the print statement in the finder function
     to print the path as it searches."""
    connected_nodes = graph['A']

    def finder(connected_nodes):
        for node in connected_nodes:
            if node == node_wanted:
                print node
                sys.exit()
            else:
                if graph.has_key(node):
                    connected_nodes = graph[node]
                    print "[%r] => %r" % (node, graph[node])
                    finder(connected_nodes)

    finder(connected_nodes)

# run on a node that's not in the tree
depth_first_searcher('M', test_tree)
# # run on a node that is in the tree
depth_first_searcher('G', test_tree)
