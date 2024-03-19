from random import randint
from time import sleep
from signs import hands, start
import os
from msvcrt import getwch
from colors import bcolors

os.system('cls')
wins = 0 #}
ties = 0 #}
losses = 0 #} Initierar variablar för olika värden som förändras under spelet
rounds = 0 #}

rock = 0 #}
paper = 1 #} anger vilka nummer som sten, sax och påse har under spelet så det går att jämföra datorn och användarens svar
scissor = 2 #}

print(start.splash)
while True:
    ai = randint(0, 2)
    user = getwch().upper() #Använder upper för att slippa använda stor och liten bokstav i if-satserna
    rounds +=1
    if user == "R":
        os.system('cls')
        if ai == rock:
            print(f"You chose:\n{hands.rock}\n\nAi chose:\n{hands.rock}\n{bcolors.YELLOW}It's a tie!{bcolors.DEFAULT}") #Visar vad du och ai valde och visar att det blev lika
            ties += 1
            print(f"Wins: {wins} Ties: {ties} Losses: {losses} Rounds: {rounds}")
            print("""To continue playing, press either (R)ock, (P)aper or (S)cissors
Press Q to quit""")

        elif ai == paper:
            print(f"You chose:\n{hands.rock}\n\nAi chose:\n{hands.paper}\n{bcolors.RED}You lost!{bcolors.DEFAULT}")
            losses +=1
            print(f"Wins: {wins} Ties: {ties} Losses: {losses} Rounds: {rounds}")
            print("""To continue playing, press either (R)ock, (P)aper or (S)cissors
Press Q to quit""")

        elif ai == scissor:
            print(f"You chose:\n{hands.rock}\n\nAi chose:\n{hands.scissor}\n{bcolors.GREEN}You won!{bcolors.DEFAULT}")
            wins += 1
            print(f"Wins: {wins} Ties: {ties} Losses: {losses} Rounds: {rounds}")
            print("""To continue playing, press either (R)ock, (P)aper or (S)cissors
Press Q to quit""")

    if user == "P":
        os.system('cls')
        if ai == rock:
            print(f"You chose:\n{hands.paper}\n\nAi chose:\n{hands.rock}\n{bcolors.GREEN}You won!{bcolors.DEFAULT}")
            wins += 1
            print(f"Wins: {wins} Ties: {ties} Losses: {losses} Rounds: {rounds}")
            print("""To continue playing, press either (R)ock, (P)aper or (S)cissors
Press Q to quit""")

        elif ai == paper:
            print(f"You chose:\n{hands.paper}\n\nAi chose:\n{hands.paper}\n{bcolors.YELLOW}It's a tie!{bcolors.DEFAULT}")
            ties +=1
            print(f"Wins: {wins} Ties: {ties} Losses: {losses} Rounds: {rounds}")
            print("""To continue playing, press either (R)ock, (P)aper or (S)cissors
Press Q to quit""")

        elif ai == scissor:
            print(f"You chose:\n{hands.paper}\n\nAi chose:\n{hands.scissor}\n{bcolors.RED}You lost!{bcolors.DEFAULT}") 
            losses += 1
            print(f"Wins: {wins} Ties: {ties} Losses: {losses} Rounds: {rounds}")
            print("""To continue playing, press either (R)ock, (P)aper or (S)cissors
Press Q to quit""")

    if user == "S":
        os.system('cls')
        if ai == rock:
            print(f"You chose:\n{hands.scissor}\n\nAi chose:\n{hands.rock}\n{bcolors.RED}You lost!{bcolors.DEFAULT}")
            losses += 1
            print(f"Wins: {wins} Ties: {ties} Losses: {losses} Rounds: {rounds}")
            print("""To continue playing, press either (R)ock, (P)aper or (S)cissors
Press Q to quit""")

        elif ai == paper:
            print(f"You chose:\n{hands.scissor}\n\nAi chose:\n{hands.paper}\n{bcolors.GREEN}You won!{bcolors.DEFAULT}")
            wins +=1
            print(f"Wins: {wins} Ties: {ties} Losses: {losses} Rounds: {rounds}")
            print("""To continue playing, press either (R)ock, (P)aper or (S)cissors
Press Q to quit""")

        elif ai == scissor:
            print(f"You chose:\n{hands.scissor}\n\nAi chose:\n{hands.scissor}\n{bcolors.YELLOW}It's a tie!{bcolors.DEFAULT}")
            ties += 1
            print(f"Wins: {wins} Ties: {ties} Losses: {losses} Rounds: {rounds}")
            print("""To continue playing, press either (R)ock, (P)aper or (S)cissors
Press Q to quit""")

    elif user == "Q":
        os.system('cls')
        exit()