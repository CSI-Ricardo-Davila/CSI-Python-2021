import random


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



used_letters =[]
invalid_caracters= ["!","@","~","`","#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}","|",":",";","'","<",",",".",">","/","?"]
invalid_numbers = ["0","1","2","3","4","5","6","7","8","9"]
word_list = ["playa","oceano","patineta","zapato","tabla","generador","palma","computadora","televisor","pelicula","fotografia","comida","Patillas","Barceloneta","municipio","Vieques","gobernador","ventana","Aibonito","Culebra"]
wrong_letter = "_"
# def get_word():
#     word_list = ["playa","oceano","patineta","zapato","tabla","generador","palma","computadora","televisor","pelicula","fotografia","comida","Patillas","Barceloneta","municipio","Vieques","gobernador","ventana","Aibonito","Culebra"]
#     return random.choice(word_list)
def get_word():
    word =  random.choice(word_list)
    return word

def get_input():
    
    while(True):
        letter = input("Chose your letter")

        if(len(letter)!= 1):
            print("error")
            continue

        if((letter)in used_letters):
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

print(get_input())

def print_word():
    temp:str = ""
    # len(word)
    for letter in my_word:
        if (letter not in my_word):
            return wrong_letter
            continue
        if (letter in my_word):
            print(letter)
            continue

    print(temp)



my_word = get_word()
while True:
    print(steps[0]) 
    get_input()
    print_word()
