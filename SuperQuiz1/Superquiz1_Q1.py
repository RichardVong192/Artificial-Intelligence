from search import *
import math

class RoutingGraph(Graph):
    def __init__(self, map_str):
        self.obstacles = ["x", "-", "|", "X"]
        self.list_map = [list(line.strip()) for line in map_str.strip().splitlines()]
    
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

        raise NotImplementedError
    
    

def main(): 
    map_str = """\
    +-------+
    |  9  XG|
    |X XXX  |
    | S  0FG|
    +-------+
    """
    
    graph = RoutingGraph(map_str)
    
    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Outgoing arcs (available actions) at starting states:")
    for s in sorted(graph.starting_nodes()):
        print(s)
        for arc in graph.outgoing_arcs(s):
            print ("  " + str(arc))
    
    node = (1,1,5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))
    
    node = (1,7,2)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))
    
    node = (3, 7, 0)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    
    node = (3, 7, math.inf)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    
    node = (3,6,5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))
    
    node = (3,6,9)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))
        
if __name__ == "__main__":
    main()