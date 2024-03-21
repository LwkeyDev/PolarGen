import os
from faker import Faker
from card_identifier.cardutils import validate_card
import sys
from card_identifier.cardutils import format_card
from card_identifier.card_type import identify_card_type
import time
from pystyle import Add, Center, Colors, Colorate, Write, System, Anime
import colorama 
import fade
from colorama import Fore


fake = Faker()
banner = '''
 



                               _ \         |                ___|              
                              |   |  _ \   |   _` |   __|  |       _ \  __ \  
                              ___/  (   |  |  (   |  |     |   |   __/  |   | 
                             _|    \___/  _| \__,_| _|    \____| \___| _|  _| 
                                                                                                               
                                           {Author: Lwkey}
                                           {Version: 2.4.9}
                        
                   [Disclaimer: This tool is for educational purposes only, the credit card]
                   [generator does not generate cards with money on them, and instead,     ]
                   [simply generates a valid credit card number, that passes as a real card]
                   [and can be used for free trials instead of having to put a real credit ]
                   [card.  Using it for free trials and other payments are highly illegal  ]
                   [and you should only be using this for testing your own security, or for]
                   [educational purposes.  We are not responsible for anything you choose  ]
                   [to do with this tool, and any trouble you may get into.                ]
                    
'''


w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
rd = Fore.RED

def loading():#FYI this part is completely useless, I just added it cause it looked weird instantly printing the result, you can remove it if you would like, just make sure to remove iit from the generators too.  
    print(f"\n{c}█▒▒▒▒▒▒▒▒▒10%")
    time.sleep(.5)
    clear_screen()
    print(f"\n{c}████▒▒▒▒▒▒30%")
    time.sleep(.6)
    clear_screen()
    print(f"\n{c}████████▒▒80%")
    time.sleep(.4)
    clear_screen()
    print(f"{c}██████████100%")
    time.sleep(.5)
    clear_screen()
    print_banner()

def clear_screen():
    print("\033[H\033[J")  #Kinda buggy rn cause it is not a full screen clear but I am working on a better option


def print_banner():
    clear_screen()
    faded_banner = fade.water(banner)
    print(faded_banner)

def folders():
    if not os.path.exists('credit_card_info'):
        os.makedirs('credit_card_info')
    if not os.path.exists('fake_personal_info'):
        os.makedirs('fake_personal_info')
    if not os.path.exists('fake_company_info'):
        os.makedirs('fake_company_info')

def gen_card():
    print_banner()
    credit_menu = """
    Credit Card Generator
    [1] MasterCard
    [2] Visa
    [3] Discover
    [4] American Express
    [5] Back to Main Menu
    """
    faded_credit_menu = fade.purpleblue(credit_menu)
    print(faded_credit_menu)
    choice = input("\nChoose a card type or enter '5' to go back: ")
    if choice == '1':
        loading()
        card_info = fake.credit_card_full(card_type="mastercard") 
    elif choice == '2':
        loading()
        card_info = fake.credit_card_full(card_type="visa")
    elif choice == '3':
        loading()
        card_info = fake.credit_card_full(card_type="discover")   
    elif choice == '4':
        loading()
        card_info = fake.credit_card_full(card_type="amex")
    elif choice == '5':
        return
    else:
        input("Invalid choice. Press Enter to continue...")
        gen_card()

    faded_card_info = fade.purpleblue(card_info)
    print(faded_card_info)

    save_option = input("\nDo you want to save this card information? (y/n): ").lower()#Was on a time crunch for the save to folder part so I ended up using chatgpt  to fix the errors which is why it may be buggy
    if save_option == 'y':
        file_choice = input("\nWhat do you want to name the file: ")
        filename = os.path.join('credit_card_info', f'{file_choice}.txt')
        with open(filename, 'a') as f:
            f.write(card_info)
            f.write("\n\n")
        print(f"Card information saved to '{filename}'")
    input("\nPress Enter to continue...")



def company_info():
    print_banner()
    loading()
    print("Company Information:\n")
    company_name = fake.company()
    company_email = fake.email()
    company_job = fake.job()
    company_slogen = fake.bs()
    full_company_info = f"Company Name: {company_name}\nCompany Job: {company_job}\nCompany Slogan: {company_slogen}\nCompany Email: {company_email}"
    faded_company_info = fade.water(full_company_info)
    print(faded_company_info)
    save_option = input("\nDo you want to save this company information? (y/n): ").lower() #Was on a time crunch for the save to folder part so I ended up using chatgpt  to fix the errors which is why it may be buggy
    if save_option == 'y':
        file_choice = input("\nWhat do you want to name the file: ")
        filename = os.path.join('fake_company_info', f'{file_choice}.txt')
        with open(filename, 'a') as f:
            f.write(full_company_info)
        print(f"Company information saved to '{filename}'")
    input("\nPress Enter to continue...")



def menu():
    print_banner()
    folders()
    while True:
        print_banner()
        menu_options = """
        [1] Generate Credit Card
        [2] Generate Fake Personal Info
        [3] Validate Credit Card
        [4] Generate Fake Company Info
        [5] Help
        [6] Credits
        [7] Exit
        """
        faded_menu = fade.water(menu_options)
        print(faded_menu)
        choice = input("\nSelect an option: ")

        if choice == '1':
            gen_card()
        elif choice == '2':
            fake_info()
        elif choice == '3':
            validate_credit_card()
        elif choice == '4':
            company_info()
        elif choice == '5':
            help_menu()
        elif choice == '6':
            credits()
        elif choice == '7':
            break
        else:
            input("Invalid choice. Press Enter to continue...")


def fake_info():
    print_banner()
    loading()
    print("Generated Fake Personal Information:\n")
    name = fake.name()
    address = fake.address()
    email = fake.email()
    
    fake_info_full = f"Name: {name}\nAddress: {address}\nEmail: {email}"
    faded_fake_info = fade.purpleblue(fake_info_full)
    print(faded_fake_info)
    
    save_option = input("\nDo you want to save this fake personal information? (y/n): ").lower()#Was on a time crunch for the save to folder part so I ended up using chatgpt  to fix the errors which is why it may be buggy
    if save_option == 'y':
        file_choice = input("\nWhat do you want to name the file: ")
        filename = os.path.join('fake_personal_info', f'{file_choice}.txt')
        with open(filename, 'a') as f:
            f.write(f"Name: {name}\nAddress: {address}\nEmail: {email}\n\n")
        print(f"Fake personal information saved to '{filename}'")
    input("\nPress Enter to continue...")



def validate_credit_card():
    print_banner()
    card_number = input(f"{c}Enter Credit Card Number: ")
    if not any(char.isdigit() for char in card_number):
        print(f"{c}Invalid input. Credit card number must contain digits.")
        input("\nPress Enter to continue...")
        return
    formated_number = format_card(card_number)
    if formated_number != card_number:
        print(f"\n{c}Formated Credit Card Number:", formated_number)
        time.sleep(1.5)
    loading()
    validation = validate_card(formated_number)
    if validation == True:
        validation_result = f"{g}The Credit Card Number is Valid"
    else:
        validation_result = f"{lr}The Credit Card Number is Invalid"    
    Card_Type = identify_card_type(formated_number)
    print("\n Validation Result:", validation_result)
    time.sleep(.2)
    print("\n Card Type:", Card_Type)
    time.sleep(1)
    input("\nPress Enter to continue...")

def help_menu():
    print_banner()
    help_menu_text = """
    PolarGen help
    This script allows you to
    - Generate fake credit card numbers
    - Generate fake personal information
    - Validate credit card numbers
    - Generate fake company information
    - Save generated information to a file
    Feel free to leave any suggestions, issues, questions, etc on the issues tab of https://github.com/LwkeyDev/PolarGen
    """
    faded_help_menu = fade.water(help_menu_text)
    print(faded_help_menu)
    choice = input("\nType would you like to know more about how the generators work (y/n): ").lower()
    if choice == 'y' or 'yes' or 'ya':
        clear_screen()
        print(f"\n{c}For generating fake credit card numbers, the script uses an algorithim called Luhns Algorithm.")
        print(f"\n{c}This is the same algorithim used to generate real credit card numbers.")
        print(f"{c}For the CVV/CVC, the script simply picks 3 random numbers in the correct ranges to be valid")
        print(f"{c}For generating names, experation dates, jobs, etc, the script simply goes through a list of names, jobs, etc")
        print(f"{c}While the generated cards do not actually have any money on them, they could pass as a real credit card for a free trial")
        print(f"{c}Using it for paying for free trials, or other things that are not yours is illegal")
        print(f"{c}We are not responsible for any harm you or others may cause themselves. ")
        time.sleep(3)
        input(f"\n{lr}Press Enter to continue...")

    else:
        input("\nPress Enter to continue...")
def credits():
    print("Credits:\n")
    print("Created by Lwkey")
    print("Libraries for generating information from joke2k")
    print("Credit Card Validator from adelq")
    choice = input("\nType 10 for more details about the Author or type 5 to go back to the menu: ")
    if choice == '10':
        print("\nWasup, thanks for using PolarGen! Im just a solo dev tryna make his mark on the world of programming.")
        print("\nFor more details check out my profile at https://github.com/LwkeyDev")
        print("\nFeel free to leave any comments, suggestions, issues, etc on the issues tab of https://github.com/LwkeyDev/PolarGen")
        input("\nPress Enter to continue...")
    else:
        input("\nPress Enter to continue...")
        



if __name__ == "__main__":
    menu()
