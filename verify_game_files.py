import os
import sys
import shutil
from data.helpers import *
import time
        
def verify_game_files():
    file = open("data/values.txt")
    for save in file:
        save = save.strip("\n")
        if os.path.exists("data/save_values/" + save + ".txt") == False:
            print("GAME FILES CORRUPTED")
            print("RESETTING GAME DATA")
            reset_data()
            sys.exit()

        save_file = open("data/save_values/" + save + ".txt", "r")
        value = save_file.read()
        if value == '0' or value == '1':
            continue
        else:
            print("GAME FILES TAMPERED WITH")
            print("OPERATION 22.4 STARTED")
            shutil.rmtree("data", ignore_errors=True)
            return 1