ongoing = True


def winner(p1, p2):
    if str(p1).lower() == str(p2).lower():
        print("Its a tie")
    elif str(p1).lower() == "P" and str(p2).lower() == "R" or str(p1).lower() == "R" and str(p2).lower() == "S" or str(
            p1).lower() == "S" and str(p2).lower() == "P":
        print("Player 1 is the winner, Congrats!")
    else:
        print("Player 2 is the winner, Congrats!")


while ongoing:

    p1 = input("Player 1 please enter your choice:- \n[R]ock\n[P]aper\n[S]cissors\n")
    p2 = input("Player 2 please enter your choice:- \n[R]ock\n[P]aper\n[S]cissors\n")
    winner(p1, p2)
    check = input("Another round?\n[N]o\n[Y]es\n")
    if check == "N":
        ongoing = False
