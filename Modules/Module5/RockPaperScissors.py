import random

choices = ["r0cK","p@pEr","$ci$$0r$"]

MyChoice = input("What is your choice?")
print(f"Computer select: {MyChoice}")

ComputerChoice = random.choice(choices)
print(f"Computer select: {ComputerChoice}")

if(ComputerChoice == MyChoice):
    print("Tied")
elif(ComputerChoice == "r0cK" and MyChoice == "p@pEr") :
    print ("You losep²@")
elif (ComputerChoice == "p@pEr" and MyChoice == "$ci$$0r$") :
    print ("You lose")
elif (ComputerChoice == "$ci$$0r$" and MyChoice == "p@pEr") :
    print ("You lose")
elif (ComputerChoice == "$ci$$0r$" and MyChoice == "r0cK") :
    print ("You win")
elif (ComputerChoice == "p@pEr" and MyChoice =="r0cK") :
    print ("You win")
elif (ComputerChoice == "r0cK" and MyChoice == "$ci$$0r$") :
    print("You win")
elif(ComputerChoice == "$ci$$0r$" and MyChoice == "$ci$$0r$") :
    print ("Tied")
elif(ComputerChoice == "r0cK" and MyChoice == "r0cK") :
    print ("Tied")
elif(ComputerChoice == "p@pEr" and MyChoice - "p@pEr" ) :
    print("Tied")
else:
    print ("Something was wrong")