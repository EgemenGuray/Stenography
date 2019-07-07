import os
os.chdir("/Users/egemen/Desktop/abc")
from cImage import *

n = 8
m = 8
im = EmptyImage(n,m)
p0 = Pixel(255,255,255) # white
p1 = Pixel(255,0,0) # red
p2 = Pixel(0,255,0) # green
p3 = Pixel(0,0,255) # blue
p4 = Pixel(127,0,255) # purple
p5 = Pixel(255,255,0) # yellow
p6 = Pixel(0,255,255) # cyan
p7 = Pixel(255,0,255) # magenta


for i in range(n):
    im.setPixel(i,0,p7)
for i in range(n):
    im.setPixel(i,1,p7)
for i in range(n):
    im.setPixel(i,2,p6)
for i in range(n):
    im.setPixel(i,3,p6)
for i in range(n):
    im.setPixel(i,4,p5)
for i in range(n):
    im.setPixel(i,5,p5)
for i in range(n):
    im.setPixel(i,6,p4)
for i in range(n):
    im.setPixel(i,7,p4)

mywin = ImageWin("Show",n,m)
im.draw(mywin)
im.save("new.gif")





        
        



            
