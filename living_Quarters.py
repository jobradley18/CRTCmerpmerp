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

def crab():
    #Making Crab
    print(" /\\   @ @")
    print("( /   | |    ()")
    print(" \\  __| |__  / ")
    print('  -/   "   \\-')
    print(" /-|       |-\\")
    print("/ /-\     /-\ \\")
    print(" / /-`---'-\ \\")
    print("  /         \\")
#default for the health of the crab
crabhealth = ["#", "#", "#",]
def health():
    #Displays the health of the crab
        print(" / /-`---'-\ \\")
    print("")
    print("")
    print("Crab health: " + str(crabhealth))

p1health = ["#", "#", "#",]
def phealth():
    #Displays the health of the crab
    print("")
    print("")
    print("Player health: " + str(p1health))

health()
crab()
phealth()

import tkinter as tk

root = tk.Tk()



def attack():
    input("You jab your DAGGER at the crab, hitting it directly")
    crabhealth.remove(crabhealth[-1])
    if len(crabhealth) == 0:
        end()  
    else:
        health()
        crab()
def end():
    input("Your swift abilities have caused the crab to faint, well done")
    root.destroy()



def talk():
    input("The crab does not seem to understand you and clacks its claws viciously")
    health()
    crab()
def run():
    input("You try to run away but the crab prevents you with some form of hypnotics")
    health()
    crab()
    
button = tk.Button(root, text='Attack', width=25, command=lambda: attack())
button2 = tk.Button(root, text='Talk', width=25, command=lambda: talk())
button3 = tk.Button(root, text='Run', width=25, command=lambda: run())
#Note that without the lambda: in the command line it will do nothing


#Don't forget to pack!
button.pack()
button2.pack()
button3.pack()
#Run the system
root.mainloop()








if x == (str("go to elevator")):
    print("You are now in the elevator..."
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
    
