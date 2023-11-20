
# we need to discuss representation of the game
# best representation will be integer representation to reduce space taken


# by convention human coin will be represented as 1, model coin will be represented as 2 and empty place will
# be represented as 0

class State:
    def __init__(self,representation:int,parent=None,children:list=[]):
        self.representation = representation
        self.children = children


    def makeChildren(self,player:int):
        for i in range(7):
            temp = self.insertIntoPuzzle(i,player)
            if temp is not None:
                self.children.append(temp)


    def insertIntoPuzzle(self,colNumber:int,player:int):
        # colNumber should be from 0 to 6
        # player is 1 for human or 2 for ai model
        
        tempList = self.convertRepresentationWithoutReverse()
        if (tempList[5][colNumber]>0):
            print("column is full, you can't push another disk in here")
            return None
        
        row=5
        
        while (row > 0 and tempList[row-1][colNumber]==0):
            row -= 1
            
        return State(parent=self,representation=self.representation+player*(10**colNumber)*(10**7)**row)


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
            while len(tempStr) < 7:
                tempStr = '0' + tempStr
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
    # test = State(0)
    # tset = State(100000000000000000000000000000000000000001)
    # test = State(123456712345671234567123456712345671234567)
    print(test)
    # print(test.convertRepresentation())
    # print(tset)

    
    test.makeChildren(2)
    i=1
    for child in test.children:
        print('child ',i,end='\n\n')
        print(child)
        i += 1
