import random

#create functions that perform those actions above
myList = []
def mainProgram():
    while True:
        try:
            print("Choose one of the following options. type a number only.")
            choice = input("""1. Add to list,
    2. Return the value at an index position
    3. Pick random number from list
    4. End
    """)
            if choice == "1":
                addToList()
            elif choice == "2":
                indexValues()
            elif choice=="3":
                randomSearch()
            else:
                break
        except:
            print("There was an error.")
        
def addToList():
    newItem=input("Please type an integer.  ")
    myList.append(int(newItem))
    print(myList)
def indexValues():
    indexPos = input("What position do you want to see?  ")
    print(myList[int(indexPos)])
def randomSearch():
    print("Here is a random number from your list.")
    print(myList[random.randint(0, len(myList)-1)])
if __name__ == "__main__":
    mainProgram()
