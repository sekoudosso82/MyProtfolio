# a strange object moves in the graphics window

from cs1graphics import *
import time

def main():
    
    # instantiaing a canvas (graphics window)
    paper = Canvas(600,600,(200,255,200),"Image")

    time.sleep(1) # waiting

    #paper.setBackgroundColor((245,226,245))

    i = Image("tree.png")
    i.moveTo(200,200)
    paper.add(i)
       
    time.sleep(4)
    paper.close() # don't forget to close the canvas
         

main()    
