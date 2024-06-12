from pyfirmata import Arduino,OUTPUT ,OUTPUT ,util,INPUT

import time,random

board = Arduino("COM4")

led_pins = [13, 12, 11, 10 , 9, 8, 7, 6, 5]  # LED pins
button_pins = [0, 1, 2]  # Button pins
buzzer_pin = 4  # Buzzer pin


it = util.Iterator(board )
it.start ()
leds = [board.get_pin('d:' + str(pin) + ':o') for pin in led_pins]
buttons = [board.get_pin('a:' + str(pin) + ':i') for pin in button_pins]
buzzer = board.get_pin('d:' + str(buzzer_pin) + ':o')




row = 0
column = 0
n=0
T = True
j=0

def defeat():
    global j,T
    print("Defeat")
    for k in range(5):
        buzzer.write(1)
        time.sleep(0.3)
        buzzer.write(0)
        time.sleep(0.2)
    T=False
    j=100
            

def option_1():
    start_time = time.time()
    while ((buttons[0].read()<0.5) or (buttons[0].read()<0.5) or (buttons[0].read()<0.5)):
        print(buttons[0].read())
        print(buttons[1].read())
        print(buttons[2].read())
        buzzer.write(1)
        if(time.time()-start_time>2):
            print(time.time()-start_time>8)
            defeat()
            break
        if(j==6):
            if((buttons[0].read()>0.5)):
                buzzer.write(0)
                print("Won6")
                break
            elif((buttons[1].read()>0.5) or (buttons[2].read()>0.5)):
                defeat()
                break

        elif(j==7):
            if((buttons[1].read()>0.5)):
                buzzer.write(0)
                print("Won7")
                break
            elif((buttons[0].read()>0.5) or (buttons[2].read()>0.5)):
                defeat()
                break
        elif(j==8):
            if((buttons[2].read()>0.5)):
                buzzer.write(0)
                print("Won8")
                break
            elif((buttons[0].read()>0.5) or (buttons[1].read()>0.5)):
                defeat()
                break

def option_2():
    start_time = time.time()
    while ((buttons[0].read()<0.5) or (buttons[0].read()<0.5) or (buttons[0].read()<0.5)):
        print(buttons[0].read())
        print(buttons[1].read())
        print(buttons[2].read())
        buzzer.write(1)
        if(time.time()-start_time>2):
            print(time.time()-start_time>8)
            defeat()
            break
        if((n-(column1 - column2))==6):
            buzzer.write(0)
            if((buttons[0].read()>0.5)):
                print("Won6")
                break
            elif((buttons[1].read()>0.5) or (buttons[2].read()>0.5)):
                defeat()
                break
        elif((n-(column1 - column2))==7):
            if((buttons[1].read()>0.5)):
                buzzer.write(0)
                print("Won7")
                break
            elif((buttons[0].read()>0.5) or (buttons[2].read()>0.5)):
                defeat()
                break
        elif((n-(column1 - column2))==8):
            if((buttons[2].read()>0.5)):
                buzzer.write(0)
                print("Won8")
                break
            elif((buttons[0].read()>0.5) or (buttons[1].read()>0.5)):
                defeat()
                break

def option_3():
    start_time = time.time()
    while ((buttons[0].read()<0.5) or (buttons[0].read()<0.5) or (buttons[0].read()<0.5)):
        print(buttons[0].read())
        print(buttons[1].read())
        print(buttons[2].read())
        buzzer.write(1)
        if(time.time()-start_time>2):
            print(time.time()-start_time>8)
            defeat()
            break
        if((n+(column2 - column1))==6):
            if((buttons[0].read()>0.5)):
                buzzer.write(0)
                print("Won6")
                break
            elif((buttons[1].read()>0.5) or (buttons[2].read()>0.5)):
                defeat()
                break

        elif((n+(column2 - column1))==7):
            if((buttons[1].read()>0.5)):
                buzzer.write(0)
                print("Won7")
                break
            elif((buttons[0].read()>0.5) or (buttons[2].read()>0.5)):
                defeat()
                break
        elif((n+(column2 - column1))==8):
            if((buttons[2].read()>0.5)):
                buzzer.write(0)
                print("Won8")
                break
            elif((buttons[0].read()>0.5) or (buttons[1].read()>0.5)):
                defeat()
                break
    

while T:
    k=1

    column1 = random.randint(0,2)
    column2 = random.randint(0,2)
    if (column1 == column2):
        column1 = 0
        column2 = 2

        

    for j in range(column1,column1+10,3):
            if k==1:
                leds[j].write(1)
                time.sleep(0.7)
                leds[j].write(0)


            else:
                if column1<column2:
                    if column1+7 > j:
                        leds[j].write(1)
                    leds[n-(column1 - column2)].write(1)
                    time.sleep(0.7)
                    if column1+7 > j:
                        leds[j].write(0)
                    leds[n-(column1 - column2)].write(0)

                    if(j==6 or j==7 or j==8):
                        option_1()
                               

                    if((n-(column1 - column2))==6 or (n-(column1 - column2))==7 or (n-(column1 - column2))==8):
                        option_2()
                            

                    
                else:
                    if column1+7 > j:
                        leds[j].write(1)
                    leds[n+(column2 - column1)].write(1)
                    time.sleep(0.7)
                    if column1+7 > j:
                        leds[j].write(0)
                    leds[n+(column2 - column1)].write(0)

                    if(j==6 or j==7 or j==8):
                        option_1()
                            

                    if((n+(column2 - column1))==6 or (n+(column2 - column1))==7 or (n+(column2 - column1))==8):
                        option_3()

            
            k=0
            n=j

        


