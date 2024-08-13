import sys
from pyfiglet import Figlet
from random import choice
figlet = Figlet()

try:
    if len(sys.argv)<2:
        figlet.setFont(font=(choice(figlet.getFonts())))
        print(figlet.renderText(input("Input: "))) 
    elif len(sys.argv)>2 and (sys.argv[1]=="-f" or "--font") and sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(input("Input: ")))
    else:
        sys.exit("Invalid Usage")
except(IndexError):
    sys.exit("Invalid Usage")



