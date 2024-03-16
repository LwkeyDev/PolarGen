import os
from faker import Faker
from card_identifier.cardutils import validate_card
import sys
from card_identifier.cardutils import format_card
from card_identifier.card_type import identify_card_type




fake = Faker()
banner = '''
 


                               _ \         |                ___|              
                              |   |  _ \   |   _` |   __|  |       _ \  __ \  
                              ___/  (   |  |  (   |  |     |   |   __/  |   | 
                             _|    \___/  _| \__,_| _|    \____| \___| _|  _| 
                                                                                                               
                                           {Author: Lwkey}
                                           {Version: 1.1.7}
                        
                   [Disclaimer: This tool is for educational purposes only, the credit card]
                   [generator does not generate cards with money on them, and instead,     ]
                   [simply generates a valid credit card number, that passes as a real card]
                   [and can be used for free trials instead of having to put a real credit ]
                   [card.  Using it for free trials and other payments are highly illegal  ]
                   [and you should only be using this for testing your own security, or for]
                   [educational purposes.  We are not responsible for anything you choose  ]
                   [to do with this tool, and any trouble you may get into.                ]
                    
'''

def clear_screen():
    print("\033[H\033[J")  #Kinda buggy rn cause it is not a full screen clear but I am working on a better option

def print_banner():
    clear_screen()
    print(banner)

def folders():
    if not os.path.exists('credit_card_info'):
        os.makedirs('credit_card_info')
    if not os.path.exists('fake_personal_info'):
        os.makedirs('fake_personal_info')
    if not os.path.exists('fake_company_info'):
        os.makedirs('fake_company_info')

def gen_card():
    print_banner()
    print("Credit Card Generator\n")
    print("[1] MasterCard")
    print("[2] Visa")
    print("[3] Discover")
    print("[4] American Express")
    print("[5] Back to Main Menu")
    
    choice = input("\nChoose a card type or enter '5' to go back: ")
    
    card_type = ""
    
    if choice == '1':
        card_type = "MasterCard"
        card_info = fake.credit_card_full(card_type="mastercard") 
    
    elif choice == '2':
        card_type = "Visa"
        card_info = fake.credit_card_full(card_type="visa")
    
    elif choice == '3':
        card_type = "Discover"
        card_info = fake.credit_card_full(card_type="discover")   
    
    elif choice == '4':
        card_type = "Amex"
        card_info = fake.credit_card_full(card_type="amex")
    
    elif choice == '5':
        return
    else:
        input("Invalid choice. Press Enter to continue...")
        gen_card()

    print(card_info)

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
    print("Company Information:\n")
    company_name = fake.company()
    company_address = fake.address()
    company_email = fake.email()
    company_job = fake.job()
    company_slogen = fake.bs()

    print("Company Name:", company_name)
    print("Company Job:", company_job)
    print("Company Address:", company_address)
    print("Company Email:", company_email)
    print("Company Slogen:", company_slogen)

    save_option = input("\nDo you want to save this company information? (y/n): ").lower() #Was on a time crunch for the save to folder part so I ended up using chatgpt  to fix the errors which is why it may be buggy
    if save_option == 'y':
        file_choice = input("\nWhat do you want to name the file: ")
        filename = os.path.join('fake_company_info', f'{file_choice}.txt')
        with open(filename, 'a') as f:
            f.write(f"Company Name: {company_name}\nCompany Address: {company_address}\nCompany Email: {company_email}\nCompany Slogen: {company_slogen}\nCompany Job: {company_job}\n\n")
        print(f"Company information saved to '{filename}'")
    input("\nPress Enter to continue...")
def menu():
    print_banner()
    folders()
    while True:
        print_banner()
        print("[1] Generate Credit Card")
        print("[2] Generate Fake Personal Info")
        print("[3] Validate Credit Card")
        print("[4] Generate Fake Company Info")
        print("[5] Help")
        print("[6] Credits")
        print("[7] Exit")
        choice = input("\nSelect an option: ")

        if choice == '1':
            gen_card()
        elif choice == '2':
            fake_info()
        elif choice == '3':
            validate_card()
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
    print("Generated Fake Personal Information:\n")
    name = fake.name()
    address = fake.address()
    email = fake.email()
    print("Name:", name)
    print("Address:", address)
    print("Email:", email)
    save_option = input("\nDo you want to save this fake personal information? (y/n): ").lower()#Was on a time crunch for the save to folder part so I ended up using chatgpt  to fix the errors which is why it may be buggy
    if save_option == 'y':
        file_choice = input("\nWhat do you want to name the file: ")
        filename = os.path.join('fake_personal_info', f'{file_choice}.txt')
        with open(filename, 'a') as f:
            f.write(f"Name: {name}\nAddress: {address}\nEmail: {email}\n\n")
        print(f"Fake personal information saved to '{filename}'")
    input("\nPress Enter to continue...")

def validate_card():
    print_banner()
    card_number = input("Enter Credit Card Number: ")
    if not any(char.isdigit() for char in card_number):
        print("Invalid input. Credit card number must contain digits.")
        input("\nPress Enter to continue...")
        return
    formated_number = format_card(card_number)
    print("\nFormated Credit Card Number:", formated_number)
    validation = validate_card(formated_number)
    if validation == True:
        validation_result = "The Credit Card Number is Valid"
    else:
        validation_result = "The Credit Card Number is Invalid"    
    Card_Type = identify_card_type(formated_number)
    print("\n Validation Result:", validation_result)
    print("\n Card Type:", Card_Type)
    input("\nPress Enter to continue...")

def help_menu():
    print_banner()
    print("PolarGen help\n")
    print("This toolbox allows you to:")
    print("- Generate fake credit card numbers")
    print("- Generate fake personal information")
    print("- Validate credit card numbers")
    print("- Generate fake company information")
    print("- Save generated information to a file")
    print("\nUse the provided options to navigate the toolbox.")
    print("\nFeel free to leave any suggestions, issues, questions, etc on the issues tab of https://github.com/LwkeyDev/PolarGen")
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
