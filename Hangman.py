#To make game of hangman
def HangManOyy(question,answer):
    import random
    from os import system
    ra=answer.upper() if answer.upper()==answer else answer.lower()
    take=""
    turn=3#The tries
    while(turn>=0):
        fail=0
        print('\nYour question is : ',question)
        for char in ra:
            if (char in take.upper()) or (char in take.lower()) or (char in take):
                print("\t",char,end="")
            else:
                print("\t_",end=" ")
                fail+=1
        guess = input("\n\n\tEnter the code: ")
        system('cls')
        if(guess=="done" and fail==0):
            return 3
        take += guess
        if(fail==0):
            print("\n You completed",)
            return 3
        if guess in ra:
            print("\nGood Going !!")
            continue
        print("\nThe chances are : ",turn-1)
        if(turn-1==0):
            print("You surrendered but !! Nice played")
            print("Also the letters were :-------",ra,"--------")
            break
        turn-=1
    print("Nice played you have found all the words ",)