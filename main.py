import module.menu as menu
import sys
from art import *
from termcolor import colored

# Lance le programme :) !

print(colored(text2art("Slender"), 'cyan'))
print(colored('Created by Morgannito \n\n'.center(120), 'red'))
if sys.version_info.major < 3:
    print("python version may be > major 3")
    exit(0)

menu.main()
