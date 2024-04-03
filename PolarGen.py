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
                                                  {Version: 3.0.1}
   
   
   
                                             {The Ultimate Info Generator}

                    
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
    faded_banner = fade.purpleblue(banner)
    print(faded_banner)

def folders():
    if not os.path.exists("credit_card_info"):
        os.makedirs("credit_card_info")
    if not os.path.exists("fake_personal_info"):
        os.makedirs("fake_personal_info")
    if not os.path.exists("fake_company_info"):
        os.makedirs("fake_company_info")
    if not os.path.exists("credit_card_mass_generator"):
        os.makedirs("credit_card_mass_generator")
def gen_card():
    clear_screen()
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
    clear_screen()
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
        
                                      
                         ╠═════════════════════════════════════════════════════════════════════╣       
                         ║                                                                     ║      
                         ║ [1] Credit Card     [2] Validate Card     [3] Mass Gen Credit Cards ║     
                         ║                                                                     ║      
                         ║ [4] Fake Company Info     [5] Fake personal info     [6] Exit       ║     
                         ╚                                                                     ╝    
                         
                        
        """
        faded_menu = fade.water(menu_options)
        print(faded_menu)
        choice = input(f"\n{lb}Select an option: ")
        if choice == '1':
            gen_card()
        elif choice == '2':
            validate_credit_card()
        elif choice == '3':
            mass_credits()
        elif choice == '4':
            company_info()
        elif choice == '5':
            fake_info()
        elif choice == '6':
            custom_exit()
        else:
            input("Invalid choice. Press Enter to continue...")



def custom_exit():
    print_banner()
    choice = input(f"\n{lr}Are you sure you would like to exit the program? (y/n): ").lower()
    if choice == "y" or choice == "ya" or choice == "yes":
        print("Exiting...")
        exit()
    elif choice == "n" or choice == "no" or choice == "nope" or choice == "nah":
        print(f"{g}Returning...")
        return menu()
    else:
        print(f"{lr}Invalid Selection.  Press Enter to continue...")

def fake_info():
    clear_screen()
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
    clear_screen()
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



def mass_credits():
    clear_screen()
    print_banner()
    credit_menu = """
    Mass Credit Card Generator
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
        card_type = "mastercard"
    elif choice == '2':
        card_type = "visa"
    elif choice == '3':
        card_type = "discover"   
    elif choice == '4':
        card_type = "amex"
    elif choice == '5':
        return
    else:
        input("Invalid choice. Press Enter to continue...")
        mass_credits()
        
    num_cards = int(input(f"\n{c}How many cards would you like to generate: "))

    file_choice = input("\nWhat do you want to name the file: ")
    filename = os.path.join('credit_card_mass_generator', f'{file_choice}.txt')
    with open(filename, 'a') as f:
        for i in range(1, num_cards + 1):
            card_info = fake.credit_card_full(card_type=card_type) 
            f.write(f"[{i}] {card_info}\n\n")
        loading()
        print(f"{c}{num_cards} cards have been successfully saved to '{filename}'")
    
    input(f"{lr}\nPress Enter to continue...")

        



if __name__ == "__main__":
    menu()
