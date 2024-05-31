from helpers import *

def open_decryptor():
    print_blank_wall()
    print("------------------------------------------------------")
    gprint("Hello and welcome to the legit (TM) decryptor!", speed=0.05)
    choice(message="Please enter your premium key: ", accepted_choices={"legit_key pbssha_kegen552 36857"}, reminder=True, reminder_message="Remember the key is: legit_key pbssha_kegen552 36857")
    gprint("Proceeding to analyse your computer", speed=0.05)
    processing(message="Analysing", num_chars=20, random_delay=True, delay_min=0.01, delay_max=10, loading_char='.')
    gprint("After careful analysis, we needs 5 decryption layers to fully decrypt your computer")
    gprint("We will bring encrypted samples from ")