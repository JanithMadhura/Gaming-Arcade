# Tic Tac Toe 
# group name:A19


import time
from pyfirmata import Arduino, util, INPUT, OUTPUT

# Constants
arduino_port = 'COM3'
light_pins = [2, 3, 4, 5, 6, 7, 8, 9, 10]
nav_button_pin = 11
select_button_pin = 12
chances = 2

# variables
lastNavButtonState = False
lastSelectButtonState = False
navigationButtonPosition = 0
currentPlayer = 1
points = [0, 0]
lightStates = [0, 0, 0, 0, 0, 0, 0, 0, 0]
lightsLastBlinkedTime = [0, 0, 0, 0, 0, 0, 0, 0, 0]
lightCanBlink = [False]*9
lightSelected = [0]*9
remainingChance = chances


# connect to the Arduino board
arduinoBoard = Arduino(arduino_port)

# start an iterator
it = util.Iterator(arduinoBoard)
it.start()

# initialize the light pins
for pin in light_pins:
    arduinoBoard.digital[pin].mode = OUTPUT

# set navigate button pin mode to output
arduinoBoard.digital[nav_button_pin].mode = INPUT
arduinoBoard.digital[select_button_pin].mode = INPUT

# enable reporting for the buttons
arduinoBoard.digital[nav_button_pin].enable_reporting()
arduinoBoard.digital[select_button_pin].enable_reporting()


def isItWin():

    # rows
    for i in range(0, 9, 3):
        if lightSelected[i] == lightSelected[i + 1] == lightSelected[i + 2] != 0:
            return True
    # columns
    for i in range(0, 3):
        if lightSelected[i] == lightSelected[i + 3] == lightSelected[i + 6] != 0:
            return True
    # diagonals
    if lightSelected[0] == lightSelected[4] == lightSelected[8] != 0:
        return True
    if lightSelected[2] == lightSelected[4] == lightSelected[6] != 0:
        return True

    return False


print('Welcome to the game')

while True:
    # read the buttons' states
    navButtonState = arduinoBoard.digital[nav_button_pin].read()
    selectButtonState = arduinoBoard.digital[select_button_pin].read()

    if navButtonState and lastNavButtonState != navButtonState:
        print('nav button pressed')

        navigationButtonPosition = (navigationButtonPosition % 9) + 1
        while lightSelected[navigationButtonPosition - 1] != 0:
            navigationButtonPosition = (navigationButtonPosition % 9) + 1

        if currentPlayer == 1:
            arduinoBoard.digital[light_pins[navigationButtonPosition - 1]
                                 ].write(1)
            lightStates[navigationButtonPosition - 1] = 1
        else:
            arduinoBoard.digital[light_pins[navigationButtonPosition - 1]
                                 ].write(0)
            lightCanBlink[navigationButtonPosition - 1] = True

        for i in range(0, 9):
            if i != navigationButtonPosition - 1 and lightSelected[i] == 0:
                arduinoBoard.digital[light_pins[i]].write(0)
                lightStates[i] = 0
                lightCanBlink[i] = False

    if selectButtonState and lastSelectButtonState != selectButtonState:

        if navigationButtonPosition == 0:
            print('Please select a position using the navigation button')

        elif lightSelected[navigationButtonPosition - 1] != 0:
            print('This position is already selected')
        else:
            if currentPlayer == 1:
                lightSelected[navigationButtonPosition - 1] = 1
                arduinoBoard.digital[light_pins[navigationButtonPosition - 1]
                                     ].write(1)
                lightStates[navigationButtonPosition - 1] = 1
            else:
                lightSelected[navigationButtonPosition - 1] = 2
                arduinoBoard.digital[light_pins[navigationButtonPosition - 1]
                                     ].write(1)
                lightCanBlink[navigationButtonPosition - 1] = True

            navigationButtonPosition = 0

            if isItWin():
                print('Player ' + str(currentPlayer) + ' wins')
                points[currentPlayer - 1] += 1
                print('Player 1: ' + str(points[0]) +
                      ' - Player 2: ' + str(points[1]))
                for i in range(0, 9):
                    lightSelected[i] = 0
                    lightCanBlink[i] = False
                    arduinoBoard.digital[light_pins[i]].write(0)
                    lightStates[i] = 0

                remainingChance -= 1
                print('Remaining Chance: ' + str(remainingChance))

                if remainingChance == 0:
                    print('Game Over')
                    print('Player 1: ' + str(points[0]) +
                          ' - Player 2: ' + str(points[1]))
                    if points[0] > points[1]:
                        print('Player 1 wins')
                    elif points[0] < points[1]:
                        print('Player 2 wins')
                    else:
                        print('Draw')

                    for i in range(0, 9):
                        lightSelected[i] = 0
                        lightCanBlink[i] = False
                        arduinoBoard.digital[light_pins[i]].write(0)
                        lightStates[i] = 0
                    remainingChance = chances
                    currentPlayer = 1
                    points = [0, 0]

            if currentPlayer == 1:
                currentPlayer = 2
            else:
                currentPlayer = 1

    lastNavButtonState = navButtonState
    lastSelectButtonState = selectButtonState

    nowTime = time.time()

    for i in range(0, 9):
        if nowTime - lightsLastBlinkedTime[i] >= 0.5 and lightCanBlink[i]:
            if lightStates[i] == 0:
                arduinoBoard.digital[light_pins[i]].write(1)
                lightStates[i] = 1
            else:
                arduinoBoard.digital[light_pins[i]].write(0)
                lightStates[i] = 0

            lightsLastBlinkedTime[i] = nowTime
