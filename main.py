thing = 0

def make():
    global thing
    maketxt = input(":")
    if maketxt.lower() == "make":
       thing = thing + 1
       print(thing)
       make()
    else:
       print(thing)
       make()

make()