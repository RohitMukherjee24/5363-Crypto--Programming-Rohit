#Name: Rohit Mukherjee
#Course: 5363 cryptography
#professor : Dr.Terry Griffin
#Program-2: randomized_vigenere.py

# importing copy and random for further use in this Vigenere class
import copy
import random

class Vigenere:
    # symbols are the list of characters from ascii values 32 to 126
    symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
    #Ctext & Ptext are two empty lists.
    Ctext = []
    Ptext = []
    
    #using seed to create keyword
    #copyright goes to professor terry griffin,i just edited the 95 characters and 32 which coverers all the characters upto 32 to 126
    def keywordFromSeed(self,seed):
        Letters = []
        while seed > 0:
            Letters.insert(0,chr((seed % 100) % 95 + 32))
            seed = seed // 100
        return ''.join(Letters)
    
    #Encyption procedure to encrypt the plain message
    def encrypt(self,pmessage,seed):
        # assigning variales to zeros that used further in this procedure
        b=0
        j=0
        #generating keyword using unique seed which is given through command line
        Genkey = self.keywordFromSeed(seed)
        #random vigenere table is generated
        vigenere = self.buildVigenere(self.symbols,seed)
        # assigning None to that list Ctext in the  range of length of message
        self.Ctext = [None for x in range(len(pmessage))]
        # assigning zero's to that list key in the  range of length of Genkey
        key=[[0] * i for i in range(len(Genkey))]
        #copying the  Genkey list into Key list thats why i imported copy in the top of the program
        key = copy.copy(Genkey)
        while(b<len(pmessage)):
            for c in range(len(Genkey)):
                for i in range(len(self.symbols)):
                    if(vigenere[i][0]==key[c]):
                        if(b<len(pmessage)):
                            symbol=ord(pmessage[b])-32
                            self.Ctext[b]=vigenere[i][symbol]
                b+=1
        return ''.join(self.Ctext)
    
    #Decryption procedure to decrypt the encripted message
    def decrypt(self,Cmessage,seed):
        # assigning variales to zeros that used further in this procedure
        q=0
        i=0
        c=0
        #random vigenere table is generated
        vigenere = self.buildVigenere(self.symbols,seed)
        # assigning None to that list Ptext in the  range of length of cryted_message
        self.Ptext=[None for x in range(len(Cmessage))]
        #Assigning length of symbols to lensym for ease of usage
        lensym=len(self.symbols)
        #generating keyword using unique seed which is given through command line
        Genkey =self. keywordFromSeed(seed)        
        # assigning zero's to that list key in the  range of length of Genkey
        key=[[0] * i for i in range(len(Genkey))]
        #copying the  Genkey list into Key list thats why i imported copy in the top of the program
        key = copy.copy(Genkey)
        while(len(Cmessage)>q):
            for c in range(len(Genkey)):
                for j in range(lensym):
                    if vigenere[j][0]==key[c]:
                        if q<len(Cmessage):
                            for b in range(lensym):
                                if(vigenere[j][b]==Cmessage[q]):
                                    symbol=b+32
                                    self.Ptext[q]=chr(symbol)
                q+=1
        return ''.join(self.Ptext)
    
    # BuildVigenere procedure is taken from srikanth  which helps us to buld randomised 95 X 95 matrix.
    # copyrights goes to srikant veeralli who provides us the matrix implementation to work with.
    def buildVigenere(self,symbols,seed):
        random.seed(seed)
        n = len(symbols)
        vigenere = [[0 for i in range(n)] for i in range(n)]
        symbols = list(symbols)
        random.shuffle(symbols)
        symbols = ''.join(symbols)
        for sym in symbols:
            random.seed(seed)
            myList = []
        
            for i in range(n):
                r = random.randrange(n)
                
                if r not in myList:
                    myList.append(r)
                else:
                    while(r in myList):
                        r = random.randrange(n)
                    myList.append(r)
                                   
                while(vigenere[i][r] != 0):
                    r = (r + 1) % n
                
                vigenere[i][r] = sym
                
        return vigenere