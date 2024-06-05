import sys
from data.helpers import *

sys.dont_write_bytecode = True
def files_decrypted():
    print_blank_wall()
    gprint("Your files have been decrypted successfully!")
    gprint("All ransaomware has been removed!")
    gprint("You have beaten my game! GG!")
    gprint("You may get to take revenge on the hacker in the sequel.")
    if choice("Reset game data? y/n: ") == 'y':
        reset_data()
