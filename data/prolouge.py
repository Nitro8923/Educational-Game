from data.helpers import *

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
    if choice("Send bitcoin? y/n") == 'y':
        gprint("Wallet ID: ", end="")
        input()
        
        gprint()
        gprint("Your wallet doesn't have enough bitcoin.")
    
    write_value("data/save_values/started_decryption.txt", "1")

def hard_mode():
    print()
    print()

    gprint("You have a pirated decryption software from a russian website")
    choice("Do you use it? y/n: ")

def started_decryption():
    gprint("")