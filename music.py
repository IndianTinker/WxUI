from easygui import *
import sys

while 1:
    msg ="Choose the scene and click background to loop music"
    title = "Ice Cream Survey"
    choices = ["Scene 1", "Scene 2", "Scene 3", "Scene 4","Scene 5", "Scene 6"]
    choice = buttonbox(msg, title, choices)
    if choice == 
  	

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)           # user chose Cancel

