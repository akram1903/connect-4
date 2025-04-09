

from tkinter import *
import time
from state import *
from algorithms.miniMax import *
from algorithms.ExpectedMinimax import *
from algorithms.minimaxWithAlpha import *
import random
from newMiniMax import MiniMaxNew

TEST_COUNTER=1
SCALE = 1
SIZE=50
respond:bool = True
window = Tk()
canvas = Canvas(window,height=600*SCALE,width=700*SCALE,background="#50577A")

# data collection for report
countAgentPlays = 0
avgResponseTime = None
# end data collection


current_state = State(0)
    
algoIndex = -1
agent = None
algorithms = ["minimax with prunning","minimax without prunning","new minimax"]


def drag_start(event):
    widget = event.widget
    widget.startX=event.x
    widget.startY=event.y
    widget.place(x=widget.winfo_x())
    
def drag_motion(event):
    widget = event.widget
    x=widget.winfo_x() - widget.startX + event.x
    y=widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)


def insertIntoPuzzle(colNumber:int,player:int):
    #colNumber should be from 0 to 6
    #player is 1 for human or 2 for ai model
    global window ,current_state
    
    tempList = current_state.convertRepresentationWithoutReverse()
    if (tempList[5][colNumber]>0):
        print("column is full, you can't push another disk in here")
        return False
    
    row=5
    drawState(current_state.representation+player*(10**colNumber)*(10**7)**row)
    window.update()
    time.sleep(.5)
    
    while (row > 0 and tempList[row-1][colNumber]==0):
        row -= 1
        drawState(current_state.representation+player*(10**colNumber)*(10**7)**row)
        window.update()
        time.sleep(.5)

    prev_state = current_state
    current_state = State(parent=current_state,representation=prev_state.representation+player*(10**colNumber)*(10**7)**row)
    print(current_state)
    
    return True

# def goBack(event):
#     global solutionIndex
#     if solutionIndex < solutionPath.__len__()-1:
#         solutionIndex += 1
#         print("back")
#         ShowPuzzle(solutionPath[solutionIndex])
    

# def goForward(event):
#     global solutionIndex
#     if solutionIndex > 0:
#         solutionIndex -= 1
#         ShowPuzzle(solutionPath[solutionIndex])
#         print("forward")


def printKeys(event):
    print(event.keysym+" key pressed")

def checkFinished():
    global current_state

    tmp = current_state.convertRepresentationWithoutReverse()

    for i in range(6):
        for j in range(7):
            if tmp[i][j]==0:
                return False
            
    return True

def calculateWinner():
    global current_state
    temp = current_state.convertRepresentationWithoutReverse()
    player = 2
    opponent = 1
    player_score = 0
    opponent_score = 0

    # Evaluate horizontally
    for row in range(6):
        for col in range(7 - 3):
            window = [temp[row][col + i] for i in range(4)]
            player_count = window.count(player)
            opponent_count = window.count(opponent)
            if player_count == 4:
                player_score += 100

            if opponent_count == 4:
                opponent_score += 100
            
    # Evaluate vertically
    for col in range(7):
        for row in range(6 - 3):
            window = [temp[row + i][col] for i in range(4)]
            player_count = window.count(player)
            opponent_count = window.count(opponent)
            if player_count == 4:
                player_score += 100
            

            if opponent_count == 4:
                opponent_score += 100
            

    # Evaluate diagonally (top-left to bottom-right)
    for row in range(6 - 3):
        for col in range(7 - 3):
            window = [temp[row + i][col + i] for i in range(4)]
            player_count = window.count(player)
            opponent_count = window.count(opponent)
            if player_count == 4:
                player_score += 100
            
            if opponent_count == 4:
                opponent_score += 100
            

    # Evaluate diagonally (bottom-left to top-right)
    for row in range(3, 6):
        for col in range(7 - 3):
            window = [temp[row - i][col + i] for i in range(4)]
            player_count = window.count(player)
            opponent_count = window.count(opponent)
            if player_count == 4:
                player_score += 100
            

            if opponent_count == 4:
                opponent_score += 100
            

    if player_score-opponent_score == 0:
        return 0
    elif player_score-opponent_score < 0:
        return 1
    else:
        return 2

def finishGame():
    global current_state,notificationLabel
    
    result = calculateWinner()

    if result == 1:
        print('human won')
        notificationLabel.config(text='human won')
    elif result == 2:
        print('ai won')
        notificationLabel.config(text='ai won')
    else:
        print('tie')
        notificationLabel.config(text='tie')
        
def selectCol(event):
    global respond
    if respond:
        respond = False
        colSelected = 6 - (event.x//100)
        print('index of column selected:',colSelected)

        # if algoIndex==2:
        #     r = random.randint(1,10)
        #     expCol = colSelected
        #     # 1 and 2 left -- 3 to 8 mid -- 9 and 10 right
        #     if r < 3:
        #         if expCol == 6:
        #             expCol -= 1
        #         else:
        #             expCol += 1
        #     elif r > 9:
        #         if expCol == 0:
        #             expCol += 1
        #         else:
        #             expCol -= 1

        #     print('col index after tripping ',colSelected)

            # if not insertIntoPuzzle(expCol,1):
            #     insertIntoPuzzle(colSelected,1)
        # else:
        insertIntoPuzzle(colSelected,1)
            

        agentTurn()

        if checkFinished():
            finishGame()
            return
        respond = True



def terminate(event):
    exit()

def drawState(representation:int):

    global canvas
    tempInt = representation
    for i in range(5,-1,-1):
        for j in range(6,-1,-1):
            if tempInt % 10 == 0:
                color = 'white'
            elif tempInt % 10 == 1:
                color = 'yellow'
            else:
                color = 'red'
            canvas.create_oval((5+2*SIZE*j)*SCALE,(5+2*SIZE*i)*SCALE,(2*SIZE*(j+1)-3)*SCALE,(2*SIZE*(i+1)-3)*SCALE,
                               fill=color,outline=color)
            tempInt //= 10

def drawEnvironment():
    window.geometry(f"{int(SCALE*1000)}x{int(SCALE*700)}")
    window.title("connect 4 with AI")
    window.config(background="#404258")
    window.resizable(False,False)
    
    global notificationLabel
    notificationLabel = Label(window,text="notification label",font=('Arial',11),foreground='#D6E4E5',background="#404258")
    notificationLabel.place(x=10*SCALE,y=400*SCALE)

    lable = Label(window,text="avg response time = ",font=('Arial',11),foreground='#D6E4E5',background="#404258")
    lable.place(x=450*SCALE,y=640*SCALE)

    global dataCollectionLable
    dataCollectionLable = Label(window,text="",font=('Arial',11),foreground='#D6E4E5',background="#404258")
    dataCollectionLable.place(x=600,y=640*SCALE)
    # dataCollectionLable.config
        
    drawState(current_state.representation)
    

def selectWithPrun():
    global algoIndex
    algoIndex = 0
    print(algorithms[algoIndex],"selected")

def selectWhithoutPrun():
    global algoIndex,agent
    algoIndex = 1
    
    print(algorithms[algoIndex],"selected")

def SelectNewMinimax():
    global algoIndex
    algoIndex = 2
    print(algorithms[algoIndex],"selected")

def resetPuzzle(event = None):
    algorithm = -1
    drawState(0)
    

def agentTurn():
    global agent,current_state,dataCollectionLable,countAgentPlays,avgResponseTime

    current_state.children = []
    current_state.parent = None
    if agent is None:
        if algoIndex==1:
            agent = MiniMax()
        elif algoIndex==0:
            agent = MiniMaxWithAlpha()
           
        elif algoIndex==2:
            agent = MiniMaxNew()
           

        else:
            print("no agent selected","select an agent to start game",sep='\n')
            current_state = State(0)
            drawState(0)
            return
    maxDepth = 5

    startTime = time.time()    
    answer = agent.solve(current_state,maxDepth,True)
    t = time.time()-startTime
    # print_tree(current_state)

    if avgResponseTime is None:
        avgResponseTime = t
    else:
        avgResponseTime = (avgResponseTime*countAgentPlays+t)/(countAgentPlays+1)
    countAgentPlays += 1
    dataCollectionLable.config(text=f'{avgResponseTime} secs')

    # if algoIndex == 2:
    #     tmpCol = answer[0]
    #     r = random.randint(1,10)
    #         # 1 and 2 left -- 3 to 8 mid -- 9 and 10 right
    #     if r < 3:
    #         if tmpCol == 6:
    #             tmpCol -= 1
    #         else:
    #             tmpCol += 1
    #     elif r > 9:
    #         if tmpCol == 0:
    #             tmpCol += 1
    #         else:
    #             tmpCol -= 1
                
    #     print('col index after tripping ',tmpCol)

    #     if(not insertIntoPuzzle(tmpCol,2)):
    #         insertIntoPuzzle(answer[0],2)

    # else:
    insertIntoPuzzle(answer[0],2)

def drawRadioButtons():

    x = IntVar()

    radioB = Radiobutton(window,text=algorithms[0],variable=x,value=0, font=('arial',11),
                        foreground='#D6E4E5',background="#404258",command=selectWithPrun)
    
    radioB.place(x=SCALE*20,y=SCALE*(50))

    radioB = Radiobutton(window,text=algorithms[1],variable=x,value=0, font=('arial',11),
                        foreground='#D6E4E5',background="#404258",command=selectWhithoutPrun)
    
    radioB.place(x=SCALE*20,y=SCALE*(50*2))

    radioB = Radiobutton(window,text=algorithms[2],variable=x,value=0, font=('arial',11),
                        foreground='#D6E4E5',background="#404258",command=SelectNewMinimax)
    
    radioB.place(x=SCALE*20,y=SCALE*(50*3))


def test(event):
    global TEST_COUNTER
    drawState(TEST_COUNTER)
    TEST_COUNTER += 2
    TEST_COUNTER *= 10

if __name__ == "__main__":

    
    drawEnvironment()
    drawRadioButtons()
    
    # keys to input the puzzle to be solved
    window.bind("<Key>",printKeys)
    canvas.place(x=250*SCALE,y=10*SCALE)
    canvas.bind('<Button-1>',selectCol)
    # key to test any action
    window.bind("<Return>",test)
    window.mainloop()
