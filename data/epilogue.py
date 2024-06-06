import sys
from data.helpers import *

def files_decrypted():
    print_blank_wall()
    write_value("data/save_values/files_decrypted.txt", "1")
    gprint("Your files have been decrypted successfully!")
    gprint("All ransomeware has been removed!")
    gprint("You have beaten my game! GG!")

    print()
    print()
    gprint("You may be able to take revenge on the hacker in the sequel.")
    print()
    print()
    if choice("Reset game data? y/n: ") == 'y':
        reset_data()
