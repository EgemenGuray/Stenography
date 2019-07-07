import os
os.chdir("/Users/egemen/Desktop/abc")
from cImage import *

def MakeZero(im1,mask):
    n = im1.getWidth()
    m = im1.getHeight()
    im2 = EmptyImage(n,m)
    for i in range(n):
        for j in range(m):
            p = im1.getPixel(i,j)
            r = p.getRed()
            g = p.getGreen()
            b = p.getBlue()
            q = Pixel(r & mask,g & mask,b & mask)
            im2.setPixel(i,j,q)
    return(im2)
            

# ----------------------
im1 = FileImage("leo1.gif")
mw1 = ImageWin("Leo",500,500)
im1.draw(mw1)

im2 = MakeZero(im1,0b11111100)
mw2 = ImageWin("Leo",500,500)
im2.draw(mw2)
im2.save("leo2.gif")

im2 = MakeZero(im1,0b11110000)
mw2 = ImageWin("Leo",500,500)
im2.draw(mw2)
im2.save("leo4.gif")

im2 = MakeZero(im1,0b11000000)
mw2 = ImageWin("Leo",500,500)
im2.draw(mw2)
im2.save("leo6.gif")

