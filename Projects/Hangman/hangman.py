import random
from tkinter.ttk import setup_master
from turtle import st


#La variable steps contiene las diferentes etapas del hangman
steps = ["""             
          |----------|
          |
          |
          |
          |
          |
          |
          |
         """,
         """            
          |----------|
          |         OO
          |        ---- 
          |        
          |
          |
          |
          |
         """,
         """            
          |----------|
          |         OO
          |        ---- 
          |          | 
          |          |
          |          |
          |
          |
         """,
         """            
          |----------|
          |         OO
          |        ---- 
          |          | 
          |       ---|
          |          |
          |          
          |         
         """,   
        
         """            
          |----------|
          |         OO
          |        ---- 
          |          | 
          |       ---|---
          |          |
          |
          |
         """,
            """            
          |----------|
          |         OO
          |        ---- 
          |          | 
          |       ---|---
          |          |
          |          ^
          |         ^
         """,
         """            
          |----------|
          |         OO
          |        ---- 
          |          | 
          |       ---|---
          |          |
          |          ^
          |         ^ ^
         """
         ]
#  int var 0

#La lista de used_letters se utiliza para poner en una lista las letras de la palabra que hay que adivinar para que una vez adivine la primera letra, verifique si está en esta lista y puede seguir corriendo el código
used_letters =[]
#La lista de invalid_caracters contiene todos los simbolos que no se pueden utilizar en la palabra para que una vez adivine la primera letra, verifique si está en esta lista y puede seguir corriendo el código
invalid_caracters= ["!","@","~","`","#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}","|",":",";","'","<",",",".",">","/","?"]
#La lista de invalid_numbers
invalid_numbers = ["0","1","2","3","4","5","6","7","8","9"]
word_list = ["playa","oceano","patineta","zapato","tabla","generador","palma","computadora","televisor","pelicula","fotografia","comida","Patillas","Barceloneta","municipio","Vieques","gobernador","ventana","Aibonito","Culebra"]
wrong_letter = "_"
# def get_word():
#     word_list = ["playa","oceano","patineta","zapato","tabla","generador","palma","computadora","televisor","pelicula","fotografia","comida","Patillas","Barceloneta","municipio","Vieques","gobernador","ventana","Aibonito","Culebra"]
#     return random.choice(word_list)
def get_word():
    word =  random.choice(word_list)
    return word.upper()

my_word = get_word()

def get_input():
    
    while(True):
        letter = input("Chose your letter").upper()

        if(len(letter)!= 1):
            print("error")
            continue

        if(letter in used_letters):
            print("You already used this letter")
            continue

        if(letter in invalid_numbers):
            print("error")
            continue

        if(letter in invalid_caracters):
            print("error")
            continue

        
        used_letters.append(letter)
        return letter


def print_word():
    temp:str = ""
    # len(word)
    for letter in my_word:
        if (letter in used_letters):
            temp = temp + letter

        else:
            temp = temp + "_"
            


    print(temp)

def get_steps():

    steps_int_variable = 0

    for letter in my_word:
        if (letter in used_letters):
            steps = steps[0]
        else:
            steps = steps[steps_int_variable + 1]
        return steps
    
# def print_steps():
#     for letter in my_word:
#         if (letter in used_letters):
#             print(steps[0])
#         else:
#             print(steps[get_steps()])
#         return steps
while True:
    get_steps()
    get_input()
    print_word()
    # 




    
