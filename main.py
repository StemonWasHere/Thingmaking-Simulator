from os import system, name
import random

thing = 0
incle = 1 #(thing inclement)
btm = 10 #big thing maker price
crit = 20 #crit rate
crincle = incle*3 #crit rate inclement

#clear func
def clr():
# windows
    if name == 'nt':
        _ = system('cls')
# macos and linux
    else:
         _ = system('clear')

#printing main dashboard
def dash(txt):
    global thing
    global incle
    global crit
    global crincle
    print("-x-x-x-x-x-x{Thingmaking Factory}x-x-x-x-x-x-")
    print(txt)
    print("type 'make' to make thing")
    print("type 'shop' to access the shop")
    print("things made:", thing)
    print("things made per make:", incle)
    print("crit rate: 1 in ",crit)
    print("things made per critical make: ", crincle)
    print("-x-x-x-x-x-x{Thingmaking Factory}x-x-x-x-x-x-")

#shop
def shop():
    global thing
    global btm
    global incle
    global crit
    global crincle
    clr()
    print("-x-x-x-x-x-x{Shop}x-x-x-x-x-x-")
    print("Things made:", thing)
    print("type 'buy[tool number] to buy tool with said number")
    print("[1] big thingmaker")
    print("make even more things (from", incle, "to", incle+1,"to be exact")
    print("price:", btm)
    print("type 'exit' to exit shop")
    print("-x-x-x-x-x-x{Shop}x-x-x-x-x-x-")
    shopin = input("shop: ")
    if shopin.lower() == "buy1":
        if thing >= btm:
            print("big thingmaker bought")
            thing = thing-btm
            btm = int(btm*2.2)
            incle = incle+1
            shop()
        else:
            print("you're too poor, come back with more things")
            shop()
    elif shopin.lower() == "exit":
            dash("shop exited")
            make()
    else:
            print("unknown command")
            shop()


#make func
def make():
    global thing
    global incle
    global crit
    global crincle
    makein = input("make: ")
    if makein.lower() == "make":
       if random.randint(1, crit) == 1: #see if crit (1 in crit chances)
           thing = thing + crincle
           clr()
           dash(f"critical hit! you made {crincle} thing(s)")
       else:
           thing = thing + incle
           clr()
           dash(f"you made {incle} thing(s)")
       make()
    elif makein.lower() == "shop":
        shop()
    else:
       clr()
       dash("unknown command")
       make()

dash(":)")
make()