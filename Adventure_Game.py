import time

# This is an adventure game where the player is kidnapped and wakes up at a shipping yard with the aim of finding out why he/she is there.

player = raw_input("What is your name, fellow explorer? ")

print "Okay, %s, let's start the game!" % player
time.sleep(0.500)

# Code that starts the game. Basic narration of settings. Uses time.sleep() so that user can read stuff easily.
def start(player):
    print "You wake up and look around you. There's nothing but shipping containers. As you stand up, you feel giddy. You touch your head and feel a bump on it. 'Where am I?' you think to yourself."
    time.sleep(6)
    print "You get your bearings. You frantically look around and yell for help in hopes that someone finds you."
    print "No one. There's no one here."
    print "It's just you."
    print "You search your pockets. Left one -- empty. Right one -- wait, there's something there. You reach into your pocket and pull out a note."
    time.sleep(10)
    print "090455-SW-13"
    print "You look around and see that all the shipping containers have such numbers. It must be the number of a shipping container right?"
    time.sleep(6)
    print "You don't know why you're here. But there's this note in your pocket - your only clue. This is the only thing you can follow."
    time.sleep(6.5)
    # use the same template for other levels to make sure that the inputs are only acceptable terms.
    game = False
    while game == False:
        ans = raw_input("Do you want to proceed to the container?")
        ans = ans.lower()
        if ans == "yes" or ans == "y" or ans == "yeah" or ans == "yepp" or ans == "yep":
            print "Onward!"
            game = True
            time.sleep(2)
            level_1(game)
        elif ans == "no" or ans == "nope" or ans == "n":
            print "Okay then, seems like you're just gonna die here. Good luck!"
            game = True
            end()
        else:
            print "Sorry, please enter either yes or no"
            game = False

# First level of the game. Player finds the container and is faced with the choice of either entering the container, jumping over it, or not entering it (in which case they die).
def level_1(game):
    print "You have located the container 090455-SW-13."
    time.sleep(1)
    print "You look around you but there's no one you can see. This container is the only thing that could possibly tell you why you're here."
    time.sleep(4)
    game = False
    while game == False:
        choice1 = raw_input("The container is unlocked but the door isn't open. Do you want to open the door? Enter 'yes' or no' ")
        choice1 = choice1.lower()
        if choice1 == "yes" or choice1 == "yepp" or choice1 == "yep" or choice1 == "y":
            print "You decided to open the door to the container."
            game = True
            time.sleep(1)
            level_2_alt1(game)
        elif choice1 == "no" or choice1 == "nope" or choice1 == "n":
            print "Okay then..."
            game = True
            time.sleep(1)
            level_2_alt2(game)
        else:
            print "Please enter a valid answer."
            game = False

#Ends the game if the player dies in the process.
def end():
    print "Thanks for playing!"
    time.sleep(0.5)
    exit()

# Shorter alternative to the game - AKA how I want the game to proceed.
def level_2_alt1(game):
    print "You have entered the container. \n In front of you lies a chest, the key to which is placed in front of the chest."
    time.sleep(3)
    game = False
    while game == False:
        choice3 = raw_input("Do you want to head to the chest and open it?")
        choice3 = choice3.lower()
        if choice3 == "yes" or choice3 == "yepp" or choice3 == "yep" or choice3 == "y":
            print "You've decided to open the chest."
            game = True
            time.sleep(1)
            level_3(game)


# If the player doesn't climb the container, this happens. If they get inside the container, it proceeds to level_2_alt1(game).
def level_2_alt2(game):
    print "You chose not to open the door. That's probably because you're scared of someone being inside... or something being inside. However, you can jump into the container from the top. \n There's a ladder to the right of the container. You can climb it and reach the inside of the container. \n Afterall, you need to know why you're here."
    game = False
    while game == False:
        choice2 = raw_input("Do you want to climb the container?")
        choice2 = choice2.lower()
        if choice2 == "yes" or choice2 == "yepp" or choice2 == "yep" or choice2 == "y":
            print "You decided to climb the container and jump into it."
            game = True
            time.sleep(1)
            level_2_alt1(game)
        elif choice2 == "no" or choice2 == "nope" or choice2 == "n":
            print "You chose to do nothing. You stood there too long and died because you couldn't find your way out."
            game = True
            time.sleep(2)
            end()
        else:
            print "Type a valid answer please"
            game = False

# The player has a choice of picking up the note and key, and going to the bank. If they choose to do so, they'll be knocked out and will wake up in an alley. Else, they can choose to stay at the shipping yard in which case they'll die.
def level_3(game):
    print "You open the chest and find another note accompanied with a weird-looking key."
    time.sleep(2)
    print "On the note it's written: \n \n 4422-6050-1122-22222 \n go to HDFC at the city center and find out why you're here \n \n a bank account number with a weird message... could this day get any better?"
    time.sleep(4)
    print "You start thinking about what to do. You don't even know where the bank is. \n \n You close the chest and see the inscription at the top. \n \n HDFC \n \n could the person who made this have made the clue any more obvious? Like, really, just giving the name?"
    time.sleep(7)
    print "You're conflicted."
    time.sleep(2)
    print "Something's odd..."
    game = False
    while game == False:
        choice4 = raw_input("Should you go there or not?")
        if choice4 == "yes" or choice4 == "yepp" or choice4 == "yep" or choice4 == "y":
            print "You've chosen to go to the bank. As you walk out of the container you see a man headed for you with a baseball bat. \n \n you try to duck but you fail. You're knocked out"
            time.sleep(4)
            print "."
            time.sleep(0.5)
            print "."
            time.sleep(0.5)
            print "."
            time.sleep(0.5)
            print "."
            time.sleep(0.5)
            game = True
            level_4(game)
        elif choice4 == "no" or choice4 == "nope" or choice4 == "n":
            print "You've chosen not to go to the bank \n \n But why are you here? \n Is there any way for you to get out of here? \n You run out of the container frantically searching for ways out."
            time.sleep(7)
            print "You look for hours"
            time.sleep(1)
            print "And hours"
            time.sleep(1)
            print "And hours."
            time.sleep(0.5)
            print "Nothing"
            print "There's no way out."
            print "You're doomed."
            time.sleep(2)
            print "You're trapped. There's no way out of this for you. No foreseeable way you're leaving this shipping yard. There's no one here. \n All the containers are empty \n No one will EVER find you."
            time.sleep(5)
            print "You're destined to die here...."
            time.sleep(2)
            game = True
            end()
        else:
            print "Type a valid answer please"
            game = False

# you're at a desolate alleyway. You can make your way to the bank or you can walk away...
def level_4(game):
    print "You wake up. The pain pierces through your head. You stand up and dust yourself."
    time.sleep(2)
    print "The note..."
    time.sleep(1)
    print "You take a look at the note once again: "
    time.sleep(1)
    print "422-6050-1122-22222 \n go there and find out why you're here."
    game = False
    while game == False:
        confirm = raw_input("Do you want to go to the bank? Enter either 'yes' or 'no'")
        # Add two more if statements - one for "no" and one for an invalid answer
        confirm = confirm.lower()
        if confirm.lower() == "yes" or confirm.lower() == "y" or confirm.lower() == "yeah" or confirm.lower() == "yepp" or confirm.lower() == "yep":
            time.sleep(0.5)
            print "You tightly hold the note in your hand, and move forward to the bank."
            time.sleep(1.5)
            print "You look around you just to make sure you're not being followed."
            time.sleep(1.5)
            print "The large sign overhead reads HDFC. You're here."
            time.sleep(1.5)
            print "You head to the reception and provide this bank account number."
            time.sleep(1.5)
            print "The receptionist searches for the number on his database; he quickly glances at the well-built security guard at the back."
            time.sleep(4)
            print "You're scared now. You don't know what to do."
            time.sleep(1)
            print "Is this account associated to someone dangerous?"
            time.sleep(1)
            print "Did I mess up? - you ask yourself"
            time.sleep(1)
            print "You need to take a decision now."
            game = True
            level_4_decision()
        elif confirm == "no" or confirm == "nope" or confirm == "n":
            print "You look around and there's still no one... thankfully."
            time.sleep(1)
            print "This whole thing, it's a little odd, isn't it?"
            time.sleep(1)
            print "You were in a seemingly abandoned shipping yard. \n You woke up with a note in your pocket. \n Then you find a chest with a key and yet another note."
            time.sleep(5)
            print "It's good you took this choice."
            time.sleep(1)
            print ". \n . \n ."
            print "You just saved yourself."
            game = True
            end()
        else:
            print "Please enter a valid answer"
            game = False

# This is the code for the lvl_4_decision input that's above. CHECK THIS cuz there could be many errors in the last parts using WHILE loops.
def level_4_decision():
    # Insert WHILE loop below; everything else should be nested in the WHILE loop.
    game = False
    while game == False:
        lvl_4_decision = raw_input("Should you run out of the bank, or should you wait? Type either 'run' or 'wait' ")
        lvl_4_decision = lvl_4_decision.lower()
        # if the decision is to wait then lead to the locker room.
        if lvl_4_decision == "run" or lvl_4_decision == "run out of the bank" or lvl_4_decision == "r":
            time.sleep(0.5)
            print "As the security guard approaches you, you dart out of the door."
            time.sleep(2)
            print "What have I done?! - you think to yourself."
            time.sleep(2)
            print "As you're running out, you turn behind to see if you're still being followed."
            time.sleep(3)
            print "You're not... \n \n or so you think. \n \n"
            time.sleep(1)
            print "It's not the bank security guard"
            time.sleep(1)
            print "He's wearing a black leather jacket - the expensive kind. You can see a gun pop out of his left pocket."
            time.sleep(2)
            print "You don't have a gun. \n But the city center is a crowded place."
            xyz = True
            while xyz = True:
                choice5 = raw_input("Do you want to run into the crowd or do you want to run into an isolated alley? Type in either 'crowd' or 'alley'")
                choice5 = choice5.lower()
                print "Good choice."
                time.sleep(1)
                print "You keep running and running and running."
                time.sleep(1)
                print "You look behind and he's gone."
                time.sleep(1)
                print "You don't't know who he was."
                time.sleep(1)
                print "You don't know what he's capable of."
                time.sleep(2)
                print "You don't know why he even followed you."
                time.sleep(1)
                print "But you do know that you just saved yourself."
                print ". /n . /n . /n"
                time.sleep(1)
                print "You're going home now."
                print "Away from all this."
                time.sleep(2)
                game = True
                xyz = False
                end()
        elif lvl_4_decision == "wait" or lvl_4_decision == "wait here" or lvl_4_decision == "w":
            print "The guard approaches you and asks you to follow him"
            time.sleep(2)
            print "You don't know where he's taking you, but you follow him anyway."
            time.sleep(3)
            print "As you follow him, you notice that there's less crowd behind you now. \n \n He's taking you to an isolated location in the bank."
            time.sleep(5)
            print "You enter the Premium locker room"
            time.sleep(1)
            print "You're asked for the number on the note again."
            time.sleep(1)
            print "Only moments later, another guard escorts you to the locker that's seemingly yours... \n \n you don't even know whose locker it is..."
            time.sleep(5)
            game = True
            lvl_5(game)
        else:
            print "Please enter a valid answer"
            game = False

def lvl_5(game):
    print "You're left alone in the private room with your locker. \n It's locked."
    time.sleep(2)
    print "You look down at the key, and decide to open the locker. You're here already so you might as well see what's inside."
    time.sleep(3)
    print "You open the locker and see a brown envelope inside - it probably has a few documents, or photos to explain why the hell you're here. It's sealed"
    time.sleep(4)
    game = False
    while game == False:
        choice6 = raw_input("Do you want to open the envelope and examine the documents? Type either 'yes' or 'no' ")
        choice6 = choice6.lower()
        if choice6 == "yes" or choice6 == "y" or choice6 == "yepp" or choice6 == "yep":
            print "As you pull out the documents, you see pictures of yourself."
            time.sleep(2)
            print "Someone was spying on you"
            time.sleep(1)
            print "But why??"
            time.sleep(1)
            print "You rummage the documents - there's bank statements, credit card bills, calendar printouts for the past year, and an FBI document... with your name on it."
            time.sleep(5)
            print "You shouldn't have gotten involved in this"
            time.sleep(2)
            print "How much worse can this get?"
            time.sleep(2)
            print "You think of asking someone. Maybe the security guard or the bank employees could help you out?"
            lvl_6(game)
            game = True
        elif choice6 == "no" or choice6 == "n" or choice6 == "nope":
            print "This is too unpredictable"
            time.sleep(1)
            print "You never know what could happen... a bank account number that leads to a locker with a sealed envelope in it? I think you'd rather not get yourself involved in this..."
            time.sleep(5)
            print "It's best you leave now"
            game = True
            lvl_7(game)
        else:
            print "Please enter a valid answer"
            game = False

def lvl_6(game):
    choice7 = raw_input("Do you want to ask the bank staff or security about the documents, or do you want to leave? Enter either 'ask' or 'leave'")
    choice7 = choice7.lower()
    if choice7 == "ask them" or choice7 == "ask" or choice7 == "ask bank staff" or choice7 == "ask security":
        print "You call them asking them what these documents are."
        time.sleep(2)
        print "They reply saying that they're not authorized to look at customers' personal locker items but you persuade them to do so."
        time.sleep(4)
        print "That might've been a mistake..."
        time.sleep(1)
        print "As the bank staffer examines the document, her eyebrow curls in an almost eerie manner. \n You feel the situation deteriorate but there's nothing you can do"
        time.sleep(5)
        print "It's over..."
        print "The staffer asked you to wait at the corner of the room. There's no escape from here"
        time.sleep(5)
        print "You can't get out."
        time.sleep(2)
        print "In a matter of minutes, the police arrive, and without saying a word, they handcuff you. Then they tell you your rights..."
        time.sleep(5)
        print "There's no way to know what you've done."
        time.sleep(4)
        print "As you walk out of the bank, you see a familiar face smirking at you... it's Tom... your own brother..."
        time.sleep(5)
        print "What happened... why it happened... maybe you'd never know... but if you did happen to know, it'd be at a court trial months later..."
        time.sleep(5)
        print "Rightn ow, you're doomed."
        game = True
        end()
    elif choice7 == "leave" or choice7 == "leave the bank" or choice7 == "leave bank":
        lvl_7(game)
        game = True
    else:
        print "Please enter a valid answer"
        game = False

def lvl_7(game):
    print "You walk out of the bank, your face towards the floor."
    time.sleep(2)
    print "Seems like that was the right choice..."
    time.sleep(1)
    print "No one's following you... \n No one's eyeing you... \n Everything seems normal"
    time.sleep(2)
    print "Maybe you knew what was really in the locker, or maybe you didn't... but you do know that you're now safe."
    time.sleep(3)
    print "It's better that you not know what were in the documents... it's for your own good."
    time.sleep(2)
    print "I know what was in it... \n \n Something incriminating... something that'd lead to your doom..."
    time.sleep(3)
    print "Sometimes it's better not to know some things, isn't it?"
    end()

start(player)
