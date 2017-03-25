from Tkinter import *

import sfml as sf 
from sfml import sf

#Load Music Here
#Scene 1

sc10=sf.Music.from_file("/home/asus/PlaySequencer/a.wav")
sc11=sf.Music.from_file("/home/asus/PlaySequencer/a.wav")
sc12=sf.Music.from_file("/home/asus/PlaySequencer/a.wav")
sc13=sf.Music.from_file("/home/asus/PlaySequencer/a.wav")
sc14=sf.Music.from_file("/home/asus/PlaySequencer/a.wav")
sc15=sf.Music.from_file("/home/asus/PlaySequencer/a.wav")
sc16=sf.Music.from_file("/home/asus/PlaySequencer/a.wav")
sc1=[sc10,sc11,sc12,sc13,sc14,sc15,sc16]

def playmusic(sc,snd):
	if sc == 1:
		sc1[snd].play()


root = Tk(className="Drama Sequencer") # creates root window
# all components of thw window will come here
Label(root, text="Scene 1").grid(row=0, sticky=W)
Button(root,text="Background Sound 1",command=lambda: playmusic(1,0)).grid(columnspan=2,row=0,column=1) 
Button(root,text="Sound 1").grid(row=1,column=0) 
Button(root,text="Sound 2").grid(row=1,column=1) 
Button(root,text="Sound 3").grid(row=1,column=2) 
Button(root,text="Sound 4").grid(row=1,column=3) 
Button(root,text="Sound 5").grid(row=1,column=4) 
Button(root,text="Sound 6").grid(row=1,column=5)
 
Label(root, text="-----------").grid(columnspan=6,row=2, sticky=N)

Label(root, text="Scene 2").grid(row=3, sticky=W)
Button(root,text="Background Sound 1").grid(columnspan=2,row=3,column=1) 
Button(root,text="Sound 1").grid(row=4,column=0) 
Button(root,text="Sound 2").grid(row=4,column=1) 
Button(root,text="Sound 3").grid(row=4,column=2) 
Button(root,text="Sound 4").grid(row=4,column=3) 
Button(root,text="Sound 5").grid(row=4,column=4) 
Button(root,text="Sound 6").grid(row=4,column=5) 

Label(root, text="-----------").grid(columnspan=6,row=5, sticky=N)

Label(root, text="Scene 2").grid(row=6, sticky=W)
Button(root,text="Background Sound 1").grid(columnspan=2,row=6,column=1) 
Button(root,text="Sound 1").grid(row=7,column=0) 
Button(root,text="Sound 2").grid(row=7,column=1) 
Button(root,text="Sound 3").grid(row=7,column=2) 
Button(root,text="Sound 4").grid(row=7,column=3) 
Button(root,text="Sound 5").grid(row=7,column=4) 
Button(root,text="Sound 6").grid(row=7,column=5) 

Label(root, text="-----------").grid(columnspan=6,row=8, sticky=N)

Label(root, text="Scene 2").grid(row=9, sticky=W)
Button(root,text="Background Sound 1").grid(columnspan=2,row=9,column=1) 
Button(root,text="Sound 1").grid(row=10,column=0) 
Button(root,text="Sound 2").grid(row=10,column=1) 
Button(root,text="Sound 3").grid(row=10,column=2) 
Button(root,text="Sound 4").grid(row=10,column=3) 
Button(root,text="Sound 5").grid(row=10,column=4) 
Button(root,text="Sound 6").grid(row=10,column=5) 

Label(root, text="-----------").grid(columnspan=6,row=11, sticky=N)

Label(root, text="Scene 2").grid(row=12, sticky=W)
Button(root,text="Background Sound 1").grid(columnspan=2,row=12,column=1) 
Button(root,text="Sound 1").grid(row=13,column=0) 
Button(root,text="Sound 2").grid(row=13,column=1) 
Button(root,text="Sound 3").grid(row=13,column=2) 
Button(root,text="Sound 4").grid(row=13,column=3) 
Button(root,text="Sound 5").grid(row=13,column=4) 
Button(root,text="Sound 6").grid(row=13,column=5) 

Label(root, text="-----------").grid(columnspan=6,row=14, sticky=N)

Label(root, text="Scene 2").grid(row=15, sticky=W)
Button(root,text="Background Sound 1").grid(columnspan=2,row=15,column=1) 
Button(root,text="Sound 1").grid(row=16,column=0) 
Button(root,text="Sound 2").grid(row=16,column=1) 
Button(root,text="Sound 3").grid(row=16,column=2) 
Button(root,text="Sound 4").grid(row=16,column=3) 
Button(root,text="Sound 5").grid(row=16,column=4) 
Button(root,text="Sound 6").grid(row=16,column=5) 







root.mainloop() # To keep GUI window running
