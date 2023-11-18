
from state import *

class WithoutPrune:
    
    def __init__(self,currentState:State):
        self.currentState = currentState

    def solve(self,state:State,depth:int,maximizingPlayer:bool)->State:
        if depth == 0:
            return state.heuristic()
        
        if maximizingPlayer:
            maxEva = float('-inf')

            for child in self.currentState.children:
                eva = self.solve(child,depth-1,False)
                if eva > maxEva:
                    maxEva = eva