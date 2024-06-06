from data.helpers import *
from data import prolouge
from data import robux_menu
from data import decryption_levels
from data import decryption_levels
from data import epilogue
from verify_game_files import *
import time



def main():    
    verify_game_files()



    if read_value("data/save_values/first_time.txt") == '0':
        robux_menu.robux_pretext()
    
    if read_value("data/save_values/started_decryption.txt") == '0':
        prolouge.ransomware_startup()

    if read_value("data/save_values/hard_mode.txt") == "0" and read_value("data/save_values/files_decrypted.txt") == "0":
        prolouge.hard_mode()
    
    if read_value("data/save_values/files_decrypted.txt") == "0":
        decryption_levels.manual_calculator()
    
    epilogue.files_decrypted()


main()

