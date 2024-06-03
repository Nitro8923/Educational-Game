import time
import random
import os

def gprint(string="", speed=0.08, end="\n"):
    for character in string:
        print(character, end="", flush=True)
        time.sleep(speed)
    print(end, end="")
    time.sleep(1)

def print_blank_wall(size=100):
    for i in range(size):
        print()

def processing(message, num_chars=25, random_delay=False, delay_min=0.1, delay_max=0.1, loading_char='.'):
    print(message, end="", flush=True)
    
    for i in range(num_chars):
        print(loading_char, end="", flush=True)
        if random_delay == True:
            delay_time = random.uniform(delay_min, delay_max)
        else:
            delay_time = delay_min
        
        time.sleep(delay_time)
    print()

def choice(message="", accepted_choices={'y', 'n'}, use_gprint=False, reminder=False, reminder_message=""):
    while True:
        if use_gprint == True:
            gprint(message, end="")
        else:
            print(message, end="")
        answer = input()

        if answer in accepted_choices:
            return answer;
        elif reminder == True:
            print()
            if gprint == True:
                gprint(reminder_message)
            else:
                print(reminder_message)

def read_value(file):
    with open(file, "r") as file:
        return file.read()

def write_value(file, value):
    with open(file, "w") as file:
        file.write(value)

def reset_data():
    try:
        file = open("data/values.txt")
    except:
        print_blank_wall()
        print("-1 Reinstall")

    for save in file:
        save = save.strip("\n")
        save_file = open("data/save_values/" + save + ".txt", "w")
        save_file.write("0")
        save_file = ""
