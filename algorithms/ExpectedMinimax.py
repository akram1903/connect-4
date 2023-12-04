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
import random
class ExpectiMiniMax:
    
    def __init__(self):
        pass
    # try
    r = random.randint(1,10)
            # 1 and 2 left -- 3 to 8 mid -- 9 and 10 right
        if r < 3:
            if tmpCol == 6:
                tmpCol -= 1
            else:
                tmpCol += 1
        elif r > 9:
            if tmpCol == 0:
                tmpCol += 1
            else:
                tmpCol -= 1


    # end try
    
    def solve(self,state:State,depth:int,maximizingPlayer:bool,alpha:int=float('-inf'),beta:int=float('inf'))->list[int,State]:
        # maximizing is AI ,minimizing is human
        if depth == 1:
            if maximizingPlayer:
                state.makeChildren(2)
                maxEvaState = None

            
                for i in range(len(state.children)):
                    if maxEvaState is None or state.children[i].Heuristic() > maxEvaState[1].Heuristic():
                        maxEvaState = [state.children[i].parCol,state.children[i]]
                        alpha = state.children[i].Heuristic()
                        if beta <= alpha:
                            break

                if maxEvaState is not None:
                    return maxEvaState
                return [state.parCol,state]
            
            else:
                minEvaState = None

                state.makeChildren(1)
    
                for i in range(len(state.children)):
                    if minEvaState is None or state.children[i].Heuristic() < minEvaState[1].Heuristic():
                        minEvaState = [state.children[i].parCol,state.children[i]]
                        beta = state.children[i].Heuristic()
                        if beta <= alpha:
                            break

                if minEvaState is not None:
                    return minEvaState
                
                return [state.parCol,state]

        if maximizingPlayer:
            state.makeChildren(2)
            maxEvaState = None

            for i in range(len(state.children)):
                evaState = self.solve(state.children[i],depth-1,False,alpha,beta)
                if maxEvaState is None or evaState[1].Heuristic() > maxEvaState[1].Heuristic():
                    maxEvaState = evaState
                    alpha = evaState[1].Heuristic()
                    if beta <= alpha:
                        break

            if maxEvaState is not None:
                return maxEvaState

            return [state.parCol,state]
        else:
            minEvaState = None

            state.makeChildren(1)
            
            for i in range(len(state.children)):
                evaState = self.solve(state.children[i],depth-1,True,alpha,beta)
                if minEvaState is None or evaState[1].Heuristic() < minEvaState[1].Heuristic():
                    minEvaState = evaState
                    beta = evaState[1].Heuristic()
                    if beta <= alpha:
                        break


            if minEvaState is not None: 
                return minEvaState
            
            return [state.parCol,state]
        

if __name__ == "__main__":
    test = State(1111112121212121212121212121122122121212)
    print(test)
    alg = ExpectiMiniMax()
    result = alg.solve(test,3,True)

    print(result[0])
    print(result[1])