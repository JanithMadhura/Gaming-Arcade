from pyfirmata import Arduino, util, INPUT, OUTPUT
from PyDictionary import PyDictionary
import time
import random
import turtle

d=PyDictionary()


pen1 = turtle.Turtle()

pen2 = turtle.Turtle()                      #Pen create for the turtle screen
pen2.pensize(5)

pen3 = turtle.Turtle()

paper=turtle.Screen()
paper.bgcolor('light blue')
paper.setup(width=1000, height=800)

t = turtle.Turtle()


# Morse code dictionary
MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}

word_list1=['ACE', 'BOB', 'COW', 'DOT', 'EGG', 'FOX', 'GYM', 'HOP', 'INK', 'JAM', 'KID', 'LAP', 'MIX', 'NAP', 'ODD', 'PUG', 'QUA', 'RAG', 'SIP', 'TUG', 'UMP', 'VET', 'WOW', 'YAK', 'ZAP']
word_list2=['ACID', 'BOLD', 'CUTE', 'DOOM', 'ECHO', 'FROG', 'GIFT', 'HAIL', 'ICON', 'JUMP', 'KITE', 'LUCK', 'MOON', 'NOON', 'OVAL', 'PINK', 'QUIT', 'RUBY', 'SOON', 'TALL', 'UNDO', 'VINE', 'WISE', 'YAWN', 'ZOOM']
word_list3=['INDIA','FLUTE', 'CRISP', 'WAGON', 'SABLE', 'PLAID','KARMA', 'FLAIR', 'SHRUB', 'TONIC', 'LEDGE']


        
# Initialize Arduino board and pins
board = Arduino("COM4")
ldr_pin = 0
led_pin_1=12
led_pin_2=11
led_pin_3=9
board .digital[led_pin_1 ].mode = OUTPUT
board .digital[led_pin_2 ].mode = OUTPUT
board .digital[led_pin_3 ].mode = OUTPUT
board.analog[ldr_pin].mode = INPUT
it = util.Iterator(board)
it.start()
board.analog[ldr_pin].enable_reporting()
time.sleep(0.1)

button_pressed = False
duration = 0
pen2.penup()

print("try to guess the word less than 3 attempts")

def all_letters_guessed(gen_word, guess_letter):
    for k in gen_word:
        if k not in guess_letter:
            return False
    return True


# Read Morse code and print corresponding word
def morse_to_letter(morse):
    return MORSE_CODE.get(morse, '')

def HANGMAN_title():
    pen1.pensize(5)
    pen1.penup()
    pen1.goto(-100,250)
    pen1.pendown()                                          # HANGMAN title of the GUI
    pen1.pencolor('gold')
    pen1.write("HANGMAN", font=("Arial", 26,"underline"))
    pen1.penup()
    pen1.setposition(0, 0)
    pen1.pendown()

stage_1_drawn = False
stage_2_drawn = False
stage_3_drawn = False


def stage_1():
    global stage_1_drawn
    if not stage_1_drawn:
        pen2.goto(100,0)
        pen2.pendown()                   #creating the head and the bar of the man
        pen2.forward(100)
        pen2.backward(50)
        pen2.right(90)
        pen2.forward(30)
        pen2.circle(20)
        pen2.penup()
        stage_1_drawn = True


def stage_2():
    global stage_2_drawn
    if not stage_2_drawn:    
        pen2.pendown()
        pen2.forward(20)
        pen2.right(30)
        pen2.fd(30)                     # creating the hands of the man
        pen2.bk(30)
        pen2.left(60)
        pen2.fd(30)
        pen2.bk(30)
        pen2.right(30)
        pen2.penup()
        stage_2_drawn = True
        
def stage_3():
    global stage_3_drawn
    if not stage_3_drawn: 
        pen2.pendown()
        pen2.fd(40)
        pen2.right(30)
        pen2.fd(50)
        pen2.bk(50)                     #creating the legs of the man
        pen2.left(60)
        pen2.fd(50)
        pen2.bk(50)
        pen2.penup()
        stage_3_drawn = True


    
def get_morse_code():
    HANGMAN_title()
    difficulty = input("Enter difficulty (easy/medium/hard): ")
    print()
    if difficulty == "easy":
        gen_word= random.choice(word_list1)
        print("You selected easy difficulty.")
    elif difficulty == "medium":
        gen_word= random.choice(word_list2)
        print("You selected medium difficulty.")
    elif difficulty == "hard":
        gen_word= random.choice(word_list3)                                 #Difficulty level choises as the player wish
        print("You selected hard difficulty.")
    else:
        print("Invalid input. Please enter 'easy', 'medium', or 'hard'.")
        get_morse_code()

    print()    
    mean = d.meaning(gen_word)        
    meaning_str = str(mean).replace(';'and',', '\n')                #write in a new line to awoid meaning sentence go beyond the turtle screen limits
    print(meaning_str)
    print()
    
    attempts=3
    guess_letter=[]
    have_list=[]
    letter_positions = []
    
    print('the word is :', len(gen_word)*(" _ "))
    print()
    print('guess the word')
    print()
    print('Hint: Number of letters :', len(gen_word))
    print()
    
    pen1.penup()
    pen1.goto(-400,220)
    pen1.pendown()
    pen1.pencolor('red')
    pen1.write('guess the word', font=("Arial", 18, "bold italic"))                         # First impresion of the GUI
    pen1.goto(-400,200)
    pen1.penup()
    pen1.goto(0,-20)
    pen1.pendown()
    pen1.pencolor('white')
    pen1.write('Hint: Number of letters %d: Meaning of the word  :%s' %(len(gen_word), meaning_str), align='center', font=("Arial", 13,"bold italic"))
    
    morse_code = ''
    duration = 0
    print('enter the morse code :')
    
    board .digital[led_pin_1 ].write(1)
    board .digital[led_pin_2 ].write(1)
    board .digital[led_pin_3 ].write(1)
    guessed_turtle = turtle.Turtle()
    guessed_turtle.hideturtle()

    pen3.penup()
    pen3.goto(-300,-300)
    pen3.pendown()
    pen3.pencolor('red')
    pen3.write("You have %d attempts left" %attempts, font=("Arial", 16, "bold italic"))
   
    
    while True:
        s = board.analog[ldr_pin].read()        #LDR value takes as s
        
       
        if s <0.7:                          #when s value is lower than 0.7 it consider as input to the system 
            duration+=1
            if duration == 3:                     #when duration is high take the '.' input and convert it to the '-' input
                if morse_code.endswith('..'):
                    morse_code = morse_code[:-2]        # remove the last two dots before adding the dash
                x='-'
                morse_code += x
                time.sleep(1)
            elif duration <3:
                y='.'
                morse_code += y
                time.sleep(1)
            else:
                duration=0
                continue
                
            print('enter the morse code :',morse_code)
            continue
            
        else:
            duration+=1
            time.sleep(1)
            if duration >= 6:           # if silence is longer than 6 seconds
                if len(morse_code) > 0:             # check if morse_code is not empty
                    if morse_code in MORSE_CODE:            # checking if the morse code is exists
                        letter = morse_to_letter(morse_code)
                        print('The letter according to the morse code is :',letter)
                        guess_letter.append(letter)
                        for i in gen_word:
                            if i in guess_letter:
                                print(i, end=" ")
                                for i in range(len(gen_word)):
                                    x = -200 + i * 50
                                    y = -100
                                    letter_positions.append((x, y))
                                for i, k in enumerate(gen_word):
                                    if k in guess_letter:
                                        t.penup()
                                        t.goto(letter_positions[i])
                                        t.write("_", font=("Arial", 24, "normal"))
                                        t.write(k, font=('Centurion Old',25,'bold'))
                                    else:
                                        t.penup()
                                        t.goto(letter_positions[i])
                                        t.write("_", font=("Arial", 24, "normal"))
                            else:
                                print("_", end=" ")
                                
                        if letter not in gen_word:
                            attempts-=1
                            
                            print()
                            print('Sorry,the letter is not in the word')
                        else:
                            
                            print()
                            print('Very good,the letter is in the word')
                              
                        if letter in have_list:
                            if letter in gen_word:
                                
                                print()
                                print("Entered value already tested")           #If it is already tested attempts will not be reduce
                                
                            else:
                                
                                print()
                                print("Entered value already tested")
                                attempts+=1
                            
                        else:
                            have_list.append(letter)
                            
                        print()       
                        print("You have",attempts,"attempts left")
                        pen3.penup()
                        pen3.goto(-300,-300)
                        pen3.pendown()
                        pen3.pencolor('red')
                        pen3.write("You have %d attempts left" %attempts, font=("Arial", 16, "bold italic"))
                        if attempts==3:
                            pen3.clear()
                            pen3.penup()
                            pen3.goto(-300,-300)
                            pen3.pendown()
                            pen3.pencolor('red')                                                                            # Turtle design acording to the attempts left
                            pen3.write("You have %d attempts left" %attempts, font=("Arial", 16, "bold italic"))
                        if attempts==2:
                            pen3.clear()
                            pen3.penup()
                            pen3.goto(-300,-300)
                            pen3.pendown()
                            pen3.pencolor('red')
                            pen3.write("You have %d attempts left" %attempts, font=("Arial", 16, "bold italic"))
                            board .digital[led_pin_1 ].write(0)
                            if not stage_1_drawn:
                                stage_1()
                        if attempts==1:
                            pen3.clear()
                            pen3.penup()
                            pen3.goto(-300,-300)
                            pen3.pendown()
                            pen3.pencolor('red')
                            pen3.write("You have %d attempts left" %attempts, font=("Arial", 16, "bold italic"))
                            board .digital[led_pin_2 ].write(0)
                            if not stage_2_drawn:
                                stage_2()
                        if attempts==0:
                            board .digital[led_pin_3 ].write(0)
                            if not stage_3_drawn:
                                stage_3()
                            print()
                            print("Game over!!.The correct word is :",gen_word)
                            pen1.penup()
                            pen1.goto(-300,-200)
                            pen1.pendown()
                            pen1.pencolor('purple')
                            pen1.write("Game over!!.The correct word is :%s" %gen_word, font=("Arial", 26, "bold italic"))
                            break
                        morse_code = ''

                        if all_letters_guessed(gen_word, guess_letter):
                            print("Congajulations, you guess the word")
                            pen1.penup()
                            pen1.goto(-300,-200)
                            pen1.pendown()
                            pen1.pencolor('green')
                            pen1.write("Congajulations, you guess the word", font=("Arial", 20, "bold italic"))
                            break
                    else:
                        print("Invalid Morse code")             #If entered morse code not in the MORSE_CODE list then it will consider as Invalid input        
                        morse_code = ''                      # reset morse_code variable
                        continue
            else:
                continue
                                
                        
                   
                         

 
    
get_morse_code()

