import random as rnd

theMainList = []
yesAnswers = ['y','Y','Yes','yes','Yeah','yeah']

def main():
    print('Welcome to the TIL game')

    askForList = str(input('Do you wanna make a list ? '))
    if askForList in yesAnswers:
        print('Cool')
        itemNum = int(input('How much item inside the list? '))
        for i in range(itemNum):
            item = str(input('Write the item'))
            theMainList.append(item)
            i = i + 1
        
        print('You have almost finished')
        
        #Let's make the PC choice
        MachineChoice = rnd.choice(theMainList)
        theUserChoice = str(input('Please choice 1 item from that list you have writen! \n'))
        if theUserChoice == MachineChoice:
            print('You got it')

main()
