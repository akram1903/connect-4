

from tkinter import *


SCALE = 1
window = Tk()

algoIndex = -1

algorithms = ["minimax with prunning","minimax without prunning","expected minimax"]


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

def selectCol(event):
    colSelected = event.x//100
    print(str(event.x),colSelected)

def terminate(event):
    exit()


def drawEnvironment():
    window.geometry(f"{int(SCALE*1000)}x{int(SCALE*700)}")
    window.title("connect 4 with AI")
    window.config(background="#404258")
    window.resizable(False,False)
    
    canvas = Canvas(window,height=600*SCALE,width=700*SCALE,background="#50577A")
    size=50
    for i in range(6):
        for j in range(7):
            canvas.create_oval((5+2*size*j)*SCALE,(5+2*size*i)*SCALE,(2*size*(j+1)-3)*SCALE,(2*size*(i+1)-3)*SCALE,
                               fill='white',outline='white')
    
    # canvas.create_line(0,0,size,size)
    canvas.place(x=250*SCALE,y=10*SCALE)
    canvas.bind('<Button-1>',selectCol)

def selectWithPrun():
    global algoIndex
    algoIndex = 0
    print(algorithms[algoIndex],"selected")

def selectWhithoutPrun():
    global algoIndex
    algoIndex = 1
    print(algorithms[algoIndex],"selected")

def SelectExpectedMinimax():
    global algoIndex
    algoIndex = 2
    print(algorithms[algoIndex],"selected")

# not done yet
def resetPuzzle(event = None):
    algorithm = -1
    


# def buildTile(num):
    
#     global tileIndex,entrySet,startState
#     if tileIndex < 9 :
#         if num not in entrySet:
#             entrySet.add(num)
#             i=tileIndex//3
#             j=tileIndex%3

#             if num is not None:
#                 startState.matrix[i][j] = int(num)
#             else:
#                 startState.matrix[i][j] = None
#             ShowPuzzle(startState)
#             tileIndex += 1
#         else:
#             print("number entered before")
#     if entrySet.__len__()==9:
#         startButton = Button(window,foreground='#D6E4E5',background="#50577A",text='start',command=startSolve,font=('arial',18))
#         startButton.place(x=SCALE*700,y=SCALE*(300))
#         resetButton = Button(window,foreground='#D6E4E5',background="#50577A",text='reset',command=resetPuzzle,font=('arial',14))
#         resetButton.place(x=SCALE*700,y=SCALE*(550))
        

def agentTurn():
    pass

def drawRadioButtons():

    x = IntVar()

    radioB = Radiobutton(window,text=algorithms[0],variable=x,value=0, font=('arial',11),
                        foreground='#D6E4E5',background="#404258",command=selectWithPrun)
    
    radioB.place(x=SCALE*20,y=SCALE*(50))

    radioB = Radiobutton(window,text=algorithms[1],variable=x,value=0, font=('arial',11),
                        foreground='#D6E4E5',background="#404258",command=selectWhithoutPrun)
    
    radioB.place(x=SCALE*20,y=SCALE*(50*2))

    radioB = Radiobutton(window,text=algorithms[2],variable=x,value=0, font=('arial',11),
                        foreground='#D6E4E5',background="#404258",command=SelectExpectedMinimax)
    
    radioB.place(x=SCALE*20,y=SCALE*(50*3))


if __name__ == "__main__":

    
    drawEnvironment()
    drawRadioButtons()


    # keys to input the puzzle to be solved
    window.bind("<Key>",printKeys)
    
    window.mainloop()