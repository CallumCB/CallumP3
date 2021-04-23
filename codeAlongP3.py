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

""" This functions asks what you want to add to the list, it then takes that and
turns it into an integer, it then adds it into the latest position of the list."""
def addToList():
    newItem=input("Please type an integer.  ")
    myList.append(int(newItem))
    print(myList)
    
""" This does the same as the add function, but it gives you a range that you can choose
how high you want the numbers to go, and then you can choose how many numbers you want to add
It then adds it to the end of the list"""
def addLot():
    print("About to add lot's"   )
    numToAdd=input("How many integers do you want to add?   ")
    numRange=input("How high do you want the numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is done.")
    
""" What this function does, is it takes the first number, sees if it is in the other list, if it is not, then it adds it to the list
It goes to the next number and does it again until there are no numbers left. At the end of adding the new numbers, there is a sort, wich will
sort all of the numbers from lowest to highest in the new list."""
def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe=input("Want to see your new list?  Y/N  ")
    if showMe.lower() == 'y':
        print(unique_list)
        
""" This asks if you want to see the list, if so, then it takes your input index position and finds it in the list, then prints it to you. """
def indexValues():
    indexPos = input("What position do you want to see?  ")
    print(myList[int(indexPos)])
    
""" This function generates a random number, and then finds that index position, then prints it """
def randomSearch():
    print("Here is a random number from your list.")
    print(myList[random.randint(0, len(myList)-1)])
    
""" This functions sees if there is anything in the new list, if you have not sorted it yet, there will be nothing there, so it will
print the original list, if there is stuff in it, it will ask wich one you want to see, then print that"""
def printLists():
    if len(unique_list)==0:
        print(myList)
    else:
        whichOne=input("Which list? sorted or un-sorted?")
        if whichOne.lower()=="sorted":
            print(unique_list)
        else:
            print(myList)
            
""" This asks if you what number you want to search for, it then looks at the first number
if it is the number, then it will add 1 to how many times it is inthe list, it will then
look at the next number and do the same untl the end of the list, then it prints how many times it was found."""
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
    
""" Recursive search looks in the middle of the list, if it your number, then it prints that,
if not, then it looks at the numbers next to it, if those arent it, then they go to another position and repeats until it finds the number."""
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
""" I don't really know how this one works, I am pretty sure that it sorts the list and removes all the numbers that
repeat, that is because it doesn't have a print or input, so I don't really know what it does. """
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

#The code that I want to add, is the ability to name lists, after you have added to them, I have no idea how to do this 

if __name__ == "__main__":
    mainProgram()
