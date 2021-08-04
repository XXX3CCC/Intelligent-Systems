"""
Solution stub for the River Problem.

Fill in the implementation of the `River_problem` class to match the
representation that you specified in problem XYZ.
"""
from searchProblem import Search_problem, Arc

class River_problem(Search_problem):
    def start_node(self):
        """returns start node"""
        #TODO
        #'[]' represents different sides of the river
        #The farmer starts from the left side of the river with three items
        #The right side of the river is empty at the beginning
        left = ['Farmer','Fox','Hen','Grain']
        right = []
        return (left, right)
    
    def is_goal(self,node):
        """is True if node is a goal"""
        #TODO
        #since in run.py: 'assert not prob.is_goal(prob.start_node())'
        #node is the element in def start_node(self)
        #which means '['Farmer','Fox','Hen','Grain'],[]'
        #node[0] means the left side of the river, and node[1] means the right side of the river
        #The goal is that the farmer move all three items from the left side to the right side
        #So that when node[1] has ['Farmer','Fox','Hen','Grain'] return true
        #which satisfies the goal
        if 'Farmer' in node[1] and 'Fox' in node[1] and 'Hen' in node[1] and 'Grain' in node[1]:
            return True
        else:
            return False # dummy goal, state has two items in it

    def neighbors(self,node):
        """returns a list of the arcs for the neighbors of node"""
        #TODO
        #Record the position of the farmer
        if 'Farmer' in node[0]:
            position = 0   #in the left side 
        else:
            position = 1   #in the right side

        #returns a list of the arcs for the neighbors of node
        #set result list [Arc(node, node+(None,), 1, 'ADD-NONE')]
        result = []
        for i in node[position]:
            #State after moving item i
            state1 = node[position][:]
            state1.remove(i)
            #Since the farmer have to take the item, he/she will go to the opposite side
            if i != 'Farmer':
                state1.remove('Farmer')

            #Another side's state
            opposite = 1 - position
            state2 = node[opposite][:]
            state2.extend([i])
            #state2.append(i)
            #Since the farmer have to take the item, he/she will go to this side
            if i != 'Farmer':
                state2.append('Farmer')

            #Actions of the farmer
            #if item is the farmer, it means that the farmer will go alone
            if i == 'Farmer':
                action = 'ADD-NONE'
            #if item is not the farmer, the item will be moved by the farmer
            else:
                action = 'ADD-' + i

            #limitation factors
            #1. The hen cannot be left alone with the grain, or it will eat the grain.
            #2. The fox cannot be left alone with the hex, or it will eat the hen.
            if 'Hen' in state1 and 'Grain' in state1 and 'Farmer' not in state1:
                continue
            elif 'Hen' in state2 and 'Grain' in state2 and 'Farmer' not in state2:
                continue
            elif 'Fox' in state1 and 'Hen' in state1 and 'Farmer' not in state1:
                continue
            elif 'Fox' in state2 and 'Hen' in state2 and 'Farmer' not in state2:
                continue

            #[Arc(node, node+(None,), 1, 'ADD-NONE')]
            if position == 0:
                result.append(Arc(node, (state1, state2), 1, action))
            else:
                result.append(Arc(node, (state2, state1), 1, action))

        return result

    def heuristic(self,n):
        """Gives the heuristic value of node n."""
        #when the farmer starts in the left side
        #there are n items left in the left
        #the farmer will at least move 2n-1 times
        #Record the position of the farmer
        if 'Farmer' in n[0]:
            position = 0   #in the left side 
            return 2 * len(n[position]) - 1
        #when the farmer starts in the right side
        #there are n items left in the right
        #the farmer will at least move 2n times
        else:
            position = 1   #in the right side
            return 2 * len(n[position])
    

