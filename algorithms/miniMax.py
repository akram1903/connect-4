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
    
    def __init__(self):
        pass

    def solve(self,state:State,depth:int,maximizingPlayer:bool)->list[int,State]:
        # maximizing is AI ,minimizing is human
        if depth == 1:
            if maximizingPlayer:
                state.makeChildren(2)
                maxEvaState = None

                for i in range(len(state.children)):
                    if maxEvaState is None or state.children[i].Heuristic() > maxEvaState[1].Heuristic():
                        maxEvaState = [i,state.children[i]]

                if maxEvaState is not None:
                    return maxEvaState
                return [state.parCol,state.Heuristic()]
            
            else:
                minEvaState = None

                state.makeChildren(1)
                for i in range(len(state.children)):
                    if minEvaState is None or state.children[i].Heuristic() < minEvaState[1].Heuristic():
                        minEvaState = [i,state.children[i]]

                if minEvaState is not None:
                    return minEvaState
                
                return [state.parCol,state.Heuristic()]

        if maximizingPlayer:
            state.makeChildren(2)
            maxEvaState = None

            for i in range(len(state.children)):
                evaState = self.solve(state.children[i],depth-1,False)
                if maxEvaState is None or evaState[1].Heuristic() > maxEvaState[1].Heuristic():
                    maxEvaState = evaState


            if maxEvaState is not None:
                return maxEvaState

            return [state.parCol,state.Heuristic()]
        else:
            minEvaState = None

            state.makeChildren(1)
            for i in range(len(state.children)):
                evaState = self.solve(state.children[i],depth-1,True)
                if minEvaState is None or evaState[1].Heuristic() < minEvaState[1].Heuristic():
                    minEvaState = evaState

            if minEvaState is not None: 
                return minEvaState
            
            return [state.parCol,state.Heuristic()]
        

if __name__ == "__main__":
    test = State(12121)
    print(test)
    alg = MiniMax()
    result = alg.solve(test,3,True)

    print(result[0])
    print(result[1])