
# we need to discuss representation of the game
# best representation will be integer representation to reduce space taken


# by convention human coin will be represented as 1, model coin will be represented as 2 and empty place will
# be represented as 0

class State:
    def __init__(self,representation:int,parent=None,children:list=None):
        self.representation = representation
        self.children = children


    # def makeChildren(self):
    #     for i in range(6):
    #         for j in range(7):
    #             if (self.representation//)%10<
    #             self.children.append(State(self.representation+j*((10**7)**i)))


    def insertIntoPuzzle(self,colNumber:int,player:int):
        #colNumber should be from 0 to 6
        #player is 1 for human or 2 for ai model
        row=5
        tempList = self.convertRepresentationWithoutReverse()
        while (row > 0 and tempList[row-1][colNumber]==0):
            row -= 1
            
        return State(self.representation+player*(10**colNumber)*(10**7)**row)
        # prev_state = current_state
        # current_state = State(parent=current_state,representation=prev_state.representation+player*(10**colNumber)*(10**7)**row)
        
        # print(current_state)

    def convertRepresentation(self)->list:
        temp = self.representation

        result = []

        for i in range(6):
            tempList =[]
            for j in range(7):
                tempList.append(temp%10)
                temp //= 10
            result.append(tempList)
        for sublist in result:
               sublist.reverse()
                  
        result.reverse()    

        return result
    

    def convertRepresentationWithoutReverse(self)->list:
        temp = self.representation

        result = []

        for i in range(6):
            tempList =[]
            for j in range(7):
                tempList.append(temp%10)
                temp //= 10
            result.append(tempList)
        # for sublist in result:
        #        sublist.reverse()
                  
        # result.reverse()    

        return result
    
    def __str__(self) -> str:
        tempInt = self.representation
        result:str ='\n'
        for i in range(6):
            tempStr = str(tempInt%(10**7))
            result += tempStr[::-1]+'\n'
            tempInt = tempInt//(10**7)
        result = result[::-1]
        return result

    def __hash__(self) -> int:
        return self.representation
    
    # should be discussed
    def heuristic(self) -> int:
        pass
    
    
if __name__ == "__main__":

    # test = State(111111122222221111111222222211111112222222)
    test = State(101100011011111)
    # tset = State(100000000000000000000000000000000000000001)
    # test = State(123456712345671234567123456712345671234567)
    print(test)
    # print(test.convertRepresentation())
    # print(tset)

    

    print(test.insertIntoPuzzle(6,1))
