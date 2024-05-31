from data.helpers import *
from data import prolouge
from data import robux_menu
from verify_game_files import *
import time


def main():    
    verify_game_files()

    if read_value("data/save_values/first_time.txt") == '0':
        robux_menu.robux_pretext()
    
    if read_value("data/save_values/started_decryption.txt") == '0':
        prolouge.ransomware_startup()

    if read_value("data/save_values/hard_mode.txt") == 0:
        prolouge.hard_mode()


main()

