from state import State

class MiniMaxNew:
    def __init__(self):
        self.answers:dict[State,list[int]] = {}   # key = state ; value = answer
    def solve(self,state:State,depth:int,maximizingPlayer:bool,alpha=float('-inf'),beta=float('inf'))->list[int,int]:
        answer = self.answers.get(state,None)
        if answer is not None:
            return self.answers[state]
        
        if depth == 0 or state.isTerminal():
            self.answers[state] = state.parCol,state.Heuristic()
            return self.answers[state]
        
        if maximizingPlayer:
            state.makeChildren(2)
            maxEval = float('-inf')
            maxParentCol = None
            for child in state.children:
                if child is None:
                    continue
                childParCol,childEval = self.solve(child,depth-1,False,alpha,beta)
                # maxEval = max(maxEval,eval)
                if maxEval < childEval:
                    maxEval = childEval
                    maxParentCol = childParCol
                alpha = max(alpha,childEval)
                if beta <= alpha:
                    break
            self.answers[state] = [maxParentCol,maxEval]
            return self.answers[state]
        else:
            state.makeChildren(1)
            minEval = float('inf')
            minParentCol = None
            for child in state.children:
                if child is None:
                    continue
                childParCol,childEval = self.solve(child,depth-1,True,alpha,beta)
                if minEval > childEval:
                    minEval = childEval
                    minParentCol = childParCol
                beta = min(beta,childEval)
                if beta <= alpha:
                    break
            self.answers[state] = [minParentCol,minEval]
            return self.answers[state]
