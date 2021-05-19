import random
import time

state = 'start'


# ------------------------------------------- fNumOk -----------------------------------------------------------
def fNumOk(num):
    if (len(num) == len(set(num))) & (int(num) > 1000):
        return True
    else:
        return False


# ------------------------------------------ fInputOk ----------------------------------------------------------
def fInputOk(num):
    ret = False
    if num.isdigit():
        if len(num) == 4:
            if fNumOk(num):
                ret = True
            else:
                print("Number must not start by '0' and all digits must be unique!")
        else:
            if len(num) < 4:
                print("Number is too short!")
            else:
                print("Number is too long!")
    else:
        print('Input must be a number!')

    return ret


# ------------------------------------------- fGenerator -------------------------------------------------------
def fGenerator():
    i = 0
    while not fNumOk(str(i)):
        i = random.randint(1000, 9999)
    return i


# ------------------------------------------- MAIN LOOP --------------------------------------------------------
print("Hi there!")

while state != 'exit':
    if state == 'start':
        secNum = fGenerator()
        guesses = 0
        print(47 * '-')
        print("I've generated a random 4 digit number for you.")
        print("Let's play a bulls and cows game.")
        print(47 * '-')
        print("Enter a number:")
        startTime = time.time()
        state = 'game'

    while state == 'game':
        bulls = 0
        cows = 0
        print(47 * '-')
        tipNum = input('>>>')

        if fInputOk(tipNum):
            for i in range(0, 4):
                if tipNum[i] in str(secNum):
                    if tipNum[i] == str(secNum)[i]:
                        bulls += 1
                    else:
                        cows += 1

            guesses += 1
            plur = ["", "s"]
            print(str(bulls) + " bull" + plur[bulls != 1] + ", " + str(cows) + " cow" + plur[cows != 1])

        if bulls == 4:
            print("Congratulation, you win the game!")
            gmTime = time.localtime(time.time() - startTime)
            print("Attempts: " + str(guesses) + ", Time: " + str(gmTime.tm_min) + "m " + str(gmTime.tm_sec) + "s")

            while (tipNum != 'y') and (tipNum != 'n'):
                tipNum = input("Do you want play again? y/n  ")
            if tipNum == 'n':
                state = 'exit'
            elif tipNum == 'y':
                state = 'start'
