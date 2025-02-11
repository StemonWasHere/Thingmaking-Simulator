#this file is experimental changes, development, and overall unstable 
#it is not recommended to play on this version, please play the main.py instead

from os import system, name

thing = 0
incle = 1 #(thing inclement)
btm = 10 #big thing maker price

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
    print("-x-x-x-x-x-x{Thingmaking Factory}x-x-x-x-x-x-")
    print(txt)
    print("type 'shop' to access the shop")
    print("Things made:", thing)
    print("Things made per make:", incle)
    print("-x-x-x-x-x-x{Thingmaking Factory}x-x-x-x-x-x-")
    
#cheat
thing = 9
    
#shop
def shop():
    global thing
    global btm
    global incle
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
            dash("type 'make' to make thing")
            make()
    else:
            print("unknown command")
            shop()
 
            
#make func
def make():
    global thing
    global incle
    makein = input("make: ")
    if makein.lower() == "make":
       thing = thing + incle
       clr()
       dash("type 'make' to make thing")
       make()
    elif makein.lower() == "shop":
        shop()
    else:
       clr()
       dash("unknown command, type 'make' to make thing")
       make()

dash("type 'make' to make thing")
make()