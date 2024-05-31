from data.helpers import *
from data.decryption_levels import *

def ransomware_startup():
    # introduce ransomware
    print_blank_wall()
    print("------------------------------------------------------")
    gprint("YOUR FILES HAVE BEEN HACKED!")
    gprint("WE HAVE THE DECRYPTION SOFTWARE TO DECRYPT YOUR FILES!")
    gprint("TO DECRYPT YOUR FILES PLEASE SEND US 250 BITCOIN TO THIS ADDRESS:")
    gprint("amgndkh_udjjgndmvbzkv782og78a9t6eo9t8")

    # send bitcoin (doesn't impact game)
    print()
    if choice("Send bitcoin? y/n: ") == 'y':
        gprint("Wallet ID: ", end="")
        input()
        
        print()
        gprint("Your wallet doesn't have enough bitcoin.")
    
    write_value("data/save_values/started_decryption.txt", "1")

def hard_mode():
    print()
    print()
    gprint("You have a pirated decryption software from a russian website")
    if choice("Do you use it? (There is no going back) y/n: ") == 'y':
        write_value("data/save_values/hard_mode", "1")
        processing(message="Extracting", num_chars=20, random_delay=True, delay_min=0.01, delay_max=0.05, loading_char='.')
        processing(message="Running", num_chars=20, random_delay=True, delay_min=0.01, delay_max=0.05, loading_char='.')
        gprint("It messed up your computer")
        gprint("Your work is going to be a lot harder now...")

def started_decryption():
    hard_mode()
    gprint("You just got off the phone with your brother")
    gprint("He just sent over a .zip file containing an legit decryptor")
    gprint("He also sent over a key to use the decryptor:")
    gprint("legit_key pbssha_kegen552 36857")
    gprint("You extract it")

    print()
    print()
    processing(message="Extracting", num_chars=20, random_delay=True, delay_min=0.01, delay_max=0.05, loading_char='.')
    choice("Open the decryptor (type open): ", {'open'})
    open_decryptor()
    