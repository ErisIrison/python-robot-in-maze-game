# The following line imports the game function library and map into
# this main program
from game_lib import *

# This is the only 'memory' of the robot that you can use to store things
#
# You are expected to use it to store only a string, which indicates the
# current 'state' of the robot

stateForTask4 = "Find a wall first!"

# These functions helps the robot to make the decision about what it needs
# to do in order to get to the exit of the map
# 
# The function should return one of the following:
#     "UP"     which means the robot decides to go up
#     "LEFT"   which means the robot decides to go left
#     "RIGHT"  which means the robot decides to go right
#     "DOWN"   which means the robot decides to go down
#     "NONE"   which means the robot decides to stay in the same place

# Your task is to help the robot to make a decision on what to do next.
#
# A collection of functions that you will find very useful here:
#
#    leftIsWall()   returns True if the robot detects that the left side is blocked, otherwise it returns False
#    rightIsWall()	returns True if the robot detects that the right side is blocked, otherwise it returns False
#    upIsWall()	returns True if the robot detects that the up side is blocked, otherwise it returns False
#    downIsWall()	returns True if the robot detects that the down side is blocked, otherwise it returns False


def makeDecisionForTask4():
    global stateForTask4

    # You need to add your code here for task 4
    
##            elif not rightIsWall() and not leftIsWall() and not upIsWall() and not downIsWall():
##                stateForTask4 = "Space"
##                return "NONE"
        
        
    stateForTask4 = "Find a wall first!"
def makeDecisionForTask4():
    global stateForTask4
    if stateForTask4 == "Find a wall first!":
        if leftIsWall():
            stateForTask4 = "Go up"
        else:
            return "LEFT"
    elif stateForTask4 == "Go up":
        if leftIsWall():
            stateForTask4 = "Go right"
        else:
            stateForTask4 = "Go left"
            return "LEFT"
    elif stateForTask4 == "Go down":
        if rightIsWall():
            stateForTask4 = "Go left"
        else:
            stateForTask4 = "Go right"
            return "RIGHT"
    elif stateForTask4 == "Go left":
        if downIsWall():
            stateForTask4 = "Go up"
        else:
            stateForTask4 = "Go down"
            return "DOWN"
    elif stateForTask4 == "Go right":
        if upIsWall():
            stateForTask4 = "Go down"
        else:
            stateForTask4 = "Go up"
            return "UP"
    return "NONE"
            
        
        
        
    # This gets replaced with your logic




# The following line of code chooses the map of the game before it starts
# 
# You can change the map of the game by changing the parameters:
# 
# - Parameter 1 can be either:
#   - "task0", "Task4", "task2", "task3", "task4" or "task5"
#     which mean the predefined maps from the task that you want to work on
#
#   - "custom"
#     which means any customized map(s) that you can add in game_map.py
#
# - Parameter 2 is a number representing the map you want to use
chooseGameMap("task4", 0)

#####
#
# !!! You DO NOT need to change anything from this point onwards
#
#####

# Using the makeDecision function to set the Decision function used in each of the tasks

setDecisionFuncForTask4(makeDecisionForTask4)


# Start the game
startGame()
