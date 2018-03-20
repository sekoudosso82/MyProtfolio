""" Final project"""

from cs1graphics import*
from time import sleep
import random
# first fuction to control the differents moves
def hanoi(n, peg1, peg2, peg3):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, peg1, peg2, peg3)
        # move disk from source peg to target peg
        if peg1:
            peg3.append(peg1.pop())
        # move tower of size n-1 from helper to target
        hanoi(n - 1, peg2, peg1, peg3)
"""        
peg1 = [4,3,2,1]
peg3 = []
peg2 = []
hanoi(len(speg1),peg1,peg2,peg3)

print (peg1, peg2, peg3)
"""


def main():
    n = int(input(" Type the number of disk :"))
    # graphic window"""
    screen = Canvas(600,600,"Orange","Tower of hanoi")
    # draw the three pegs
    #peg 1
    peg1base = Polygon(Point(50,550),Point(150,550))
    peg1base.setBorderWidth(10)
    peg1base.adjustReference(100,550)
    screen.add(peg1base)
    dx1 = 100
    dy11 = 200
    dy12 = 550
    peg1Height = Polygon(Point(dx1,dy11),Point(dx1, dy12))
    peg1Height.setBorderWidth(10)
    peg1Height.adjustReference(100,550)
    screen.add(peg1Height)
    # peg 2
    peg2base = Polygon(Point(250,550),Point(350,550))
    peg2base.setBorderWidth(10)
    peg2base.setBorderColor('green')
    peg2base.adjustReference(300,550)
    screen.add(peg2base)
    dx2 = 300
    dy21 = 200
    dy22 = 550
    peg2Height = Polygon(Point(dx2,dy21),Point(dx2, dy22))
    peg2Height.setBorderWidth(10)
    peg2Height.setBorderColor('green')
    peg2Height.adjustReference(300,550)
    screen.add(peg2Height)
    # peg 3
    peg3base = Polygon(Point(450,550),Point(550,550))
    peg3base.setBorderWidth(10)
    peg3base.setBorderColor('Blue')
    peg3base.adjustReference(500,550)
    screen.add(peg3base)
    dx3 = 500
    dy31 = 200
    dy32 = 550
    peg3Height = Polygon(Point(dx3,dy31),Point(dx3, dy32))
    peg3Height.setBorderWidth(10)
    peg3Height.setBorderColor('Blue')
    peg3Height.adjustReference(500,550)
    screen.add(peg3Height)

    color = ['blue','green','purple','red','white','black','yellow']

    w = 80# width
    h = 20 #height
    dx = 100
    dy = 535
    for i in range (int(n)):
      #Polygon(Point(450,550),Point(550,550))
      disk = Rectangle(w,h, Point(dx,dy))
      disk.setBorderWidth(2)# height of peg
      disk.setFillColor(random.choice(color))
      disk.setBorderColor(random.choice(color))
      #disk.ajustReference(500,550)
      screen.add(disk)
      ratio = 80/(int(n))
      w = w-ratio
      h = h
      dy =dy-(2+h)
      sleep(1)
      for i in range (int(n-1)):
          #Polygon(Point(450,550),Point(550,550))
          disk(n-1).move(400,400)
          sleep(1)
      
   
    # the end"""
main()
    


    
