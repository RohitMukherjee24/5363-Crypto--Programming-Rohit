#Name: Rohit Mukherjee
#Course: 5363 cryptography
#professor : Dr.Terry Griffin
#Program-2: main.py

import argparse
from randomized_vigenere import Vigenere 

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
parser.add_argument("-s", "--seed", dest="seed",type = int,help="Integer seed") # here i just added the type as integer of argument seed

args = parser.parse_args()

#seed should be an integer type if already not checked while passing the ragument then
#seed = int(args.seed)
seed=args.seed

f = open(args.inputFile,'r')
message = f.read()

if(args.mode == 'encrypt'):
    data = Vigenere().encrypt(message,seed)
else:
    data = Vigenere().decrypt(message,seed)
    
o = open(args.outputFile,'w')
o.write(str(data))
o.close()