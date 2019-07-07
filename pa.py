import os
from cImage import *
from time import sleep

os.chdir('./abc')

# gets a string char by char converts it to the 
# 16-tuples of binary array adds to the binary array
# string -> array(0,1)
def textToBinary(text):
	result = ""
	for letter in text:
		char = ord(letter)
		binary = format(char, '016b')
		result = result + binary
	return result

# gets an array of 0s and 1s slices into 16-tuples
# converts to char and adds to the resulting text
# array(0,1) -> string
def binaryToText(binary):
	retText = ""
	for i in range(len(binary) // 16):
		seq = binary[16*i : 16*i+16]
		unicode_pt = int(seq, 2)
		retText = retText + chr(unicode_pt)
	return retText


def embedText(img, k, j, text):

	n = img.getWidth()
	m = img.getHeight()
	binary = textToBinary(text)
	binary = binary.ljust(n*k*3,"0")
	im2 = EmptyImage(n,m)


	for row in range(j):
		for i in range(n):
			im2.setPixel(i,row,img.getPixel(i,row))

	for i in range(n):
		#get k by k for each subpixels
		y = binary[i*k*3 : i*k*3+k]
		r = int(y,2)
		y = binary[i*k*3+k : i*k*3+k*2]
		g = int(y, 2)
		y = binary[i*k*3+k*2 : i*k*3+k*3]
		b = int(y, 2)
		p = Pixel(r,g,b)
		im2.setPixel(i,j,p)

	for row in range(j+1,m,1):
		for i in range(n):
			im2.setPixel(i, row, img.getPixel(i, row))
	return im2

def extraText(img, k, j):
	n = img.getWidth()
	m = img.getHeight()
	result = ""
	for i in range(n):
		p = img.getPixel(i,j)
		y = format(p.getRed(),'0' +str(k) + 'b')
		result = result + y
		y = format(p.getGreen(), '0' + str(k) + 'b')
		result = result + y
		y = format(p.getBlue(), '0' + str(k) + 'b')
		result = result + y

	value = binaryToText(result)
	return value.split('\x00')[0]


#-------------------- Test ------------------------
txt = "PlaceHolder"

img = FileImage("leo.gif")

im2 = embedText(img, 3, 0, txt)
tx2 = extraText(im2, 3, 0)
print(tx2)
