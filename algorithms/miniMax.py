import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)
 
# now we can import the module in the parent
# directory.
from state import State

class MiniMax:
    
    def __init__(self,currentState:State):
        self.currentState = currentState

    def solve(self,state:State,depth:int,maximizingPlayer:bool)->State:
        # maximizing is AI ,minimizing is human
        if depth == 1:
            if maximizingPlayer:
                state.makeChildren(2)
                maxEvaState:State = None

                for child in state.children:
                    if maxEvaState is None or child.heuristic() > maxEvaState.heuristic():
                        maxEvaState = child

                return maxEvaState
            
            else:
                minEvaState:State = None

                state.makeChildren(1)
                for child in state.children:
                    if minEvaState is None or child.heuristic() < minEvaState.heuristic():
                        minEvaState = child

                return minEvaState
        
        if maximizingPlayer:
            state.makeChildren(2)
            maxEvaState:State = None

            for child in state.children:
                evaState = self.solve(child,depth-1,False)
                if maxEvaState is None or evaState.heuristic() > maxEvaState.heuristic():
                    maxEvaState = evaState

            return maxEvaState
        
        else:
            minEvaState:State = None

            state.makeChildren(1)
            for child in state.children:
                evaState = self.solve(child,depth-1,True)
                if minEvaState is None or evaState.heuristic() < minEvaState.heuristic():
                    minEvaState = evaState

            return minEvaState
        

if __name__ == "__main__":
    test = State(1000)
    print(test)
    alg = MiniMax(test)
    result = alg.solve(test,4,True)

    print(result)