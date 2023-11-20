
from state import *

class MiniMax:
    
    def __init__(self,currentState:State):
        self.currentState = currentState

    def solve(self,state:State,depth:int,maximizingPlayer:bool)->State:
        if depth == 0:
            return state.heuristic()
        
        if maximizingPlayer:
            maxEvaState:State = None

            for child in self.currentState.children:
                evaState = self.solve(child,depth-1,False)
                if maxEvaState is None or evaState.heuristic() > maxEvaState.heuristic():
                    maxEvaState = evaState

            return maxEvaState
        
        else:
            minEvaState:State = None

            for child in self.currentState.children:
                evaState = self.solve(child,depth-1,True)
                if minEvaState is None or evaState.heuristic() < minEvaState.heuristic():
                    minEvaState = evaState

            return minEvaState