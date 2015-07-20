import fractions
import cryptoMath
import os

file1 = open('Input.txt').readlines()                      # Input file reading line by line
file1 = [file1.strip('\n').upper() for file1 in file1]     # making it uppercase all the letters 
dictionary = open('dictionary.txt').read()                 # Read the dictionary 

Maxcount = 0                                               # Maxcount is used to keep track of words count in a line 
maxPhrase =""                                              # maxphrase is the line which has max-count of elements similar with Dictionary

for linebyline in file1:                                   # for loop goes on line by line
    count = 0                                              # count assigned to zero
    for word in linebyline.split():                        # for loop for words which are separated using phrase.split()
        if word in dictionary.split():                     # if the above word is in dictionary which is splitted suing dictionary.split()
            count += 1                                     # increment the count if matches
    if(Maxcount < count):                                  # if Maxcount is less than new count then replace it with count
        Maxcount = count                                   # assigning count to Maxcount
        maxPhrase += linebyline                            # assigning the max number of count line to maxphrase
print("Maximum word count match line is:" + maxPhrase)     # printing maxphrase
