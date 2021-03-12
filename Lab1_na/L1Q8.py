def compare(p1,p2):
    if p1==p2:
        print("It's a tie")
    elif p1==1: #paper beats rock
        if p2==2:
            print("Player 2 wins!")
        else: #rock beats scissors
            print("Player 1 wins!")
    elif p1==2: #scissors beats paper
        if p2==3:
            print("Player 2 wins!")
        else: #paper beats rock
            print("Player 1 wins!")
    elif p1==3: #rock beats scissors
        if p2==1:
            print("Player 2 wins!")
        else: #scissors beats paper
            print("Player 1 wins!")

while True:
    opt=input("\nDo you want to start a new game?\n1-Yes\n2-No\n")
    if opt==1:
        p1=input("Player 1: Choose one: (1-rock,2-paper,3-scissors)")
        p2=input("Player 2: Choose one: (1-rock,2-paper,3-scissors) ")
        compare(p1,p2)
    else:
        break
