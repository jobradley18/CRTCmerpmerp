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

#########################################################
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
        label01.config(text="The claws clacked so viciously that it hurt your ears, you lose one health")
        if len(p1health) == 0:
            death()
    elif y == 3 and len(p1health) != 0:
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









if x == (str("go to elevator")):
    print("You are now in the elevator...")
    exitToFirstFloor()

def exitToFirstFloor():
    print("You are now in the elevator..."
    x = raw_input("---What would you like to do?  ")
    in_elevator = True
    i = 0
    z = 0
    while True:
        y = raw_input("---What would you like to do?  ")
        if y == ("press up") and in_elevator and i == 0:
            print ("")
            print ("The elevator doors close with a thud")
            print ("it slowly climbs its way back to the first floor")
            print ("however the doors stay closed.")
            i = i + 1
        elif y == ("press down") and i == 1:
            print ("The elevator is stuck, what would you like to do?")
        elif y == ("freak out") and z == 0:
            print ("You scream until you pass out...")
            print ("When you wake up you feel a lot better")
            print ("like you could take on the world, by yourself")
            print ("then you remeber... your on Mars.")
            z = 1
        elif y == ("freak out") and z == 1:
            print ("Please stop freaking out")
            print ("its becoming very, very, very annoying.")
            z = 2
        elif y == ("use elevator"):
            print ("")
            print ("What specifically would you like to do?")
        elif y == ("exit elevator")and i == 0:
            print ("")
            print ("You have exited the elevator and are now looking")
            print ("back at the room with errie white lights")
            print ("lining the ceiling, a few flicker as you look on")
            print ("There are two rows of beds on either side of the room.")
            print ("Eight beds in total each with pristine white sheets")
            print ("There is a pillow at the head of each bed and a chest at the foot.")
            break
            in_elevator = False
        elif y == ("press up")and i == 1:
            print ("")
            print ("The doors slowly open revealing that")
            print ("the elevator is stuck, the first floor is")
            print ("only visible through the top half of the elevator.")
            i = i + 1
        elif y == ("exit elevator")and i == 2:
            print ("")
            print ("You have now exited the elevator and")
            print ("are on the first floor.")
            in_elevator = False
            break
        else:
            print ("")
            print ("I'm sorry I do not understand...")
    
