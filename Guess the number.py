import random
#To guess by U
def GuessByU(upperLimit = 10, level = 1):
    print(f'LEVEL {level}')
    print(f'The Number To Guess is In Between 1 & {upperLimit}')
    toGuess = random.randint(1, upperLimit)
    yourGuess = 0
    while yourGuess != toGuess:
        yourGuess = int(input('Enter Your Guess = '))
        if yourGuess < toGuess:
            print('The Number Is Higher')
        elif yourGuess > toGuess:
            print('The Number Is Lower')
    print(f'Congratulations!!!\nYou Guessed It Correct!!\nThe Number Is {toGuess}')
    nextLevel = input("Next Level [Y] or Exit [N]").lower()
    if nextLevel == 'n':
        return
    else:
        upperLimit += 10
        level += 1
        GuessByU(upperLimit, level)

#To guess by computer
def GuessByComp(upperLimit = 10, level = 1):
    if upperLimit <= 1000:
        lowerLimit = 1
        feedback = ''
        print(f'Think Of A Number Between Including {lowerLimit} & {upperLimit}')
        while feedback != 'c':
            if lowerLimit != upperLimit:
                guess = random.randint(lowerLimit, upperLimit)
            else:
                guess = lowerLimit
            feedback = input(f'Is {guess} Is Higher [H] Or Lower [L] Or Correct [C]?? ').lower()
            if feedback == 'h':
                upperLimit = guess - 1
            elif feedback == 'l':
                lowerLimit = guess + 1
        print(f'The Computer Has Guessed The Number Correctly!!\nThe Number Is {guess}')
        nextLevel = input("Next Level [Y] or Exit [N]").lower()
        if nextLevel == 'n':
            return
        else:
            upperLimit += 10
            level += 1
            GuessByComp(upperLimit, level)

#__main__
#To print the Menu & get the choice
while True:
    print("MENU")
    print("1: Play Guess The Number Where You Will Guess The Number")
    print("2: Play Guess The Number Where The Computer Will Guess The Number")
    print("0: Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        GuessByU()
    elif choice == 2:
        GuessByComp()
    elif choice == 0:
        print('Exiting The Game!!')
        break
    else:
        print(f'{choice} Is Not A Mode\nPlease Choose Again')