import random

def displaymenu():
    print('What would you like to do?\n')
    print('1. Start New Game')
    print('2. Load Game')
    print('3. Quit\n')
    choice  = int(input('Enter choice: '))
    return choice

def gamedisplay():
    print("What would you like to do?\n")
    print("1. Play Again")
    print("2. View Statistics")
    print("3. Quit")

    option = int(input("Enter Choice: "))
    return option

def rpsdisplay():
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')

    rpsoption = int(input('What will it be? '))
    return rpsoption

def loaduserinfo():
    filename = input("Enter your name: ")
    try:
        f = open(filename + ".rps", "r")
        userinfo = {"name": "", "wins": 0, "loss": 0, "ties": 0}
        linenum = 0
        for line in f:
            if linenum == 0:
                userinfo["name"] = line.strip()
            elif linenum == 1:
                userinfo["wins"] = int(line)
            elif linenum == 2:
                userinfo["loss"] = int(line)
            elif linenum == 3:
                userinfo["ties"] = int(line)
            linenum += 1
        return userinfo
    except OSError:
        print("Hello "+ filename + " Your game file cound not be found")


def saveGame(userinfo):
    f = open(userinfo["name"] + ".rps", "w")
    f.write(userinfo["name"] +"\n"+ str(userinfo["wins"]) + "\n" + str(userinfo['loss']) + "\n" + str(userinfo["ties"]))
    f.close()

    print(userinfo["name"] + ", Your game has been saved")


def calcwin(user,computer):
    if user == 1 and computer == 1:
        return "tie"
    elif user == 1 and computer == 2:
        return "computer"
    elif user == 1 and computer == 3:
        return "user"
    elif user == 2 and computer == 1:
        return "user"
    elif user == 2 and computer == 2:
        return "tie"
    elif user == 2 and computer == 3:
        return "computer"
    elif user == 3 and computer == 1:
        return "computer"
    elif user == 3 and computer == 2:
        return "user"
    elif user == 3 and computer == 3:
        return "tie"

def rpscheck(check):
    if check == 1:
        return "rock"
    elif check == 2:
        return "paper"
    elif check == 3:
        return "scissors"

def showuserstats(round, userinfo):
    print(userinfo['name'] + ", here are your game play statistics...")
    print("Wins: " + str(userinfo["wins"]))
    print("Losses: " + str(userinfo["loss"]))
    print("Ties: " + str(userinfo["ties"]))
    if userinfo["wins"] == 0:
        print("Win/Loss Ratio: 0\n")
    else:
        print("Win/Loss Ratio: " + str(float(userinfo["wins"]/userinfo["loss"]))+ "\n")
    choice = gamedisplay()
    if choice == 1:
        runRPS(round +1,userinfo)
    elif choice == 2:
        showuserstats(round , userinfo)
    elif choice == 3:
        saveGame(userinfo)
    else:
        print("Please enter a valid choice ")




def runRPS(round, userinfo):
    print("Round "+ str(round))
    userrps = rpsdisplay()
    if userrps > 3 or userrps < 1:
        print("Please enter a numeric value between 1 and 3")
        runRPS(round, userinfo)
    else:
        computer = random.randint(1,3)
        checkwin = calcwin(userrps, computer)
        if checkwin == "user":
            print("You chose " + rpscheck(userrps) + ". The computer chose " + rpscheck(computer) + ". You win!")
            userinfo["wins"] += 1
        elif checkwin == "computer":
            print("You chose " + rpscheck(userrps) + ". The computer chose " + rpscheck(computer) + ". You lose!")
            userinfo["loss"] += 1
        elif checkwin == "tie":
            print("You chose " + rpscheck(userrps) + ". The computer chose " + rpscheck(computer) + ". You tied!")
            userinfo["ties"] += 1
        choice = gamedisplay()
        if choice == 1:
            runRPS(round +1,userinfo)
        elif choice == 2:
            showuserstats(round , userinfo)
        elif choice == 3:
            saveGame(userinfo)
        else:
            print("Please enter a valid vhoice ")
        
        
    
def createnewgame():
    name = input("What is your name? ")
    print("Hello " + name + ", Let's Play!")
    userinfo = {"name":name, "wins":0, "loss": 0, "ties": 0 }

    runRPS(1, userinfo)

 

def main():
    print("Welcome to Rock, Paper, Scissors\n")
    choice = displaymenu()
    if choice == 1:
        createnewgame()
    elif choice == 2:
        userinfo = loaduserinfo()
        print("Welcome back, " + userinfo["name"] + " let's play again!")
        savedrounds = userinfo["wins"] + userinfo["loss"] + userinfo["ties"]
        choice = gamedisplay()
        if choice == 1:
            runRPS(savedrounds +1,userinfo)
        elif choice == 2:
            showuserstats(savedrounds , userinfo)
        elif choice == 3:
            saveGame(userinfo)
        else:
            print("Please enter a valid vhoice ")
    elif choice == 3:
        exit()


main()








