import sys
from collections import deque

test_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'F', 'G'],
    'C': ['H'],
    'G': ['I', 'J'],
    'H': ['K', 'L'],
}

def breadth_first_searcher(node_wanted, graph):
    """ Iterative function uses a queue to carry out a
    breadth-first search. Uncomment the print statements to watch
    the search. """

    Q = deque()
    Q.append('A')

    while len(Q) > 0:
        current_node = Q.popleft()
        if current_node == node_wanted:
            print current_node
            sys.exit()
        else:
            # print "Current node is: %r" % current_node
            if graph.has_key(current_node):
                # print "Adding more nodes on this level..."
                for node in graph[current_node]:
                    Q.append(node)
                # print "Queue is: %r" % Q


# try it out!
breadth_first_searcher('L', test_tree)
