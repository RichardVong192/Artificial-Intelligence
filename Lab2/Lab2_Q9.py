from search import *
import math
import heapq

class LocationGraph(ExplicitGraph):
    """This is a concrete subclass of Graph where vertices and edges
     are explicitly enumerated. Objects of this type are useful for
     testing graph algorithms."""

    def __init__(self, nodes, edges, starting_nodes, goal_nodes, locations):
        """Initialises an location graph.
        Keyword arguments:
        nodes -- a set of nodes
        edges -- a sequence of tuples in the form (tail, head) or 
                     (tail, head, cost)
        starting_nodes -- the list of starting nodes. We use a list
                          to remind you that the order can influence
                          the search behaviour.
        goal_node -- the set of goal nodes. It's better if you use a set
                     here to remind yourself that the order does not matter
                     here. This is used only by the is_goal method. 
        """
        #make new set for all edges
        #loop through edges
        #for each edge calculate distance which will be the cost
        #add edge from tail to head with cost and head to tail to new set
        self.edges = edges
        self.locations = locations
        self._starting_nodes = starting_nodes
        aSet = set()
        for edge in self.edges:
            distance = math.sqrt( ((locations.get(edge[0])[0]-locations.get(edge[1])[0])**2)+((locations.get(edge[0])[1]-locations.get(edge[1])[1])**2) )
            aSet.add((edge[0], edge[1], distance))
            aSet.add((edge[1], edge[0], distance))
        self.edges = aSet
        
        super(LocationGraph, self).__init__(nodes = nodes, edge_list = self.edges, starting_nodes=starting_nodes, goal_nodes=goal_nodes)
            


    def outgoing_arcs(self, node):
        """Returns a sequence of Arc objects that go out from the given
        node. The action string is automatically generated.

        Need to make Bi-directionional
        Need to calculate cost based on euleadian distance
        """
        arcs = []
        for edge in self.edges:
            if len(edge) == 2:  # if no cost is specified
                tail, head = edge
                cost = 1        # assume unit cost
            else:
                tail, head, cost = edge
            if tail == node:
                arcs.append(Arc(tail, head, str(tail) + '->' + str(head), cost))
        return sorted(arcs, key=lambda x: x[2]) #sorts by action


class LCFSFrontier():
    """This is an abstract class for frontier classes. It outlines the
    methods that must be implemented by a concrete subclass. Concrete
    subclasses determine the search strategy.

    """
    def __init__(self):
        self.container = []

    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method.
        """
        #loop through arcs in path and sum cost
        #add to heap with .heapPush() (cost,path)
        cost = 0
        for arcs in path:
            cost += arcs[3]
        heapq.heappush(self.container,(cost, path))

    def __iter__(self):
        """We don't need a separate iterator object. Just return self. You
        don't need to change this method."""
        return self
    
    def __next__(self):
        if len(self.container) > 0:
            return heapq.heappop(self.container)[1] #index refers to the last value of heap i think
        else:
            raise StopIteration   # don't change this one        

graph = LocationGraph(nodes=set('ABC'),
                      locations={'A': (0, 0),
                                 'B': (3, 0),
                                 'C': (3, 4)},
                      edges={('A', 'B'), ('B','C'),
                             ('B', 'A'), ('C', 'A')},
                      starting_nodes=['A'],
                      goal_nodes={'C'})

solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)

print("==============")

graph = LocationGraph(nodes=set('ABC'),
                      locations={'A': (0, 0),
                                 'B': (3, 0),
                                 'C': (3, 4)},
                      edges={('A', 'B'), ('B','C'),
                             ('B', 'A')},
                      starting_nodes=['A'],
                      goal_nodes={'C'})

solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)

print("============")

pythagorean_graph = LocationGraph(
    nodes=set("abc"),
    locations={'a': (5, 6),
               'b': (10,6),
               'c': (10,18)},
    edges={tuple(s) for s in {'ab', 'ac', 'bc'}},
    starting_nodes=['a'],
    goal_nodes={'c'})

solution = next(generic_search(pythagorean_graph, LCFSFrontier()))
print_actions(solution)