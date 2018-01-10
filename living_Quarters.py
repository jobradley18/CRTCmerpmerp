########################################################

def check_Inventory():
    print (inventory)

########################################################

while True:
    input("You are decending in an old elevator. Slowly, it creaks to a stop and the doors open.")
    input("You are greeted with the rancid smell of teen's sweat.")
    input("Errie white lights line the ceiling, a few flicker as you look on")
    input("There are two rows of beds on either side of the room.")
    input("Eight beds in total each with pristine white sheets")
    input("There is a pillow at the head of each bed and a chest at the foot.")
    input("Everything is still, too still...")
    
########################################################

    inventory = [] 
    input("The bed...")
    input("Its pressence calls out to you.")
    input("You notice that something silver underneath the pillow.")
    
    while True:
        investigate = input("Do you want to investigate the pillow?:")
        if investigate.lower() == "yes":       
            input("You found a KEY")
            inventory.append("KEY")
        
########################################################

        trunk = ["NOTEBOOK", "PEN","DAGGER"]
        if "KEY" in inventory: 
            input("With the key in hand you approach the large wooden trunk.")
            input("You insert the key hopefully into the old lock on the front.")
            input("In the trunk you find a collection of NOTEBOOKS, PENS, and a SMALL DAGGER.")
            inventory.extend(trunk) 
            break
        else:
            input("You approach a trunk at the foot of one of the beds.")
            input("This trunk requires a KEY")
            continue
            
########################################################

    break
    
########################################################

# -*- coding: utf-8 -*-
#beginning of encounter

########################################################

input("You turn around to encounter a giant, fluffy crab.")
input("It seems to have been hiding in one of the trunks behind you")
input("It stands menacingly between you and the elevator door.")
input("How will you defend yourself?")

"""
Odds for fight:
Run - 100% chance to lose health
Talk - 25% chance to lose heealth (3 talks = win?(woo the crab?))
Attack - At full health: 50%
         At 2 health: 25%
         At 1 health: 5%
"""

import random
qwerty = False
#default for the health of the crab
crabhealth = ["<3", "<3", "<3"]
p1health = ["<3", "<3", "<3"]
import tkinter as tk
from tkinter import *
root = tk.Tk()
def retry():
    global p1health
    global crabhealth
    p1health = ["<3", "<3", "<3"]
    crabhealth = ["<3", "<3", "<3"]
    label2.config(text="Player Health: " + " ".join(p1health))
    label.config(text="Crab Health: " + " ".join(crabhealth))
    label0.config(text="")
    label01.config(text="")
    button.config(text="Attack", command=lambda: attack())
    button2.config(text="Talk", command=lambda: talk())
    button3.config(text="Run", command=lambda: run())
def death():
    #Change all buttons to restart fight
    label0.config(text="You ran out of life, but don't worry you can always try again!")
    label01.config(text="")
    button.config(text="Rety", command=lambda: retry())
    button2.config(text="Rety", command=lambda: retry())
    button3.config(text="Rety", command=lambda: retry())
def attack():
    label01.config(text="")
    try:
        crabhealth.remove(crabhealth[0])
        label0.config(text="You swing your dagger at the crab, wallopping one of it's eyes")
        if len(crabhealth) == 0:
            root.destroy()
        x = random.randint(1, 20)
        if len(p1health) == 3:
            if x <= 10:
                p1health.remove(p1health[0])
                crabhealth.append("<3")
                label0.config(text="You swing at the crab, but your full health made you overconfident")
                label01.config(text="The crab to pinched you. It hurt a lot...")
        elif len(p1health) == 2:
            if x <= 5:
                p1health.remove(p1health[0])
                crabhealth.append("<3")
                label0.config(text="I'm not sure I can validate that swipe as a valid attempt to attack the crab...")
                label01.config(text="The crab shakes your hand, but it was such firm handshake you take one damage")
        elif len(p1health) == 1:
            if x <= 1:
                p1health.remove(p1health[0])
                crabhealth.append("<3")
                label0.config(text="The crab has made you weak at this point, your last stand was simply you collapsing mid swing")
                label01.config(text="As everything fades to black you see the crab do a celebratory jig")
                death()
        label2.config(text="Player Health: " + " ".join(p1health))
        label.config(text="Crab Health: " + " ".join(crabhealth))
    except:
        #As odd as this seems tkinter is spitting out an error as it thinks
        #It is running after being destroyed but gets confused because
        #It is destroyed. This just negates the error and ends the fight
        pass
y = 0
def talk():
    global y
    label01.config(text="")
    x = random.randint(1, 4)
    y += 1
    label0.config(text="The crab does not seem to understand you and clacks its claws viciously")
    if x == 1:
        p1health.remove(p1health[0])
        label2.config(text="Player Health: " + " ".join(p1health))
        label01.config(text="The claws clacked so viciously that it hurt your ears, you lose one health")
        if len(p1health) == 0:
            death()
    elif y >= 3 and len(p1health) != 0:
        global qwerty
        qwerty = True
        try:
            root.destroy()
        except:
            pass
def run():
    p1health.remove(p1health[0])
    if len(p1health) == 0:
        death()
    else:
        label0.config(text="You try to run away but the crab prevents you with some form of hypnotics")
        label01.config(text="Discouraged from you feable attempt the crab pokes you")
        label2.config(text="Player Health: " + " ".join(p1health))
label0 = tk.Label(root, text=" ")
label0.pack(side=TOP)
label01 = tk.Label(root, text=" ")
label01.pack(side=TOP)
label = tk.Label(root, text="Crab Health: " + " ".join(crabhealth))
label.pack(side=TOP)
T = Text(root, height=8, width=16, foreground=("purple"))
T.pack(side=TOP)
T.insert(INSERT, """ /\\   @ @
( /   | |    ()
 \\  __| |__  /
  -/   "   \\-
 /-|       |-\\
/ /-\     /-\ \\
 / /-`---'-\ \\
  /         \\
""")
label2 = tk.Label(root, text="Player Health: " + " ".join(p1health))
label2.pack(side=TOP)
label3 = tk.Label(root, text=" ")
label3.pack(side=TOP)
button = tk.Button(root, text='Attack', width=25, command=lambda: attack())
button2 = tk.Button(root, text='Talk', width=25, command=lambda: talk())
button3 = tk.Button(root, text='Run', width=25, command=lambda: run())
#Note that without the lambda: in the command line it will do nothing



button.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
#Run the system
root.mainloop()
if qwerty:
    input("Being the smooth talker you are you somehow convinced the crab to leave you be. Well done")
else:
    input("Your swift abilities have caused the crab to faint, well done")








def enterLivingQuarter():
    exit = True
    while exit:
        global speak
        speak = raw_input(str("---What would you like to do? "))
        speak = speak.lower()
        if speak == "down" or speak == "go down":
            print("")
            raw_input("You are decending in an old elevator. Slowly, it creaks to a stop and the doors open.")
            raw_input("You are greeted with the rancid smell of teen's sweat.")
            raw_input("Errie white lights line the ceiling, a few flicker as you look on")
            raw_input("There are two rows of beds on either side of the room.")
            raw_input("Eight beds in total each with pristine white sheets")
            raw_input("There is a pillow at the head of each bed and a chest at the foot.")
            raw_input("Everything is still, too still...")
            exit = False
        elif speak == "go up" or speak == "up":
            print("")
            raw_input("The elevator begins to move up, then stops suddenly.")
            raw_input("For a few seconds there is nothing but silence")
            raw_input("Until the elevator plumits downward moving faster and faster until")
            raw_input("finally it comes to a complete stop, slowly the doors creak open.")
            raw_input("You are greeted with the rancid smell of teen's sweat.")
            raw_input("Errie white lights line the ceiling, a few flicker as you look on")
            raw_input("There are two rows of beds on either side of the room.")
            raw_input("Eight beds in total each with pristine white sheets")
            raw_input("There is a pillow at the head of each bed and a chest at the foot.")
            raw_input("Everything is still, too still...")
            exit = False
        else:
            print("I do not understand.")


def exitToFirstFloor():
    print("You are now in the elevator...")
    in_elevator = True
    progress = 0
    freakOut = 0
    while in_elevator:
        respond = raw_input("---What would you like to do?  ")
        if respond == ("press up") and in_elevator and progress == 0:
            print ("")
            raw_input ("The elevator doors close with a thud")
            raw_input ("it slowly climbs its way back to the first floor")
            raw_input ("however the doors stay closed.")
            progress = progress + 1
        elif respond == ("press down") and progress == 1:
            print ("")
            raw_input ("The elevator is stuck, what would you like to do?")
        elif respond == ("freak out") and freakOut == 0:
            print ("")
            raw_input ("You scream until you pass out...")
            raw_input ("When you wake up you feel a lot better")
            raw_input ("like you could take on the world, by yourself")
            raw_input ("then you remeber... your on Mars.")
            freakOut = 1
        elif respond == ("freak out") and freakOut == 1:
            print ("")
            raw_input ("Please stop freaking out")
            raw_input ("its becoming very, very, very annoying.")
            freakOut = 2
        elif respond == ("use elevator"):
            print ("")
            raw_input ("What specifically would you like to do?")
        elif respond == ("exit elevator")and progress == 0:
            print ("")
            raw_input ("You have exited the elevator and are now looking")
            raw_input ("back at the room with errie white lights")
            raw_input ("lining the ceiling, a few flicker as you look on")
            raw_input ("There are two rows of beds on either side of the room.")
            raw_input ("Eight beds in total each with pristine white sheets")
            raw_input ("There is a pillow at the head of each bed and a chest at the foot.")
            break
            in_elevator = False
        elif respond == ("press up")and progress == 1:
            print ("")
            raw_input ("The doors slowly open revealing that the")
            raw_input ("elevator is stuck, only the bottom of the door is")
            raw_input ("visible through the top half of the elevator.")
            progress = progress + 1
        elif respond == ("exit elevator")and progress == 2:
            print ("")
            raw_input ("You have now exited the elevator and")
            raw_input ("are on the first floor.")
            in_elevator = False
            break
        else:
            print ("")
            raw_input ("I'm sorry I do not understand...")
            
    
print("You open the door to reviel an open elevator.")
print("There are only 2 buttons in the elevevator, one to go up and one to go down.")
