print("Welcome to guess number game")
print("in this game you should guess the numbers in range(1, 1000)")
import random
point = 0
x = range(0, 1001)
while True: 

    listOfNUmbers = []


    numbers = int(input("How many numbers do you want to guess? "))


    for i in range(numbers):
        listOfNUmbers.append(random.choice(x))


    listOfGuessNum = input("Enter your numbers with space between each numbers : ").split()
    listOfcorrectGuess = []

    for x in range(len(listOfGuessNum)):
        listOfGuessNum[x] = int(listOfGuessNum[x])

    for i in listOfGuessNum:
        if i in listOfNUmbers:

            listOfcorrectGuess.append(i)
            point += 1

    print("================================")
    print("Numbers that you guessed : ", listOfNUmbers)
    print("================================")
    print("Random numbers : ", listOfGuessNum)
    print("================================")
    print("Numbers that you guessed correctly : ", listOfcorrectGuess)
    print("================================")
    print("your score is : ",point)
    print("================================")
    if input("do you want to continue ? (y,n) :") == "n":
        break
    
