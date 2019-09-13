"""

Project #3 Choose your Own Adventure
@Authors: Kalani Daniel & Colby Grames
@Date: 9/6/2019
@Params: name


"""
 
from time import sleep
import sys


#our functions are built into each other, meaning based on each decison it will call a differnt function. 



def Intro(): 
  print()
  print()
  print()
  lines={"Welcome to the High School Adventure Story! " +name+", you are a senior at Citrus Valley High School. It's late in the school year and you have 'senioritis'. "}
  for line in lines:         
    for x in line:          #this block of code animates the text
      print(x,end='')       #this is repeated everytime there is a non                           question statement in the story 
      sys.stdout.flush()
      sleep(0.05)
    print('')
  print() 
  go_stay()

#asks user for their name
def getName(): 
  name= input('Hello user what is your name? ')
  print()
  return name

#main decision that changes the experience
def go_stay(): 
  ans=input(name+ ' would you like to go to school today?')
  print()
  if (ans=='yes' or ans=='yes ' or ans== 'yeah' or ans=='yeah ' or ans==' yes'or ans==' yes ' ):
    lines={"You decided to go to school. You quickly get dressed and get in your car and begin to drive to school"}
    for line in lines: 
      for x in line: 
        print(x,end='')
        sys.stdout.flush()
        sleep(0.05)
      print('')
    print()
    driveStyle()
  
  else: 
    lines={'You have decided to stay home today.'}
    for line in lines: 
      for x in line: 
        print(x,end='')
        sys.stdout.flush()
        sleep(0.05)
      print('')
    print()
    party_game()

#asking the user how he would like to drive
def driveStyle(): 
  ans=input('You notice that you are going to be late to school if you dont speed up. Do you want to speed up to try to get to school or just drive causally to school? ')
  print()
  if(ans=='speed'or ans=='speed 'or ans=='speed up'or ans=='speed up 'or ans=='speedup'):
    lines={'You chose to speed up to get to school.','', 
    'As you were picking up speed to get to school a cop pulled out and turns on his lights.'}
    for line in lines: 
      for x in line: 
        print(x,end='')
        sys.stdout.flush()
        sleep(0.05)
      print('')
    print()
    cops()
  else: 
    lines={'You drive to school normally but are late to school.'}
    for line in lines: 
      for x in line: 
        print(x,end='')
        sys.stdout.flush()
        sleep(0.05)
      print('')
    print()
    late()
    first4p()

#asks what the user wants to do when the cops start after them
def cops(): 
  ans=input('You can try to run from the cops or take the ticket like a man. What do you want to do?')
  print()
  if (ans=='run'or ans=='run 'or ans=='fuck 12' or ans=='run from the cops'):
    lines={'After some skillful driving and some smart decisons you get away and get to school on time.'}
    for line in lines: 
      for x in line: 
        print(x,end='')
        sys.stdout.flush()
        sleep(0.05)
      print('')
    print()
    first4p()
  else: 
    lines={'You let the cop pull you over for going 20 MPH over the speed limit. The cop gives you a ticket and you go on to school getting there slightly late. '}
    for line in lines: 
      for x in line: 
        print(x,end='')
        sys.stdout.flush()
        sleep(0.05)
      print('')
    print()
    late()

#only prints story element 
def first4p(): 
  lines={'Your first 4 periods are uneventful and boring as usual after which you go to lunch with your friend.'}
  for line in lines: 
    for x in line: 
      print(x,end='')
      sys.stdout.flush()
      sleep(0.05)
    print('')
  print()
  lunch()
  
#function called if you end up late to school
def late(): 
  lines={'You got to school after the first bell rang. The security guard sends you to detention for the rest of class.'}
  for line in lines: 
    for x in line: 
      print(x,end='')
      sys.stdout.flush()
      sleep(0.05)
    print('')
  print()
  first3p()

#same thing as first4p() but it accounts for the detention the user got for being late to school
def first3p(): 
  lines={'After you get out of detention you go to the rest of your morning classes as ususal.'}
  for line in lines: 
    for x in line: 
      print(x,end='')
      sys.stdout.flush()
      sleep(0.05)
    print('')
  print()
  print()
  
#asks user if they want to get into a fight
def lunch(): 
  ans=input('At lunch you and your friend go out into the quad and you turn away to talk to a class mate for a second. When you turn back to your freind he is in an aurgument with someone. You can tell they are about to fight. Do you break it up or back up your friend?')
  print()
  if (ans== 'break up' or ans=='break up 'or ans== 'break' or ans== 'yeah'or ans=='break it up' or ans=='break it up '):
    lines={'You step in and calm your friend and the person he is aurguing with and you all walk away.'}
    for line in lines: 
      for x in line: 
        print(x,end='')
        sys.stdout.flush()
        sleep(0.05)
      print('')
    print()
    goodEnding()
  else: 
    lines={'You chose to back up your friend and the others didnt back down either. The confrontation gets physical and a brawl breaks out. Security eventually rushes over and breaks it up taking you and your friends to the office.'}
    for line in lines: 
      for x in line: 
        print(x,end='')
        sys.stdout.flush()
        sleep(0.05)
      print('')
    print()
    badEnding()

def goodEnding(): 
  lines={'You finish your last two periods and go home and take a nap, capping off your normal day at highschool.'}
  for line in lines: 
    for x in line: 
      print(x,end='')
      sys.stdout.flush()
      sleep(0.05)
    print('')
  print()
  print('The End. ')
  print()
  replay()

def badEnding(): 
  lines={'After security takes you to the office your parents are called to come pick you up. They are furious with you and they ground you for the rest of the semester.'}
  for line in lines: 
    for x in line: 
      print(x,end='')
      sys.stdout.flush()
      sleep(0.05)
    print('')
  print()
  print('The End.')
  print()
  replay()

#Another choice leading to a party or to staying at home
def party_game():
  ans=input('With your day off you are deciding between planning a party or just playing video games for the rest of the day. Want do you want to do, game or party?')
  print()
  if (ans=='game ' or ans=='game'):
    lines={'As you just barely turn on your console, your friend texts you and invites you to a party.'}
    for line in lines: 
      for x in line: 
        print(x,end='')
        sys.stdout.flush()
        sleep(0.05)
      print('')
    print()
    newparty_game()
    
  elif (ans=='party ' or ans=='party'):
    print()
    party()
    
  else:
    lines={"That is not an option. Please try again."}
    for line in lines: 
      for x in line: 
        print(x,end='')
        sys.stdout.flush()
        sleep(0.05)
      print('')
    print()
    party_game()

#A choice giving a second chance to go to a different party
def newparty_game():
  ans=input('The choice is now yours, would you like to game or go to the party?')
  print()
  if (ans=='party ' or ans=='party' or ans=='go to party' or ans=='Party'):
    print()
    party()
  elif(ans=='game' or ans=='game ' or ans=='Game'):
    print()
    game()
  else:
    lines={'That is not an option. Please try again. '}
    for line in lines: 
      for x in line: 
        print(x,end='')
        sys.stdout.flush()
        sleep(0.05)
      print('')
    newparty_game()
    
#Story caused by choosing to game  
def game():
  ans=input("While sitting on the couch, you hear your parents car pull up. Would you like to hide or turn off console then run? ")
  if (ans=='hide ' or ans=='hide' or ans=='Hide'):
    print()
    lines={'As you are hiding, you cannot control your sneeze and your parents catch you.'}
    for line in lines: 
      for x in line: 
        print(x,end='')
        sys.stdout.flush()
        sleep(0.05)
      print('')
    getCaught()
  else:
    print()
    lines={'You are too slow and your parents catch you before you can hide.'}
    for line in lines: 
      for x in line: 
        print(x,end='')
        sys.stdout.flush()
        sleep(0.05)
      print('')
    getCaught()

#Story caused by choosing to party
def party():
  lines={"Within an hour, the party has exploded with other people who ditched."}
  for line in lines: 
    for x in line: 
      print(x,end='')
      sys.stdout.flush()
      sleep(0.05)
    print('')
  print()
  linez={'However, the cops are called and are banging on the front door.'}
  for line in linez: 
    for x in line: 
      print(x,end='')
      sys.stdout.flush()
      sleep(0.05)
  print('')
  cops2()
  
#A choice regarding the cops at the party
def cops2():
  print()
  ans=input("With the cops at the door, you have to make a snap decision. Do you hide or talk to the cops? ")
  print()
  if(ans=='hide' or ans=='hide '):
    lines={'The cop finds you and calls your parents.'}
    for line in lines: 
      for x in line: 
        print(x,end='')
        sys.stdout.flush()
        sleep(0.05)
      print('')
    getCaught()
  else:
    lines={"The cop doesn't listen to your rambling and instead calls your parents."}
    for line in lines: 
      for x in line: 
        print(x,end='')
        sys.stdout.flush()
        sleep(0.05)
      print('')
    getCaught()

#The terminator of the story; both paths lead to this end
def getCaught():
  lines={'As your parents catch you, you suffer a major grounding.'}
  for line in lines: 
    for x in line: 
      print(x,end='')
      sys.stdout.flush()
      sleep(0.05)
    print('')
  print()
  print('GAME OVER')
  print()
  replay()

#Gives user the option to replay game
def replay():
  ans=input('Would you like to play again? Please enter yes or no. ')
  if (ans=='yes ' or ans=='yes' or ans=='yeah' or ans== 'Yes' or ans== 'y'):
    Intro()
    print()
  elif(ans=='no' or ans=='no 'or ans=='No' or ans=='n'or ans=='nah'):
    lines={"Thank you for playing!"}
    for line in lines: 
      for x in line: 
        print(x,end='')
        sys.stdout.flush()
        sleep(0.05)
      print('')


#Actual code for game
name=getName()

Intro()



