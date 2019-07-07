import os
os.chdir("/Users/koc/Desktop/abc")
from cImage import *

#converts text to binary array of length 8
def binText(text): 
        newText = []  
          
        for i in text: 
            newText.append(format(ord(i), '08b')) 
        return newText 

#converts decimal to binary array of length 8
def decToBinary(n):
	result = []
	for i in range(7, -1, -1):  
		k = n >> i; 
		if (k & 1): 
			result.append(1)
		else:
			result.append(0)
	return result

#converts char to binary array of length 16
def charToBinary(c):
	n = ord(c)
	result = []
	for i in range(15, -1, -1):  
		k = n >> i; 
		if (k & 1): 
			result.append(1)
		else:
			result.append(0)
	return result

#converts string to binary array
def strToBinary(txt):
	result = []
	for i in range(len(txt)):
		result.extend(charToBinary(txt[i]))

	return result

#converts binary array to string

def binToString(bin):
	result = ""
	strBin = bin
	while strBin:
		result = result + binToChar(strBin[:16])
		strBin = strBin[16:]

	return result

#prints array
def arrayPrint(arr):
	for i in range(len(arr)):
		print(arr[i],end='')

#binary array of 8 to decimal
def binToDec(arr):
	a = 7
	result = 0;
	for i in range(len(arr)):
		result = (2**a) * arr[i] + result
		a = a - 1
	return result

#binary array of 16 to char
def binToChar(arr):
	a = 15
	result = 0;
	for i in range(len(arr)):
		result = (2**a) * arr[i] + result
		a = a - 1
	return chr(result)

# embeds y binary array lenght of k yto binary array x
def Embed(x,y,k):
	a = 0;
	for i in range(8-k, len(x)):
		if a < len(y):
			x[i] = y[a]
			a = a + 1

	return x


# extracts the last k elements of binary array x
def Extract(x,k):
	return x[-k:]


def embedText(img,k,j,text):
	n = img.getWidth()
	m = img.getHeight()
	retImg = EmptyImage(n,m)
	cur_index = 0;
	binText = strToBinary(text + "#")
	for i in range(n):
		for z in range(m): 
			if z == j and binText: 
				p1 = img.getPixel(i,z)
				r1 = p1.getRed()
				g1 = p1.getGreen()
				b1 = p1.getBlue()
				#print(r1, g1, b1)
				
				y = binText[:k]
				nr = binToDec(Embed(decToBinary(r1),y,k))
				binText = binText[k:] 

				if binText: 
					y = binText[:k] 
					ng = binToDec(Embed(decToBinary(g1),y,k))
					binText = binText[k:]
				else:
					ng = g1

				if binText: 
					y = binText[:k]
					nb = binToDec(Embed(decToBinary(b1),y,k))
					binText = binText[k:]
				else:
					nb = b1

				#print(nr, ng, nb)
				#print(" ")
				np = Pixel(nr,ng,nb)
				retImg.setPixel(i,z,np)
				cur_index = cur_index + 1
			else:
				p1 = img.getPixel(i,z)
				r1 = p1.getRed()
				g1 = p1.getGreen()
				b1 = p1.getBlue()
				#print(r1, g1, b1)
				#print(" ")
				retImg.setPixel(i,z,p1)
				#cur_index = cur_index + 1
	#print(cur_index)
				
	return(retImg)


def extraText(img, k,j):
	n = img.getWidth() 
	text = "" 
	textBin = []
	binChar = [] 
	cur = 0;
	for i in range(n):
		p1 = img.getPixel(i,j)
		r1 = p1.getRed()
		g1 = p1.getGreen()
		b1 = p1.getBlue()
		nr = Extract(decToBinary(r1),k)
		ng = Extract(decToBinary(g1),k)
		nb = Extract(decToBinary(b1),k)
		
		if cur == 16:
			c = binToChar(binChar)
			if c == "#":
				break
			text = text + c
			cur = 0
			binChar = []
			binChar.extend(nr)
			cur = cur + k
		else:
			binChar.extend(nr)
			cur = cur + k

		if cur == 16:
			c = binToChar(binChar)
			if c == "#":
				break
			text = text + c
			cur = 0
			binChar = []
			binChar.extend(ng)
			cur = cur + k
		else:
			binChar.extend(ng)
			cur = cur + k

		if cur == 16:
			c = binToChar(binChar)
			if c == "#":
				break
			text = text + c
			cur = 0
			binChar = []
			binChar.extend(nb)
			cur = cur + k
		else:
			binChar.extend(nb)
			cur = cur + k
	return text


# ----------------------
txt = "Fotoğrafçı Çetin Kaya Koç 21 Aralık 2018"

img = FileImage("leo.gif")

im2 = embedText(img, 1, 0, txt)
tx2 = extraText(im2, 1, 0)
print(tx2)
