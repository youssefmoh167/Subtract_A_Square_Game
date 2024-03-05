
# Purpose: The game is called subtract a square where 2 players start the game with a pile of coins each player takes turn removing non-zero square number of coins and the player that removes the last coin wins.
# Author: Youssef Mohamed Ali Mohamed Ali



#start game
print ("WELCOME TO THE SUBTRACT A SQUARE GAME")
while True:#checking if the user entered anything but a number
    try:
        coins= int(input("Enter the number of coins to start the game: "))
        while (coins**0.5)%1 == 0: #if the players enter square number of coins at the beginning of the game
            coins = int(input('''You cannot start the game with a square number\nPlease enter another number of coins:'''))
        break
    except ValueError:
        print ("Error,Please enter a valid number not letters")
while coins >= 1 :
#player1's turn
    while True:#checking if the user entered anything but a number
        try:
            p1= int(input('''PLAYER1, Enter a non-zero square number to remove from the pile:'''))
  #stating the exceptions           
            while (p1**0.5) != int(p1**0.5) or p1 == 0 or p1>coins :
                p1 = int(input("Please enter a valid non-zero square number to remove from the pile:"))
            break
        except ValueError:
            print ("Error,Please enter a valid number not letters")
    
    #stating the exceptions 
    while (p1**0.5) == int(p1**0.5):#if the square root of the number is an integer
        coins -= p1
        print(f"THE COINS COUNTER NOW IS {coins}")
        break
    if coins == 0:
        print("P1 WON") 
        break
	#the game ends
#player2's turn
    while True:#checking if the user entered anything but a number
        try:
            p2 = int(input('''PLAYER2, Enter a non-zero square number to remove from the pile:'''))
            while (p2**0.5) != int(p2**0.5) or p2 == 0 or p2>coins :
                p2=int(input("Please enter a valid non-zero square number to remove from the pile:"))
            break
        except ValueError:
            print ("Error,Please enter a valid number not letters")
    
    while (p2**0.5) != int(p2**0.5) or p2 == 0 or p2>coins :
        p2=int(input("Please enter a valid non-zero square number to remove from the pile:"))
    while (p2**0.5) == int(p2**0.5):#if the square root of the number is an integer
        coins -= p2
        print(f"THE COINS COUNTER NOW IS {coins}")
        break
        if (p2**0.5) == int(p2**0.5):#if the square root of the number is an integer
            coins -= p2
            print(f"THE COINS COUNTER NOW IS {coins}")
            break
    if coins == 0:
        print ("P2 WON")
        break #the game ends