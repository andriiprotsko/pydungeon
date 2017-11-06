from sys import exit

#variables

beast = True
dragon = True
sword = False

#rooms

#room01

def room01():
    print("You are in a big room with massive walls and mud everywhere.")
    print("It's really dark, but you can see three doors.")
    print("They lead east, north and west. What do you do?")

    choice = input("> ");

    if "west" in choice:
        room02()
    elif "north" in choice:
        room04()
    elif "east" in choice:
        gameover("""You decided to go to east.
You walked about few minutes, when you see a solid wall before you.
You decided to go back, but there was another wall behind you.
Somewhat, you have trapped youself. Without water and food, you
will die some days later. So stupid...""")
    else:
        room01()

#room02

def room02():
    print("This room has a really low ceiling, so you have crawl to walk forward.")
    print("At his room you see the same three doors leading to west, east and north.")
    print("When you are looking on west door you can see a bright light. Maybe it is exit?..")
    print("From the north you you can smell a really bad scents.")
    print("Doors to the east leads to the first room, where you came from.")
    print("What do you do?")

    choice = input("> ");

    if "west" in choice:
        gameover("""So you follow the door with bright light.
You open the door and light gets brighter and brighter, until you can't see anything.
You decided to go forward, but suddenly, you can no longer feel the floor under your
feet and, as you fall in a pit of white light. No one knows where
the light came from. You thought you flight will never ends, but you fall... How pathetic""")
    elif "north" in choice:
        room03()
    elif "east" in choice:
        room01()
    else:
        room02()

#room03

def room03():

    global beast
    global sword

    if beast:
        print("At the moment you walked into the room, you understand where the smell came from.")
        print("The floor is covered with ugly slime.")
        print("Suddenly you hear a powerfull growl and a huge beast appears in front of you.")
        print("You see a door on the east, flaming torch on the ground nearby,")
        print("a skeleton, holding a sword and a hole on the far side of the room.")
        print("The passage to the south leads to the previous room.")
        print("What do you do?")

        choice = input("> ");

        if "east" in choice:
            gameover("""You decided to run towards the east passage, but the beast leaps
in front of you. You don't have the time to do anything,
because the beast opens its jaws and rips of your head... Looks disguisted""")
        elif "torch" in choice:
            print("""You take the flaming torch and wave it in front of the
beast. It leaps back in fear, stumbles and falls in the
hole, disappearing from the room.""")
            beast = False
            room03()
        elif "sword" in choice:
            print("""You take the sword. For some reason it starts glowing with warm yellow light
and you feel invincible. Without knowing how, you
jump forward and kill the beast as a real hero, invincible hero of course.""")
            beast = False
            sword = True
            room03()
        elif "hole" in choice:
            gameover("""You jump in the dark. It wasn't
such a good idea, though. You start falling in the void,
never again hitting a floor. You die days later, still
falling. Fly birdie... fly...""")
        elif "south" in choice:
            room02()
        else:
            room03()

    else:
        print("The floor is covered with ugly slime.")
        print("You see a door on the east, flaming torch on the ground nearby,")
        print("a skeleton, holding a sword and a hole on the far side of the room.")
        print("The passage to the south leads to the previous room.")
        print("What do you do?")

        choice = input("> ")

        if "east" in choice:
            room04()
        elif "torch" in choice:
            print("""You take the flaming torch and wave it in the air.
You feel stupid and put it down.""")
            room03()
        elif "sword" in choice:
            print("""You take the sword.""")
            sword = True
            room03()
        elif "hole" in choice:
            gameover("""You jump in the dark. It wasn't
such a good idea, though. You start falling in the void,
never again hitting a floor. You die days later, still
falling. Fly birdie... fly...""")
        elif "south" in choice:
            room02()
        else:
            room03()

#room04

def room04():

    global dragon

    if dragon:

        print("The room is really huge, and for a good reasons. It is the home of a dragon.")

        if sword:
            print("""Suddenly your sword starts to glow with red light. Some unknown power urges you to
leap forward and hit the sword in the heart of the dragons.
It dies with horrible roar.""")
            dragon = False
            room04()
        else:
            print("There is a doors to the north, one to the east, one to the")
            print("south and one to the west. What do you do?")

        choice = input("> ")

        gameover("The dragon leaps in front of you and roasts you alive. Oops")

    else:

        print("There is a doors to the north, one to the east, one to the")
        print("south and one to the west. What do you do?")

        choice = input("> ")

        if "east" in choice:
            gameover("""You follow the east door until you end up in a little
room with a desk and a PC on it. A two guys are typing smth
on the PC and suddenly they noticed your presence. 'You should
not have found us, the coders of this game!' they says. 'Now
you have to die.' They types something on the python3, and you die.""")
        elif "south" in choice:
            room01()
        elif "west" in choice:
            room03()
        elif "north" in choice:
            gameover("""The door leads to the surface. You are free! The sun is shining and
you have won the game!""")
        else:
            room04()

#start

def start():
    room01()

#gameover

def gameover(s):

    global beast
    global dragon
    global sword

    beast = True
    dragon = True
    sword = False

    print (s)
    print("Do you want to play again? (y / n)")

    choice = ""
    while choice != "y" and choice != "n":
        choice = input("> ")
        if choice == "y":

            start()
        elif choice == "n":
            exit(0)

#main

start()