########################################################

def check_Inventory():
    print (inventory)



########################################################

while True:
    input("You are decending in an old elevator. Slowly, it creaks to a stop and the doors open.")
    input("You are greeted with the rancid smell of teen's sweat.")
    input("An errie white lights line the ceiling, a few flicker as you look on")
    input("There are two rows of beds on either side of the room.")
    input("Eight beds in total each with pristine white sheets")
    input("There is a pillow at the head of each bed and a chest at the foot.")
    input("Everything is still, too still...")
    
########################################################

    import tkinter as tk

    root_Inventory = tk.Tk()

    button = tk.Button(root_Inventory, text='Inventory', width=25, command=lambda: check_Inventory())
    button.pack()
    root_Inventory.mainloop()
    inventory = [] 
    input("The bed...")
    input("Its pressence calls out to you.")
    input("You notice that something silver underneath the pillow.")
    
    while True:
        investigate = input("Do you want to investigate the pillow?:")
        if investigate.lower() == "yes":       
            input("You found a KEY")
            inventory.append("KEY")
            break
        

    


########################################################

        trunk = ["NOTEBOOK", "PEN","DAGGER"]
        if "KEY" in inventory: 
            input("With the key in hand you approach the large wooden trunk.")
            input("You insert the key hopefully into the old lock on the front.")
            input("In the trunk you find a collection of NOTEBOOKS, PENS, and a SMALL DAGGER.")
            inventory.extend(trunk) 
        else:
            input("You approach a trunk at the foot of one of the beds.")
            input("This trunk requires a KEY")
            continue
            
########################################################

    break
    
    
    
    
# -*- coding: utf-8 -*-
#beginning of encounter






print("You encounter a giant fluffy crab")
print("It seems angry for some reason")
print("How will you defend yourself?")
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
    print("You swing your sword at the crab, hitting it derectly")
    crabhealth.remove(crabhealth[-1])
    if len(crabhealth) == 0:
        end()  
    else:
        health()
        crab()
def end():
    print("Your swift abilities have caused the crab to faint, well done")
    root.destroy()



def talk():
    print("The crab does not seem to understand you and clacks its claws viciously")
    health()
    crab()
def run():
    print("You try to run away but the crab prevents you with some form of hypnotics")
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
