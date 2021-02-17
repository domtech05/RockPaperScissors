# imports single player and multiplayer functions
import time as t
import random


#set scores to 0
scpu = 0
splayer = 0


#definitions for single player
def singleplayer():
    print("####################################")
    print("Rock, Paper, Scissors: Singleplayer")
    print("####################################")
    rpscpu()
def rpscpu():
    comp_possible = 1, 2, 3
    comp_choice = random.choice(comp_possible)
    if comp_choice == 1:
        computer_choice_rock()
    elif comp_choice == 2:
        computer_choice_paper()
    else:
        computer_choice_scissors()
    return comp_choice
def computer_choice_rock(): #CPU selects rock
    global scpu
    global splayer
    user_choice = int(input("1 for rock, 2 for paper, 3 for scissors: "))
    if user_choice == 1:
        print("\n####################################")
        print("Tie - You and the CPU chose Rock")
        scpu += 1
        splayer += 1
        try_again()
    if user_choice == 2:
        print("\n####################################")
        print("Win - You selected Paper. CPU selected Rock")
        splayer += 1
        try_again()
    if user_choice == 3:
        print("\n####################################")
        print("Lose - You selected scissors. CPU selected Rock")
        scpu += 1
        try_again()
    else:
        print("\nTry again")
        computer_choice_rock()
def computer_choice_paper(): #   CPU selects paper
    #   CPU selects paper
    global scpu
    global splayer
    user_choice = int(input("1 for rock, 2 for paper, 3 for scissors: "))
    if user_choice == 1:
        print("\n####################################")
        print("Lose - You selected rock. CPU selected paper")
        scpu += 1
        try_again()
    if user_choice == 2:
        print("\n####################################")
        print("Tie - You and the CPU chose paper")
        scpu += 1
        splayer += 1
        try_again()
    if user_choice == 3:
        print("\n####################################")
        print("Win - You selected scissors. CPU selected paper")
        splayer += 1
        try_again()
    else:
        print("\nTry again")
        computer_choice_paper()
def computer_choice_scissors():
    #CPU selects scissors
    global scpu
    global splayer
    user_choice = int(input("1 for rock, 2 for paper, 3 for scissors: "))
    if user_choice == 1:
        print("\n####################################")
        print("Win - You selected rock. CPU selected scissors")
        splayer += 1
        try_again()
    if user_choice == 2:
        print("\n####################################")
        print("Lose - You selected Paper. CPU selected scissors")
        scpu += 1
        try_again()
    if user_choice == 3:
        print("\n####################################")
        print("Tie - You selected scissors. CPU selected scissors")
        scpu += 1
        splayer += 1
        try_again()
    else:
        print("\nTry again")
        computer_choice_rock()
def try_again(): #end of round menu
    global scpu
    global splayer
    print("\n####################################")
    print("current score:\n Player:" , splayer, " \n CPU:" , scpu)
    print("####################################")
    endofround_menu()
def endofround_menu():
    choice = input("Would you like to play again (y / n) or return to menu (m)? Y/N/M?: ")
    if choice == "y":
        rpscpu()
    elif choice == "n":
        print("\nThanks for playing!")
        quit()
    elif choice == "m":
        runner()
    else:
        print("\ninvalid input. Please try again")
        endofround_menu()


#Definitions for multiplayer
mplayer1 = 0
mplayer2 = 0
def multiplayer():
    print("\n####################################")
    print("Rock, Paper, Scissors: Multiplayer")
    print("####################################")
    p1_count = 0
    print("\nPLAYER 1 GOES FIRST ...")
    p1_in = (input("\nR FOR ROCK, P FOR PAPER, S FOR SCISSORS: "))
    while p1_count != 50:
        if p1_in == "R" or p1_in == "P" or p1_in == "S" or p1_in == "r" or p1_in == "p" or p1_in == "s":
            print(" ")
            p1_count = p1_count+1
    else:
        if p1_in == "R" or p1_in == "r" or p1_in == "Rock" or p1_in == "rock":
            p1_rock()
        elif p1_in == "P" or p1_in == "p" or p1_in == "Paper" or p1_in == "paper":
            p1_paper()
        if p1_in == "S" or p1_in == "s" or p1_in == "Scissors" or p1_in == "scissors":
            p1_scissors()
        else:
            print("\nPlayer 1 input not recognised. Try again")
            p1_in = (input("\nR FOR ROCK, P FOR PAPER, S FOR SCISSORS: "))
def p1_rock(): #p1 selects rock
    global mplayer1
    global mplayer2
    print("YOUR TURN PLAYER 2>>>")
    p2_in = (input("R FOR ROCK, P FOR PAPER, S FOR SCISSORS: "))
    if p2_in == "r":
        print("\n####################################")
        print("\nResults:")
        t.sleep (2)
        print("\nTie - You both selected Rock")
        mplayer1 = mplayer1+1
        mplayer2 = mplayer2+1
        sptry_again()
    elif p2_in == "p":
        print("\n####################################")
        print("\nresults:")
        t.sleep (2)
        print("\nPlayer 2 wins! P1 selected rock, P2 selected Paper")
        mplayer2 = mplayer2+1
        sptry_again()
    if p2_in == "s":
        print("\n####################################")
        print("\nResults:")
        t.sleep (2)
        print("\nPlayer 1 wins! P1 selected rock, P2 selected scissors")
        mplayer1 = mplayer1+1
        sptry_again()
    else:
        print("\nInvalid input, Try again")
        p1_rock()
def p1_paper(): #p1 selects paper
    global mplayer1
    global mplayer2
    print("YOUR TURN PLAYER 2>>>")
    p2_in = (input("R FOR ROCK, P FOR PAPER, S FOR SCISSORS: "))
    if p2_in == "r":
        print("\n####################################")
        print("\nResults:")
        t.sleep (2)
        print("\nPlayer 1 wins! P1 selected paper, P2 selected rock.")
        mplayer1 = mplayer1+1
        sptry_again()
    elif p2_in == "p":
        print("\n####################################")
        print("\nResults:")
        t.sleep (2)
        print("\nTie - You both selected paper")
        mplayer1 = mplayer1+1
        mplayer2 = mplayer2+1
        sptry_again()
    if p2_in == "s":
        print("\n####################################")
        print("\nResults:")
        t.sleep(2)
        print("\nWin - Player 2 selected scissors. Player 1 selected Paper")
        mplayer2 += 1
        sptry_again()
    else:
        print("\nInvalid input, Try again")
        p1_rock()
def p1_scissors(): #p1 selects scissors
    global mplayer1
    global mplayer2
    print("YOUR TURN PLAYER 2>>>")
    p2_in = (input("R FOR ROCK, P FOR PAPER, S FOR SCISSORS: "))
    if p2_in == "r":
        print("\n####################################")
        print("\nResults:")
        t.sleep (2)
        print("\nPlayer 2 wins! P1 selected scissors, P2 selected rock.")
        mplayer2 += 1
        sptry_again()
    elif p2_in == "p":
        print("\n####################################")
        print("\nResults:")
        t.sleep(2)
        print("\nPlayer 1 wins! P1 selected scissors, P2 selected paper")
        mplayer1 += 1
        sptry_again()
    if p2_in == "s":
        print("\n####################################")
        print("\nResults:")
        t.sleep (2)
        print("\nTie - You both selected scissors")
        mplayer1 += 1
        mplayer2 += 1
        sptry_again()
    else:
        print("\nInvalid input, Try again")
        p1_rock()
def sptry_again(): #end of round
    global mplayer1
    global mplayer2
    print("\n####################################")
    print("Current Scores: \nPlayer 1: ", mplayer1, " | Player 2: ", mplayer2)
    print("####################################")
    choice = input("\nWould you like to play again (y / n) or return to menu(m) Y/N/M?: ")
    if choice == "y":
        multiplayer()
    elif choice == "n":
        print("\nThanks for playing!")
        quit()
    elif choice == "m":
        print("\nGoing back to menu. Please wait.......")
        t.sleep(2)
        runner()


#MAIN RUNNER CODE
def runner():
    exitCalled = False

    #print GUI
    print ("Welcome to rock paper scissors!")
    print (" Main menu\n1. Singleplayer\n2. Multiplayer\n3. Exit")
    grabUserInput = int(input("enter an option: "))

    while exitCalled != True:
        if grabUserInput == 1:
            print ("beginning singleplayer game. Please wait......")
            t.sleep(2)
            singleplayer()
        elif grabUserInput == 2:
            print("Beginning Multiplayer game. Please wait.......")
            t.sleep(2)
            multiplayer()
        elif grabUserInput == 3:
            exitCalled = True
            exit()
        else:
            print("INVALID INPUT. Please try again.")
            grabUserInput = int(input("Enter and option: "))


#START GAME
runner()
