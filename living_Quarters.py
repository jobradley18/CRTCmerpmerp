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

    inventory = [] 
    input("The bed...")
    input("Its pressence calls out to you.")
    input("You notice that something silver underneath the pillow.")
    while True:
        investigate = input("Do you want to investigate?:")
        if investigate.lower() == "yes":       
            input("You found a KEY")
            inventory.append("KEY")
            break
        elif investigate.lower() == "no":
            break

########################################################

    trunk = ["NOTEBOOK", "PEN","DAGGER"]
    if "KEY" in inventory: 
        input("Wth the key in hand you approach the large wooden trunk.")
        input("You insert the key hopefully into the old lock on the front.")
        input("In the trunk you find a collection of NOTEBOOKS, PENS, a  SMALL DAGGER,")
        inventory.extend(trunk) 
    else:
        input("This trunk requires a KEY")
   
########################################################

    break
    
