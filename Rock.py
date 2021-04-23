#To implement the rock ,paper and scissors
#Take the user input 
import random
from time import sleep
from os import system
score=0
name=input('To begin with game enter your name : ')
while True:
    system('cls')
    lst=['Paper','Rock','Scissor']
    user_values=''
    computer=random.choice(lst)
    print('\n\n\t\t\t-------------Rock: r , Paper: p , Scissors: s ,Quit: q-------------------')
    print('Score :',score)
    user=input('\n\n\tEnter the choice from the rock,paper and scissors : ')
    if user=='q':
        print('Thankyou for playing ')
        break
    elif(user=='r' or user=='p' or user=='s'):
        if(user=='r'):
            user_values='Rock'
            if computer=='Scissor':
                print('\t\t\t',user_values,'vs',computer,'\n')
                print(f'\n\t{name} is winner\n\n\t\t\t{name} your item was :',user_values,'\n\n\t\t\tComputer item was: ',computer)
                score+=1
            elif user_values==computer:
                print('\t\t\t',user_values,'vs',computer,'\n')
                print(f'\n\n\t\t\t!!!Draw!!!\n\n\t\t\t{name} your item was :',user_values,'\n\n\t\t\tComputer item was: ',computer)
            else:
                print('\n\n\t\t\t',user_values,'vs',computer,'\n','\n\tComputer is winner')
                print(f'\n\n\t\t\t{name} your item was :',user_values,'\n\n\t\t\tComputer item was: ',computer)
                score-=1
        elif(user=='s'):
            user_values='Scissor'
            if computer=='Paper':
                print('\t\t\t',user_values,'vs',computer,'\n')
                print(f'\n\t{name} is winner\n\n\t\t\t{name} your item was :',user_values,'\n\n\t\t\tComputer item was: ',computer)
                score+=1
            elif user_values==computer:
                print('\t\t\t',user_values,'vs',computer,'\n')
                print(f'\n\n\t\t\t!!!Draw!!!\n\n\t\t\t{name} your item was :',user_values,'\n\n\t\t\tComputer item was: ',computer)
            else:
                print('\n\n\t\t\t',user_values,'vs',computer,'\n','\nComputer is winner')
                print(f'\n\n\t\t\t{name} your item was :',user_values,'\n\n\t\t\tComputer item was: ',computer)
                score-=1
        else:
            user_values='Paper'
            if computer=='Rock':
                print('\t\t\t',user_values,'vs',computer,'\n')
                print(f'\n\t{name} is winner\n\n\t\t\t{name} your item was :',user_values,'\n\n\t\t\tComputer item was: ',computer)
                score+=1
            elif user_values==computer:
                print('\t\t\t',user_values,'vs',computer,'\n')
                print(f'\n\n\t\t\t!!!Draw!!!\n\n\t\t\t{name} your item was :',user_values,'\n\n\t\t\tComputer item was: ',computer)
            else:
                print('\n\n\t\t\t',user_values,'vs',computer,'\n','\nComputer is winner')
                print(f'\n\n\t\t\t{name} your item was :',user_values,'\n\n\t\t\tComputer item was: ',computer)
                score-=1
    else:
        print('Invalid Input!!')
        sleep(3)
        continue
    sleep(8)

    

