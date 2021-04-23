import re,os,datetime
#Creating function for file functioning and fetching the hours,minutes,date stored in file for processing
def funct(filename):
    global hour,minutes,date
    count=1
    file=open(filename)
    for line in file:
        Date_hour_time=re.findall('\s(\d+-\d+-\d+|\d+)',line)
    while (Date_hour_time[1]!=hour or Date_hour_time[2]!=minutes or Date_hour_time[0]!=date):
        date=(str(datetime.datetime.now()).split(' ')[0])[::-1]
        time=str(datetime.datetime.now()).split(' ')[1]
        hour,minutes=list(map(int,time.split(':')[0:2]))
    file.close()  
#Created empty list
Date_hour_time=[] 
#Initialized with zeroes
hour,minutes,date=[0,0,0]
name=input('\t\tEnter the name : ')
filename=input('\nEnter the filename : ')
user=input('\n Which task is set for reminder ?: ')
print('\nPlease enter the date in (day-month-year) format ')
Date=input('\nDate -> ')
print('\nEnter at what time you want to display the task ? : ')
try:
    hour_a=int(input('\nHour -> '))
    minute_a=int(input('\nMinutes -> '))
except:
    print('\nInvalid')
#Checking if file is exist in path or not if exist then check for overwrite
if  not os.path.exists(filename):
    print('\t\n \t---------------------------New file is created-------------------')
    file=open(filename,'w')
    file.write('Text -> '+str(user)+' Date -> '+str(Date)+' Hour -> '+str(hour_a)+' Minutes -> '+str(minute_a))
    file.close()
    funct(filename)
    print('\n\t\t--------------------------------------------------------')
    print('\nHello',name,'your task is : ',user)
#else part means file is present 
else:
    print('\tThe file is existed so , ')
    check=input('\nDo you want to overrite the file [y/n] : ')
    while True:
        if check=='y':
            funct(filename)
        else:
            again_check=input('Confirm it [y/n] : ')
            if again_check==n:
                break
            else: continue
        print('\n\t\t--------------------------------------------------------')
    print('\nHello',name,'your task is : ',user)
#End of sticky notes goes on creating multiple files and add task to it .