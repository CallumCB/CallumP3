import random
myList = []
unique_list=[]

def mainProgram():
    while True:
        try:
            print("Choose one of the following options. type a number only.")
            choice = input("""1. Add to list,
2. Add a bunch of numbers
3. Return the value at an index position
4. Sort list
5. Pick random number from list
6. Search in list
7. Print changed lists
8. Recursive binary search
9. Interative binary search
10. End
""")
            if choice == "1":
                addToList()
            elif choice=="2":
                addLot()
            elif choice=="3":
                indexValues()
            elif choice=="4":
                sortList(myList)
            elif choice=="5":
                randomSearch()
            elif choice=="6":
                linearSearch()
            elif choice=="7":
                printLists()
            elif choice=="8":
                binSearch= input("What number are you looking for?  ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice=="9":
                binSearch= input("What number are you looking for?  ")
                result = interativeBinarySearch(unique_list, int(binSearch))
                if result != -1:
                    print("Your number is at index position {}".format(result))
                else:
                    print("Your number isn't here")
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
def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe=input("Want to see your new list?  Y/N  ")
    if showMe.lower() == 'y':
        print(unique_list)
def indexValues():
    indexPos = input("What position do you want to see?  ")
    print(myList[int(indexPos)])
def randomSearch():
    print("Here is a random number from your list.")
    print(myList[random.randint(0, len(myList)-1)])
def printLists():
    if len(unique_list)==0:
        print(myList)
    else:
        whichOne=input("Which list? Sorted or un-sorted?")
        if whichOne.lower()=="sorted":
            print(unique_list)
        else:
            print(myList)
def linearSearch():
    print("We're going to search the list")
    searchItem=input("What are you looking for?  ")
    numAm=0
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            numAm = numAm + 1
            print("Your number is at index {}".format(x))
    print("The number {}".format(searchItem))
    print("appeared {} times".format(numAm))
def recursiveBinarySearch(unique_list, low, high, x):
    if high>=low:
        mid=(high+low) // 2
        if unique_list[mid] == x:
            print("your number is at index position {}".format(mid))
            return mid
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid -1, x)
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("That number isn't in this list.") 
def interativeBinarySearch(unique_list, x):
    low=0
    high=len(unique_list)-1
    mid=0
    while low <= high:
        mid=(high + low) // 2
        if unique_list[mid] < x:
            low = mid + 1
        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    mainProgram()
