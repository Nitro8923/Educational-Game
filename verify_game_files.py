import os
import sys
import shutil
from data.helpers import *
import time
import sys

sys.dont_write_bytecode = True


def verify_game_file():
    print("GAME FILES TAMPERED WITH")
    print("OPERATION 22.4 STARTED")
    # shutil.rmtree("data", ignore_errors=True)
    sys.exit()

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
            verify_game_file()
    good = True
    counter = 0
    if read_value("data/save_values/decryption_layer1.txt") == "1":
        counter += 1
    if read_value("data/save_values/decryption_layer2.txt") == "1":
        counter += 1
        if not counter == 2:
            good = False
    if read_value("data/save_values/decryption_layer3.txt") == "1":
        counter += 1
        if not counter == 3:
            good = False
    if read_value("data/save_values/decryption_layer4.txt") == "1":
        counter += 1
        if not counter == 4:
            good = False
    if read_value("data/save_values/decryption_layer5.txt") == "1":
        counter += 1
        if not counter == 5:
            good = False
    counter = 0
    if read_value("data/save_values/hard_decryption_layer1.txt") == "1":
        counter += 1
        if not counter == 1:
            good = False
    if read_value("data/save_values/hard_decryption_layer2.txt") == "1":
        counter += 1
        if not counter == 2:
            good = False
    if read_value("data/save_values/hard_decryption_layer3.txt") == "1":
        counter += 1
        if not counter == 3:
            good = False
    if read_value("data/save_values/hard_decryption_layer4.txt") == "1":
        counter += 1
        if not counter == 4:
            good = False
    if read_value("data/save_values/hard_decryption_layer5.txt") == "1":
        counter += 1
        if not counter == 5:
            good = False
    
    if good == False:
        verify_game_file()