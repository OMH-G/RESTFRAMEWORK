#Starting to build questions and answer app and storing in the database
import sqlite3
from os import system
import re
import random
import time
import Hangman
database=sqlite3.connect('questionandAnswer.sqlite')
cur=database.cursor()
cur.executescript('''
DROP TABLE IF EXISTS QnA;
CREATE TABLE QnA(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
Question TEXT,
Answer TEXT
);
''')
#Taking the input from the user to play the game or not 
user=input('Enter the name of the player : ')
#Extracting information from the file into the database of QnA
file=open('QuestionAndAnswer.txt',encoding='utf8')
score=0
tries=3
new_val=tries
Append_list=list()
def Badges(score):
    if(score>=20):
        print('\n____Your first badge___\n')
        patterns.first_badge()
        print('\n^^^^^^^^^^^^^^^\n')
    if(score>=30):
        print('\n____Your second badge___\n')
        patterns.second_badge()
        print('\n^^^^^^^^^^^^^^^\n')
    if(score>=50):
        print('\n____Your third badge___\n')
        patterns.third_badge()
        print('\n^^^^^^^^^^^^^^^\n')
    if(score>=70):
        system('cls')
        print(user,'You have completed last badge\n')
        print('\n____Your fourth badge___\n')
        patterns.last_badge()
        print('\n^^^^^^^^^^^^^^^\n')

if __name__ == "__main__":
    for line in file:
        if line.strip()=='':continue
        line=line.strip()
        qna_list=re.findall('\.(?P<name>\s[A-Z-a-z].*|.*)?(-|>|:)(?P<answer>\s.*|.*)',line)
        cur.execute('''INSERT OR IGNORE INTO QnA (question,answer) VALUES(?,?)
        ''',(qna_list[0][0],qna_list[0][2]))
    cur.execute('''SELECT * FROM QnA ''')
    Append_list=cur.fetchall()
    database.commit()
    value=''
    checker_list=list()
    while value!='q':
        system('cls')
        choice=random.choice(Append_list)
        if choice in checker_list:continue
        checker_list.append(choice)
        index_number=Append_list.index(choice)
        cur.execute('''SELECT Question,Answer FROM QnA where Question=? AND Answer=?''',(Append_list[index_number][1],Append_list[index_number][2]))
        question,answer=cur.fetchone()
        print('\n\n\t\tNow The Game Starts .....')
        time.sleep(2)
        test_score=Hangman.HangManOyy(question,answer.strip())
        try:
            score+=test_score
        except:
            print('You failed try again!!')
        time.sleep(1)
        options=input('\n\tFor options press \'o\' Otherwise press enter  :')
        if(options=='o'):
            value=input('\n\t\t\t Quit: q , Score:s , BADGES:b ,Continue:Press Enter -> ')
        system('cls')
        if(value=='s'):
            print('\t\t\t\nAtlast Your Score is : ',score)
        elif(value=='b'):
            if(score<10):print('\n You are not eligible for badge to get badge obtain score more than 10 ')
            if(score>=10):
                for i in range(5):
                    for j in range(5):
                        if(i==0 or j==0 or i==4 or j==4):
                            print('*',end=' ')
                        else:
                            print(' ',end=' ')  
                    print()
            if(score>=35):
                for i in range(1,6):
                    print(''*(4-i),'*'*i) 
            if(score>=50):
                for i in range(1,6):
                    print(' '*(4-i),'*'*i)
            if(score>=70):
                for i in range(6,0,-1):
                    for j in range(6):
                        if(j<i):
                            print(' ',end='')
                        else:
                            print('*',end=' ')          
        value=''
        time.sleep(5)
    print('\n\t\tThankyou For playing!!')
    # while tries>0:
    #     Answer=input('Enter the Answer : ').lower().strip()
    #     if(Answer=='exit'):
    #         break  
    #     elif(Answer!=answer.lower().strip()):
    #         print(f'\n\t\tAnd {user} your ...')
    #         time.sleep(2)
    #         print('\n\t\tAnswer is Wrong ! try it once more ')
    #         print('\n\t If you get bored then enter \'exit\'')
    #         score-=1
    #         if(score==-1):
    #             score=0
    #         if(tries==new_val-1):
    #             print('\n\tI think you want answer , so answer is :',Append_list[index_number][2])
    #         tries-=1
    #         print('\n\tTries: ',tries)
    #         print('\n\t\t Score : ',score)
                
    #     else:
    #         print(f'\n\t\tAnd {user} your ...')
    #         time.sleep(2)
    #         print('\n\t\tAnswer is correct !!!')
    #         score+=1
    #         break
    # time.sleep(1)
    # system('cls')
    # print('Tries are over hence the game is over')
    # print(f'\t\t\nHi {user} your score is : ',score,'enjoy it !!!!!')
    # print(f'\n\nCongratulation!,{user} now complete entire question ')


