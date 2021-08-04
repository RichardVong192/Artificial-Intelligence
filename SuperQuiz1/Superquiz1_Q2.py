from search import *
import heapq
from heapq import *
import math


class RoutingGraph(Graph):
    
    def __init__(self, map_str):
        self.obstacles = ["x", "-", "|", "X"]
        self.list_map = [list(line.strip()) for line in map_str.strip().splitlines()]
        self.goal_nodes = []
    
    def is_goal(self, node):
        """Returns true if the given node is a goal state, false otherwise."""
        return (self.list_map[node[0]][node[1]] == "G")
        
    def starting_nodes(self):
        """Returns a sequence of starting nodes. Often there is only one
        starting node but even then the function returns a sequence
        with one element. It can be implemented as an iterator if
        needed.
        """
        starting_nodes = []
        
        for row in range(len(self.list_map)):                               
            for col in range(len(self.list_map[row])):                     
                if self.list_map[row][col] == "S":                              
                    starting_nodes.append((row, col, math.inf))
                elif self.list_map[row][col] == "G":
                    self.goal_nodes.append((row, col))
                elif self.list_map[row][col].isdigit():
                    starting_nodes.append((row, col, int(self.list_map[row][col])))
        return starting_nodes

    def outgoing_arcs(self, tail_node):
        """Given a node it returns a sequence of arcs (Arc objects)
        which correspond to the actions that can be taken in that
        state (node)."""
        nav_list = [('N' , -1, 0),
                    ('E' ,  0, 1),
                    ('S' ,  1, 0),
                    ('W' ,  0, -1),]
        arcs = []
        move_cost = 5
        fuel_up_cost = 15
        
        for row, col, fuel in [tail_node]:
            for direction, row_movement, col_movement in nav_list:
                next_row = row + row_movement
                next_col = col + col_movement
                
                if fuel > 0 and self.list_map[next_row][next_col] not in self.obstacles:
                    head_node = (next_row, next_col, fuel - 1)
                    yield (Arc(tail_node, head_node, direction, move_cost))
            
            if self.list_map[row][col] == "F" and fuel < 9:
                head_node = (row, col, 9)
                yield (Arc(tail_node, head_node, "Fuel up", fuel_up_cost))

    def estimated_cost_to_goal(self, node):
        """Return the estimated cost to a goal node from the given
        state. This function is usually implemented when there is a
        single goal state. The function is used as a heuristic in
        search. The implementation should make sure that the heuristic
        meets the required criteria for heuristics."""


class AStarFrontier(Frontier):
    
    def __init__(self, map_graph):
        self.frontier = []          #list of all paths
        self.expanded_nodes = set() #list of all expanded nodes
        self.counter = 1            #counter to keep track of heap order
        self.map_graph = map_graph  #initalise map_graph
    
    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method."""
        path_being_explored = path[-1].head
        if path_being_explored not in self.expanded_nodes:      #If path not explored yet
            cost = 0
            for arc in path:                                    #Calculate cost of arc movement
                cost += arc.cost
            heappush(self.frontier, (cost, self.counter, path)) #Add to list of paths
            self.counter += 1

    def __iter__(self):
        """We don't need a separate iterator object. Just return self. You
        don't need to change this method."""
        return self

    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any. Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy. If there nothing to return this should raise a
        StopIteration exception."""
        while len(self.frontier) > 0:                           #Repeated until a path is returned (or frontier becomes empty)
            path = heappop(self.frontier)[2]                    #Path is selected and removed
            end_node = path[-1].head
            if end_node not in self.expanded_nodes:             #If end node not been expanded before
                self.expanded_nodes.add(end_node)               #Add to expanded nodes to know that it has been traversed
                return path                                     #And path is returned
        raise StopIteration      
        
    
def main(): 
    map_str = """\
    +----------------+
    |2              F|
    |XX     G 123    |
    |3XXXXXXXXXXXXXX |
    |  F             |
    |          F     |
    +----------------+
    """
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    #map_str = """\
    #+-------+
    #|  F  X |
    #|X XXXXG|
    #| 3     |
    #+-------+
    #"""
    
    #map_graph = RoutingGraph(map_str)
    #frontier = AStarFrontier(map_graph)
    #solution = next(generic_search(map_graph, frontier), None)
    #print_actions(solution)    

if __name__ == "__main__":
    main()