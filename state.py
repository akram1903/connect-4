
# we need to discuss representation of the game
# best representation will be integer representation to reduce space taken


# by convention human coin will be represented as 1, model coin will be represented as 2 and empty place will
# be represented as 0

class State:
    def __init__(self,representation:int,parent=None,children=None):
        self.representation = representation
        self.children = children
    
    def convertRepresentation(self)->list:
        temp = self.representation

        result = []

        for i in range(6):
            tempList =[]
            for j in range(7):
                tempList.append(temp%10)
                temp //= 10
            result.append(tempList)

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

    test = State(111111122222221111111222222211111112222222)
    test = State(1111)
    # tset = State(100000000000000000000000000000000000000001)
    # test = State(123456712345671234567123456712345671234567)
    print(test)
    print(test.convertRepresentation())
    # print(tset)
