import random
comp = random.randint(0,10)
nationalteam={
    "4":"Brazil",
    "5":"Germany",
    "6":"England",
    "7":"Argentina",
    "8":"Netherlands",
    "9":"Italy",
    "10":"France",
    "11":"Portugal",
    "12":"Spain",
    "13":"Mexico",
    "14":"Croatia",
    "15":"San Marino"
}
clubteam={
    "16":"Manchester City",
    "17":"Manchester United",
    "18":"Chelsea",
    "19":"Bayern Munich",
    "20":"PSG",
    "21":"Liverpool",
    "22":"Inter Milan",
    "23":"AC Milan",
    "24":"Tottenham Hotspur",
    "25":"Napoli",
    "26":"Real Madrid",
    "27":"FC Barcelona",
    "28":"Borrusia Dortmund",
    "29":"Juventus",
    "30":"Leeds United"
}
def Userfirst_striking():
    chances=5
    count=0
    count1=0
    for i in range(chances):
        usernum=int(input("Enter a number from 1 to 10: "))
        compnum=random.randint(0,10)
        print("The Computer entered: ",compnum)
        if(compnum==usernum+1 or compnum==usernum-1 or (compnum==10 and usernum==0) or (compnum==0 and usernum==10)):
            print("GOAL !!")
            count=count+1
        else:
            print("MISS !!")
    print(userteam,"(You)have Scored ",count," number of goals. Now it's your time for Goalkeeping")
    for i in range(chances):
        usernum=int(input("Enter a number from 1 to 10: "))
        compnum=random.randint(0,10)
        print("The Computer entered: ",compnum)
        if(compnum==usernum+1 or compnum==usernum-1 or (compnum==10 and usernum==0) or (compnum==0 and usernum==10)):
            print("You have conceded !!")
            count1=count1+1
        else:
            print("SAVED !!")
    print(compnat,"(The Computer) has Scored ",count1," number of goals.")
    if (count>count1):
        print("Congratulations. You've won with a scoreline of ",userteam,"(",count,"-",count1,")",compnat)
    elif(count<count1):
        print("Sorry. You've lost with a scoreline of ",compnat,"(",count1,"-",count,")",userteam)
    else:
        print("The Game ended in a draw. Scoreline is ",userteam,"(",count,"-",count1,")",compnat)
        
def Userfirst_GK():
    chances=5
    count=0
    count1=0
    for i in range(chances):
        usernum=int(input("Enter a number from 1 to 10: "))
        compnum=random.randint(0,10)
        print("The Computer entered: ",compnum)
        if(compnum==usernum+1 or compnum==usernum-1 or (compnum==10 and usernum==0) or (compnum==0 and usernum==10)):
            print("You have Conceded !!")
            count1=count1+1
        else:
            print("SAVED !!")
    print("The Computer Scored ",count1," number of goals. Now it's your time for Striking")
    for i in range(chances):
        usernum=int(input("Enter a number from 1 to 10: "))
        compnum=random.randint(0,10)
        print("The Computer entered: ",compnum)
        if(compnum==usernum+1 or compnum==usernum-1 or (compnum==10 and usernum==0) or (compnum==0 and usernum==10)):
            print("GOAL !!")
            count=count+1
        else:
            print("MISS !!")
    print("You have Scored ",count," number of goals.")
    if (count>count1):
        print("Congratulations. You've won with a scoreline of ",userteam,"(",count,"-",count1,")",compnat)
    elif(count<count1):
        print("Sorry. You've lost with a scorline of ",compnat,"(",count1,"-",count,")",userteam)
    else:
        print("The Game ended in a draw. Scoreline is ",userteam,"(",count,"-",count1,")",compnat)

def compFirst_Striking():
    chances=5
    count=0
    count1=0
    for i in range(chances):
        usernum=int(input("Enter a number from 1 to 10: "))
        compnum=random.randint(0,10)
        print("The Computer entered: ",compnum)
        if(compnum==usernum+1 or compnum==usernum-1 or (compnum==10 and usernum==0) or (compnum==0 and usernum==10)):
            print("You have Conceded !!")
            count1=count1+1
        else:
            print("SAVED !!")
    print("The Computer Scored ",count1," number of goals. Now it's your time for Striking")
    for i in range(chances):
        usernum=int(input("Enter a number from 1 to 10: "))
        compnum=random.randint(0,10)
        print("The Computer entered: ",compnum)
        if(compnum==usernum+1 or compnum==usernum-1 or (compnum==10 and usernum==0) or (compnum==0 and usernum==10)):
            print("GOAL !!")
            count=count+1
        else:
            print("MISS !!")
    print("You have Scored ",count," number of goals.")
    if (count>count1):
        print("Congratulations. You've won with a scoreline of ",userteam,"(",count,"-",count1,")",compnat)
    elif(count<count1):
        print("Sorry. You've lost with a scorline of ",compnat,"(",count1,"-",count,")",userteam)
    else:
        print("The Game ended in a draw. Scoreline is ",userteam,"(",count,"-",count1,")",compnat)

def compFirst_GK():
    chances=5
    count=0
    count1=0
    for i in range(chances):
        usernum=int(input("Enter a number from 1 to 10: "))
        compnum=random.randint(0,10)
        print("The Computer entered: ",compnum)
        if(compnum==usernum+1 or compnum==usernum-1 or (compnum==10 and usernum==0) or (compnum==0 and usernum==10)):
            print("GOAL !!")
            count=count+1
        else:
            print("MISS !!")
    print("You have Scored ",count," number of goals. Now it's your time for Goalkeeping")
    for i in range(chances):
        usernum=int(input("Enter a number from 1 to 10: "))
        compnum=random.randint(0,10)
        print("The Computer entered: ",compnum)
        if(compnum==usernum+1 or compnum==usernum-1 or (compnum==10 and usernum==0) or (compnum==0 and usernum==10)):
            print("You have conceded !!")
            count1=count1+1
        else:
            print("SAVED !!")
    print("The Computer has Scored ",count1," number of goals.")
    if (count>count1):
        print("Congratulations. You've won with a scoreline of ",userteam,"(",count,"-",count1,")",compnat)
    elif(count<count1):
        print("Sorry. You've lost with a scorline of ",compnat,"(",count1,"-",count,")",userteam)
    else:
        print("The Game ended in a draw. Scoreline is ",userteam,"(",count,"-",count1,")",compnat)
    
    
print("THIS IS HAND SOCCER")
intclub=int(input("Press 4 for International Soccer or 5 for Club Soccer: "))
if(intclub==4):
    userteam=input("Enter your National Team: ")
    compnat=random.choice(list(nationalteam.values()))
    print("The Computer's National Team is: ",compnat)
    print("It is: ",userteam," VS ",compnat)
elif(intclub==5):
    userteam=input("Enter your Club Team: ")
    compnat=random.choice(list(clubteam.values()))
    print("The Computer's Club Team is: ",compnat)
    print("It is: ",userteam," VS ",compnat)
usertoss = int(input("It's Toss Time. Press 0 for Even and 1 for Odd: "))
user = int(input("Enter a number from 0 to 10 : "))
print("The Computer entered:",comp)
add = comp+user
if(usertoss==0 and add%2==0):
    print("Its Even. You've won the toss. Press 2 for Striking and 3 for Goalkeeping")
    choice = int(input())
elif(usertoss==1 and add%2!=0):
    print("Its Odd. You've won the toss. Press 2 for Striking and 3 for Goalkeeping")
    choice = int(input())
else:
    compchoice = random.randint(2,3)
    if(compchoice==2):
        print("You've lost the Toss. The Computer chooses Striking")
    elif(compchoice==3):
        print("You've lost the Toss. The Computer chooses Goalkeeping")
    
if(usertoss==0 and add%2==0 and choice==2):
    Userfirst_striking()
    
elif(usertoss==0 and add%2==0 and choice==3):
    Userfirst_GK()
    
elif(usertoss==1 and add%2!=0 and choice==2):
    Userfirst_striking()
    
elif(usertoss==1 and add%2!=0 and choice==3):
    Userfirst_GK()
    
elif(compchoice==2):
    compFirst_Striking()
    
elif(compchoice==3):
    compFirst_GK()
    