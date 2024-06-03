from data.helpers import *
import time

def robux_pretext():
    print_blank_wall()
    print("------------------------------------------------------------------------------------------------------------------------------------")
    gprint("Hello, and welcome to free robux generator. We will give u ur 10milion free robx aftr you enter your computer username and password")
    print("\n")
    gprint("USer: ", end="")
    input()
    gprint("Password: ", end="")
    input()

    print("\n")
    processing("Getting you your robux", 100, True, 0.02, 0.4, '.')

    write_value("data/save_values/first_time.txt", "1")