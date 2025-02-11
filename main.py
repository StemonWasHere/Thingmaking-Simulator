from os import system, name

thing = 0

#clear func
def clr():
# windows
    if name == 'nt':
        _ = system('cls')
# macos and linux
    else:
         _ = system('clear')

#printing main dashboard
def dash():
    global thing
    print("-x-x-x-x-x-x{Thingmaking Factory}x-x-x-x-x-x-")
    print("Things make:", thing)
    print("-x-x-x-x-x-x{Thingmaking Factory}x-x-x-x-x-x-")

#make func
def make():
    global thing
    maketxt = input(":")
    if maketxt.lower() == "make":
       thing = thing + 1
       clr()
       dash()
       make()
    else:
       clr()
       dash()
       make()

make()