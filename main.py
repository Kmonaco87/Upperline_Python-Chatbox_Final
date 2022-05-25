def signIn ():

  global count

  print(" ")
  print("Welcome to the Student Hub to create your assignment list for Python, Please sign into your account ")
  print(" ")
  print("Remember you only have three attempts to correctly sign-in. After three attemps, you will be locked out. ")
  print(" ")
  sec1 = input("Q1. What is your favorite color? ")
  sec2 = input("Q2. What is your favorite month?")

  if sec1 == "purple" and sec2 == "february":
    studentHub()
  else: 
    print(" ")
    print("Sorry, that was an invalid entry. You have " + str(2 -count) + " attemps remaining before being locked out of the account." )
    count += 1

    if count <3:
      signIn()
    else: 
      print(" ")
      print("SECURITY ALERT:  You have been locked out of this app! Try again in 15 minutes.")


def studentHub():

  global choice

  while choice != "c" or choice != "C":
    print("")
    print("Student Python Assignment Task ")
    print("a. Add a Python Task to your list")
    print("b. Remove a completed item from your list")
    print("c. Exit app")
    choice = input("What would you like toa do? [a|b|c] ")
    print(" ")
    
    if choice.upper() == "A":
      numTimes = int(input("How many items would you like to add to the list?  "))
      if numTimes >=1 and numTimes<= 100000:
        for x in range (numTimes):
          task = input("What task are you adding?  ")
          to_do_List.append(task)
        print(" ")
        print("This is what you still have to do:")
        for every_item in range(len(to_do_List)):
          print("%s. %s" % (every_item + 1,to_do_List[every_item] ))
      elif numTimes <1:
        print("Sorry, you must enter a number greater than '0'. Let's start again!")

    elif choice.upper() == "B":
      print("")
      for i in range(len(to_do_List)):
        print("%s: %s" % (i+1, to_do_List[i]))
      print(" ")
      ask = input("Do you wish to remove all items on your list? (y/n) ")

      if ask.upper() == "Y":

          to_do_List.clear()
          print("All items on your to do list have been erased.")
      
      elif ask.capitalize() == "N":

          print(" ")
          rid = int(input("How many items do you wish to remove? (must be less than total number of items in the list) "))
          print(" ")

          if rid == len(to_do_List):
              print("Sorry, your number must be less than the total number of items on your list.")
              print(" ")
              
          elif rid < len(to_do_List):
              print(" ")
              for x in range (0,rid):
                  remove_index = int(input("Which number item do you want to complete? " ))
                  to_do_List.remove(to_do_List[remove_index - 1])
                  print(" ")
                  print("This is what you still have to do: ")
                  for i in range(len(to_do_List)):
                      print("%s: %s" % (i+1, to_do_List[i]))
          else:
              print(" ")
              print("That is an incorrect input. Try again.")
              signIn()

    elif choice.upper() == "C":
        print("You have chosen to end this session.")
        print(" ")
        print("This is what you still have to do:")
        for every_item in range(len(to_do_List)):
          print("%s. %s" % (every_item + 1,to_do_List[every_item] ))
        if len(to_do_List) == 0:
            print("No tasks registered")
        print(" ")
        print("Thanks for using the app!  Don't forget to tell your friends about us!")
        
        break

  


#list to store tasks
to_do_List = [ ]

#lockcounter
count = 0

#while loop control variable
choice = "empty"

#begin game
signIn()
