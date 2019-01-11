import random
import time
import os

def passwordGenerator():
    clear()
    print("Welcome to Password Generator v1.0.0")
    print("Would you like a Memorable or Secure password?")
    time.sleep(2)
    askType()

def askType():
    typePass = raw_input("Type 'memorable' or 'secure' - ")
    if typePass == "memorable":
        memorablePassGen()
    elif typePass == "secure":
        securePassGen()
    else:
        passwordGenerator()

def clear(): 
  os.system('cls' if os.name == 'nt' else 'clear')

def memorablePassGen():
    clear()
    print("Generating Memorable Password (0%)")
    time.sleep(0.5)
    clear()
    print("Generating Memorable Password (25%)")
    time.sleep(0.5)
    clear()
    print("Generating Memorable Password (50%)")
    time.sleep(0.5)
    clear()
    print("Generating Memorable Password (75%)")
    time.sleep(0.5)
    clear()
    print("Generating Memorable Password (100%)")
    time.sleep(1)
    clear()
    time.sleep(0.1)
    
    for i in range(1):
        w1num=int(random.randint(1,10))
        if w1num==1:
            w1str="Zippy"
        elif w1num==2:
            w1str="System"
        elif w1num==3:
            w1str="Ritzy"
        elif w1num==4:
            w1str="Immense"
        elif w1num==5:
            w1str="Brother"
        elif w1num==6:
            w1str="Damp"
        elif w1num==7:
            w1str="Scarf"
        elif w1num==8:
            w1str="Name"
        elif w1num==9:
            w1str="Optimal"
        elif w1num==10:
            w1str="Red"
    for i in range(1):
        w2num=int(random.randint(1,10))
        if w2num==1:
            w2str="Amount"
        elif w2num==2:
            w2str="Dress"
        elif w2num==3:
            w2str="Stranger"
        elif w2num==4:
            w2str="Wooden"
        elif w2num==5:
            w2str="Five"
        elif w2num==6:
            w2str="Water"
        elif w2num==7:
            w2str="Cute"
        elif w2num==8:
            w2str="Cry"
        elif w2num==9:
            w2str="Stick"
        elif w2num==10:
            w2str="Bells"
    for i in range(1):
        w3num=int(random.randint(1000,10000))
        w4num=int(random.randint(1000,10000))
        
    print "Your password is - "
    print w1str+str(w4num)+w2str+str(w3num)
    time.sleep(5)
    askAgain()
    
def securePassGen():
    clear()
    print("Generating Secure Password (0%)")
    time.sleep(0.5)
    clear()
    print("Generating Secure Password (25%)")
    time.sleep(0.5)
    clear()
    print("Generating Secure Password (50%)")
    time.sleep(0.5)
    clear()
    print("Generating Secure Password (75%)")
    time.sleep(0.5)
    clear()
    print("Generating Secure Password (100%)")
    time.sleep(1)
    clear()
    time.sleep(0.1)
    
    
    securePass = ""
    characters = '0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!@#$%^&*'
    for i in range(1):
        charNum=int(random.randint(5,25))
    for i in range(1,charNum):
        securePass+= random.choice(characters)
    print("You password is - ")
    print securePass
    time.sleep(5)
    askAgain()

def askAgain():
    print("")
    print("")
    goAgain = raw_input("Go again? - ")
    if goAgain == "yes":
        passwordGenerator()
    elif goAgain == "y":
        passwordGenerator()
    
passwordGenerator()