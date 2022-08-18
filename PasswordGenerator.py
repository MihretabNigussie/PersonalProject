import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","(",")","_","+","|"]
# You can also add other symbols that are not included here and also you can add upper case letters

def passwordGenerator (letter , number , symbol):
    passwordGenerated= []
    
    for i in range(letter):
        lettersGenerated = random.choice(letters)
        passwordGenerated.append(lettersGenerated)
        
    for i in range(number):
        numbersGenerated = random.choice(numbers)
        passwordGenerated.append(numbersGenerated)

    for i in range(symbol):
        symbolsGenerated = random.choice(symbols)
        passwordGenerated.append(symbolsGenerated)

    random.shuffle(passwordGenerated)
    # to make my password very hard to crack, I need to shuffle the letters, numbers and symbols


    My_Password = ""
    for item in passwordGenerated:
        My_Password += item
   
    return My_Password
        
            
        
    
        
        


