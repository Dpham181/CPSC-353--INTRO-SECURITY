


#  tr 'abcdefghijklmnopqrstuvwxyz' 'cfmypvbrlqxwiejdsgkhnazotu' <ciphertext.txt> plain.txt



import random 
import collections
import string
from string import maketrans



alphabet = "abcdefghijklmnopqrstuvwxyz"

key = "cfmypvbrlqxwiejdsgkhnazotu"

transformer= string.maketrans(alphabet,key)


	
def frequency(text) :
	freq = collections.defaultdict(int)
        for line in text:

	    line = line.rstrip('\n')

	    for char in line:

	    	freq[char] +=1

	return freq

def printplaintext(text):

	plaintext =text.translate(transformer)
	
	return plaintext

def writeplaintext(text):
	with open('plaintext.txt', 'w+' ) as w:
		w.write(text)
	

if __name__ == "__main__" :

	with open ('ciphertext.txt', 'r') as ciphertext:
		text = ciphertext.read()
		print "\n HERE IS THE FREQUENCY TABLES THAT READING FROM CIPHER TEXT\n"
		print (frequency(text))  
                print "\n THE PLAIN TEXT WILL BE WIRTE TO A FILE IN YOUR DIR \n"
		print ("ALPHABET:",alphabet)
		print ("KEY:",key)
		writeplaintext(printplaintext(text))
		




