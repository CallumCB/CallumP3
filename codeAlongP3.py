import random
myList = []
def mainProgram():
    while True:
        try:
            print("Choose one of the following options. type a number only.")
            choice = input("""1. Add to list,
2. Add a bunch of numbers
3. Return the value at an index position
4. Print list.
5. Pick random number from list
6. Search in list
7. End
    """)
            if choice == "1":
                addToList()
            elif choice=="2":
                addLot()
            elif choice=="3":
                indexValues()
            elif choice=="4":
                print(myList)
            elif choice=="5":
                randomSearch()
            elif choice=="6":
                linearSearch()
            else:
                break
        except:
            print("There was an error.")
def addToList():
    newItem=input("Please type an integer.  ")
    myList.append(int(newItem))
    print(myList)

def addLot():
    print("About to add lot's"   )
    numToAdd=input("How many integers do you want to add?   ")
    numRange=input("How high do you want the numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is done.")

def indexValues():
    indexPos = input("What position do you want to see?  ")
    print(myList[int(indexPos)])

def randomSearch():
    print("Here is a random number from your list.")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're going to search the list")
    searchItem=input("What are you looking for?  ")
    numAm=0
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            numAm = munAm + 1
            print("Your number is at index {}".format(x))
    print("The number {}".format(searchItem))
    print("appeared {} times".format(numAm))
if __name__ == "__main__":
    mainProgram()
