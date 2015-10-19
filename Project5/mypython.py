#CS344 Program #5
#Gerald Gale 
import sys
import random 
import string 

#Crate data variables
randomWords = []
randomLetters = ""
randomNumber1 = 0
randomNumber2 = 0
randomNumberProduct = 0

#Print out instructions
print "Hello human, we will generate 3 strings each containing 10 lowercase ASCII characters, \n"
print "and place each string into its own file called file1.txt, file2.txt, & file3.txt respectively."
print "We have a surprise for you at the very end. It's simple, but we think you will like it."
print "\n\n"

#Perform calculations for 3 strings with 10 random ascii characters each
#Then output them into a file and print them on screen
for i in range(0, 3):
	for j in range(0, 10):
		randomLetters = randomLetters + str( random.choice(string.ascii_lowercase))
	
	randomWords.append(randomLetters)
	
	fileName = "file" + str(i + 1) + ".txt" 
	newFile = open(fileName, 'w')
	newFile.write(randomWords[i] + "\n")
	newFile.close()
	print "File " + str(i + 1) + " contains: " + randomWords[i]	
	
	randomLetters = ""

#Print results of the 3 strings
print "We have created the 3 files that you need."
print "SURPRISE!\nWe will now create 2 random integers from 1 to 42 and then find the product of those two numbers.\n"

#Create the random numbers and the product 
randomNumber1 = random.randint(1, 42)
randomNumber2 = random.randint(1, 42)
randomNumberProduct = randomNumber1 * randomNumber2

#Print out the random numbers and the product 
print "Your first random number is: " + str(randomNumber1)
print "Your second random number is: " + str(randomNumber2) 
print "The product of your random numbers is: " + str(randomNumberProduct) 

