from data.helpers import *
from random import randint
import sys

sys.dont_write_bytecode = True

def open_decryptor():
    print_blank_wall()
    print("--------------------------------------------------------------------------------------------")
    gprint("Hello and welcome to the legit (TM) decryptor!", speed=0.05)
    choice(message="Please enter your premium key: ", accepted_choices={"legit_key pbssha_keygen552 36857"}, reminder=True, reminder_message="Remember the key is: legit_key pbssha_keygen552 36857")
    print()
    print()
    gprint("Proceeding to analyse your computer", speed=0.05)
    processing(message="Analysing", num_chars=100, random_delay=True, delay_min=0.01, delay_max=0.1, loading_char='.')
    print()
    print()
    gprint("After careful analysis, we need 5 decryption layers to fully decrypt your computer")

    if read_value("data/save_values/hard_mode.txt") == "1":
        gprint("This computer is harder to decrypt")

    gprint("But don't worry, our automatic calculator will take care of all that")
    gprint("We will bring encrypted samples from your computer and decrypt them for you")
    
    print()
    processing(message="Decrypting", num_chars=5, random_delay=True, delay_min=0.9, delay_max=1, loading_char='.')
    time.sleep(1)
    gprint("ERROR: Automatic calculator not found.")
    
    print()
    processing(message="Downloading Automatic calculator", num_chars=5, random_delay=True, delay_min=0.9, delay_max=1, loading_char='.')
    time.sleep(1)
    gprint("Download failed. Starting manual calculator software.")
    time.sleep(2)
    manual_calculator()

def manual_calculator():
    print_blank_wall()
    print("---------------------------------------------------------------------------------------------------")
    gprint("Hello and welcome to the manual calculation software!")
    gprint("We will give you equations to solve")
    gprint("You will need to enter the combination of all of the answers to decrypt a layer")
    gprint("You will need to decrypt 5 layers to fully decrypt your computer!")
    input("Press enter to start decrypting")
    time.sleep(2)
    while(True):
        if read_value("data/save_values/hard_mode.txt") == "0":
            if read_value("data/save_values/decryption_layer1.txt") == "0":
                level1()
            elif read_value("data/save_values/decryption_layer2.txt") == "0":
                level2()
            elif read_value("data/save_values/decryption_layer3.txt") == "0":
                level3()
            elif read_value("data/save_values/decryption_layer4.txt") == "0":
                level4()
            elif read_value("data/save_values/decryption_layer5.txt") == "0":
                level5()
            else:
                break
        elif read_value("data/save_values/hard_mode.txt") == "1":
            if read_value("data/save_values/hard_decryption_layer1.txt") == "0":
                hard_level1()
            elif read_value("data/save_values/hard_decryption_layer2.txt") == "0":
                hard_level2()
            elif read_value("data/save_values/hard_decryption_layer3.txt") == "0":
                hard_level3()
            elif read_value("data/save_values/hard_decryption_layer4.txt") == "0":
                hard_level4()
            elif read_value("data/save_values/hard_decryption_layer5.txt") == "0":
                hard_level5()
            else:
                break
    
    files_decrypted()
        
    
def files_decrypted():
    pass


def level1():
    print()
    print()
    gprint("First layer")
    gprint("3 questions")
    ans = 0
    for i in range(3):
        x = randint(0, 10)
        y = randint(0, 10)
        gprint("Q" + str(i + 1) + " " + str(x) + " + " + str(y))
        input("Press enter for next question")
        print()
        print()
        ans += x + y
    gprint("The code for the first decryption layer is all the answers added together")
    choice(message="Enter code: ", accepted_choices={str(ans)}, use_gprint=True,reminder=True, reminder_message="Breaking decryption layer....................... \nCode is wrong!")
    print()
    print()
    processing("Breaking decryption layer", num_chars=100)
    gprint("Decryption layer broken")
    gprint("1 Decryption Layer Completed, 4 to go.")
    write_value("data/save_values/decryption_layer1.txt", "1")

def level2():
    print()
    print()
    gprint("Second layer")
    gprint("5 questions")
    ans = 0
    for i in range(5):
        x = randint(1, 10)
        y = randint(1, 10)
        z = randint(1, 20)
        if randint(0, 1) == 0:
            gprint("Q" + str(i + 1) + " " + str(x) + " + " + str(y) + " + " + str(z))
            ans += x + y + z
        else:
            gprint("Q" + str(i + 1) + " " + str(max(x, y)) + " - " + str(min(x, y)) + " + " + str(z))
            ans += max(x, y) - min(x, y) + z

        input("Press enter for next question")
        print()
        print()
        
    gprint("The code for the second decryption layer is all the answers added together")
    choice("Enter code: ", accepted_choices={str(ans)}, reminder=True, reminder_message="Breaking decryption layer....................... \nCode is wrong!", use_gprint=True)
    print()
    print()
    processing("Breaking decryption layer", num_chars=100)
    gprint("Decryption layer broken")
    gprint("2 Decryption Layers Completed, 3 more to go.")
    write_value("data/save_values/decryption_layer2.txt", "1")

def level3():
    print()
    print()
    gprint("Third layer")
    gprint("5 questions")
    ans = 1000
    for i in range(5):
        x = randint(1, 10)
        y = randint(1, 10)
        gprint("Q" + str(i + 1) + " " + str(x) + " * " + str(y))
        ans -= (x * y)

        input("Press enter for next question")
        print()
        print()
        
    gprint("The code for the third decryption layer is all the answers subtracted from 1000")
    choice("Enter code: ", accepted_choices={str(ans)}, reminder=True, reminder_message="Breaking decryption layer....................... \nCode is wrong!", use_gprint=True)
    print()
    print()
    processing("Breaking decryption layer", num_chars=100)
    gprint("Decryption layer broken")
    gprint("3 Decryption Layers Completed, 2 more to go.")
    write_value("data/save_values/decryption_layer3.txt", "1")

def level4():
    print()
    print()
    gprint("Fourth layer")
    gprint("10 questions")
    ans = 0
    for i in range(10):
        x = randint(1, 10)
        y = randint(1, 200)
        gprint("Q" + str(i + 1) + " " + str(x * y) + " / " + str(x))
        ans += y

        input("Press enter for next question")
        print()
        print()
        
    gprint("The code for the fourth decryption layer is all the answers added together")
    choice("Enter code: ", accepted_choices={str(ans)}, reminder=True, reminder_message="Breaking decryption layer....................... \nCode is wrong!", use_gprint=True)
    print()
    print()
    processing("Breaking decryption layer", num_chars=100)
    gprint("Decryption layer broken")
    gprint("4 Decryption Layers Completed, 1 more to go.")
    write_value("data/save_values/decryption_layer4.txt", "1")

def level5():
    print()
    print()
    gprint("Fifth layer")
    gprint("10 questions")
    ans = 0
    for i in range(10):
        x = randint(1, 1000)
        y = randint(1, 1000)
        gprint("Q" + str(i + 1) + " " + str(x) + " + " + str(y))
        ans += x + y

        input("Press enter for next question")
        print()
        print()
    
    gprint("The code for the fifth decryption layer is all the answers added together")
    choice("Enter code: ", accepted_choices={str(ans)}, reminder=True, reminder_message="Breaking decryption layer....................... \nCode is wrong!", use_gprint=True)
    print()
    print()
    processing("Breaking decryption layer", num_chars=100)
    gprint("Decryption layer broken")
    write_value("data/save_values/decryption_layer5.txt", "1")

def hard_level1():
    print()
    print()
    gprint("First layer")
    gprint("10 questions")
    ans = 0
    for i in range(10):
        x = randint(0, 10000)
        y = randint(0, 10000)
        gprint("Q" + str(i + 1) + " " + str(x) + " + " + str(y))
        input("Press enter for next question")
        print()
        print()
        ans += x + y
    gprint("The code for the first decryption layer is all the answers added together")
    choice("Enter code: ", accepted_choices={str(ans)}, reminder=True, reminder_message="Breaking decryption layer....................... \nCode is wrong!", use_gprint=True)
    print()
    print()
    processing("Breaking decryption layer", num_chars=100)
    gprint("Decryption layer broken")
    gprint("1 Decryption Layers Completed, 4 more to go.")
    write_value("data/save_values/hard_decryption_layer1.txt", "1")

def hard_level2():
    print()
    print()
    gprint("Second layer")
    gprint("10 questions")
    ans = 0
    for i in range(10):
        x = randint(1, 1000)
        y = randint(1, 1000)
        z = randint(1, 100000)
        if randint(0, 1) == 0:
            gprint("Q" + str(i + 1) + " " + str(x) + " + " + str(y) + " + ", + z)
            ans += x + y + z
        else:
            gprint("Q" + str(i + 1) + " " + str(max(x, y)) + " - " + str(min(x, y)) + " + " + z)
            ans += max(x, y) - min(x, y) + z

        input("Press enter for next question")
        print()
        print()
        
    gprint("The code for the second decryption layer is all the answers added together")
    choice("Enter code: ", accepted_choices={str(ans)}, reminder=True, reminder_message="Breaking decryption layer....................... \nCode is wrong!", use_gprint=True)
    print()
    print()
    processing("Breaking decryption layer", num_chars=100)
    gprint("Decryption layer broken")
    gprint("2 Decryption Layers Completed, 3 more to go.")
    write_value("data/save_values/hard_decryption_layer2.txt", "1")

def hard_level3():
    print()
    print()
    gprint("Third layer")
    gprint("10 questions")
    ans = 1000000
    for i in range(10):
        x = randint(1, 100)
        y = randint(1, 100)
        gprint("Q" + str(i + 1) + " " + str(x) + " * " + str(y))
        ans -= (x * y)

        input("Press enter for next question")
        print()
        print()
        
    gprint("The code for the third decryption layer is all the answers subtracted from 1000000")
    choice("Enter code: ", accepted_choices={str(ans)}, reminder=True, reminder_message="Breaking decryption layer....................... \nCode is wrong!", use_gprint=True)
    print()
    print()
    processing("Breaking decryption layer", num_chars=100)
    gprint("Decryption layer broken")
    gprint("3 Decryption Layers Completed, 2 more to go.")
    write_value("data/save_values/hard_decryption_layer3.txt", "1")

def hard_level4():
    print()
    print()
    gprint("Fourth layer")
    gprint("20 questions")
    ans = 0
    for i in range(20):
        x = randint(1, 100)
        y = randint(1, 2000)
        gprint("Q" + str(i + 1) + " " + str(x * y) + " / " + str(y))
        ans += x

        input("Press enter for next question")
        print()
        print()
        
    gprint("The code for the fourth decryption layer is all the answers added together")
    choice("Enter code: ", accepted_choices={str(ans)}, reminder=True, reminder_message="Breaking decryption layer....................... \nCode is wrong!", use_gprint=True)
    print()
    print()
    processing("Breaking decryption layer", num_chars=100)
    gprint("Decryption layer broken")
    gprint("4 Decryption Layers Completed, 1 more to go.")
    write_value("data/save_values/hard_decryption_layer4.txt", "1")

def hard_level5():
    print()
    print()
    gprint("Fifth layer")
    gprint("25 questions")
    ans = 0
    for i in range(25):
        x = randint(1, 100000)
        y = randint(1, 100000)
        z = randint(1, 10000000)
        gprint("Q" + str(i + 1) + " " + str(x) + " + " + str(y) + str(z))
        ans += x + y + z

        input("Press enter for next question")
        print()
        print()
    
    gprint("The code for the fifth decryption layer is all the answers added together")
    choice("Enter code: ", accepted_choices={str(ans)}, reminder=True, reminder_message="Breaking decryption layer....................... \nCode is wrong!", use_gprint=True)
    print()
    print()
    processing("Breaking decryption layer", num_chars=100)
    gprint("Decryption layer broken")
    write_value("data/save_values/hard_decryption_layer5.txt", "1")
    