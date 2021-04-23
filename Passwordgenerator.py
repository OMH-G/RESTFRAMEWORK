import string,random,os
#Take the input from the user
if __name__ == "__main__":
    StartingName="Database of Passwords"
    val=StartingName.split(" ")
    lval=list()
    which_app=input("For which app do you want password : ")
    if not os.path.exists("Passwords.txt"):
        file=open("Passwords.txt","w+")
        file.write("Database Collection \n")
    file = open("Passwords.txt")
    for i in file:
        val=i.split(" ")
        lval.extend(val)
    if(which_app not in lval):
        password_length=int(input("Enter the length of the password : "))
        s,take,o_string=list(),list(),""
        s.extend((list(string.ascii_lowercase),list(string.ascii_uppercase),list(string.digits),list(string.punctuation)))
        take=list()
        for i in s:
            take.extend(i)
        random.shuffle(take)
        for i in range(password_length):
            o_string+=random.choice(take)
        #Method without append 
            # if not os.path.exists("Passwords.txt"):
            #     with open("Passwords.txtDatabase.txt","w") as P:
            #         P.write("Starting to Database of passwords\n")
        with open("Passwords.txt","a") as P:
            P.write(which_app+" = "+o_string+"\n")
        print("Ok Your password generated is : ",o_string)
    else:
        print("--Sorry you can't Overwrite the name which was created earlier.--")
        
