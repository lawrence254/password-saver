#!/usr/bin/env python3.7
from password import User, Credential
import random
import getpass
import string

def create_user(name,username,password):
    '''
    Function to create a new user
    '''
    new_user = User(name,username,password)
    return new_user

def generate_password(user):
    """
    Function to generate random password for user
    """
    return user.generate_random_password()    

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()   

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()     

def create_credential(name, account, username, password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(name,account,username,password)
    return new_credential  

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()   

def del_credential():
    '''
    Function to delete a credential
    '''
    credential.delete_credential()   

def find_credential(username):
    '''
    Function that finds a credential by username and returns the credential
    '''
    return Credential.find_by_username(username)    

def check_existing_credentials(username):
    '''
    Function that check if a credential exists with that username and return a Boolean
    '''
    return Credential.credential_exist(username)      

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()  


def main():
    print("Welcome to password locker. What is your name?")
    name = input()

    ask= input(f"Hello {name}.Do you have an account? yes or no > ")

    if ask == "no":
        print("Signup now to use our services")
        username = input("Enter your preffered username > ")
        create = input(f"Good to have you {username}. Do you want autogenerated password? yes or no > ")
        if create == "no":
            print("Please enter your preffered password then")
            getpass.getpass()
            print("Signin successfull") 

        while True:
            print("""
            Use the short codes: cc to create new credential
                                 dc to display credential
                                 fc to find credential
                                 dl to delete credential
                                 rp to generate random password
                                 ex to exit
                                 """)  
            short_code = input ("Navigate now using the short-codes > ")    

            if short_code == "cc":
               print("Create new account")
               print("-"*12)   

               print("Enter your name(s)")
               name = input("> ")

               print("Enter account for example facebook, twitter...")  
               account = input("> ")

               print("Enter you preffered username...")
               username=input("> ")

               print("Enter password")
               password=input("> ")

               save_credential(create_credential(name, account, username, password))

               print("\n")
               print(f"New credential Nam: {name} account: {account} username: {username} and password {password} have just been created")
               print("\n")

            elif short_code == "rp":
                print(
                    "Please enter the account you want to generate password for > ")
                account = input("Enter account type > ")   

                def random_password(string_length):
                    letters = string.ascii_letters
                    return "".join(random.choice(letters) for i in range(string_length))

                print(
                    f"Your autogenerated password for {account} is: ", random_password(10))

            elif short_code == "dc":

                if display_credentials():
                    print("Here is a list of all your Credentials and passwords")
                    print("\n")
                    for credential in display_credentials():
                        print(f"Name: {credential.name} Account: {credential.account} Username: {credential.username}Password: {password}")
                        print("\n")
                else:
                    print("\n")
                    print(
                        "You don't have any saved credentials yet.")
                    print("\n")

            elif short_code == 'fc':

                print("Enter the account username you want to search for")

                search_account_username = input()
                if check_existing_credentials(search_username):
                    search_credential = find_credential(search_username)
                    print(f"{search_credential.account} {search_credential.username}")
                    print('-' * 25)

                    print(f"Account password....{search_credential.password}")

                else:
                    print("That credential does not exist")

            elif short_code == "dl":
                print("Enter the account username of the credential you would like to delete.")
                username = input("> ")
                username = find_credential(username)
                Credential.credential_list.remove(username)
                
            elif short_code == "ex":
                print("Logged out")
                break

    elif ask == "yes":
               print("Welcome back to our password locker. Enter your username and password to login")
               username = input("Enter username > ")
               print("|Don't mind if your password is not vissible as you type. WE go your password secured.|")#
               account_password= getpass.getpass()
               while True:
                    print("""
                    Use the short codes: cc to create new credential
                                 dc to display credential
                                 fc to find credential
                                 dl to delete credential
                                 rp to generate random password
                                 ex to exit
                                 """)  
                    short_code = input ("Navigate now using the short-codes > ")   
                        
                    
                    if short_code == "cc":
                        print("Create new account")
                        print("-"*12)   

                        print("Enter your name(s)")
                        name = input("> ")

                        print("Enter account for example facebook, twitter...")  
                        account = input("> ")

                        print("Enter you preffered username...")
                        username=input("> ")

                        print("Enter password")
                        password=input("> ")

                        save_credential(create_credential(name, account, username, password))

                        print("\n")
                        print(f"New credential Name: {name} Account: {account} username: {username} Password: {password} have just been created")
                        print("\n")

                    elif short_code == "rp":
                        print(
                        "Please enter the account you want to generate password for > ")
                        account = input("Enter account type > ")   

                        def random_password(string_length):
                           letters = string.ascii_letters
                           return "".join(random.choice(letters) for i in range(string_length))

                           print(f"Your autogenerated password for {social_media} is: ", random_password(10))

                    elif short_code == "dc":

                        if display_credentials():
                           print("Here is a list of all your Credentials and passwords")
                           print("\n")
                        for credential in display_credentials():
                           print(f"{credential.name} {credential.account} {credential.username}{password}")
                           print("\n")
                        else:
                           print("\n")
                           print("You don't have any saved credentials yet.")
                           print("\n")

                    elif short_code == 'fc':

                        print("Enter the account username you want to search for")

                        search_username = input()
                        if check_existing_credentials(search_username):
                           search_credential = find_credential(search_username)
                           print(f"{search_credential.account} {search_credential.username}")
                           print('-' * 25)

                           print(f"Account password....{search_credential.password}")

                        else:
                           print("That credential does not exist")

                    elif short_code == "dl":
                           print("Enter the account username of the credential you would like to delete.")
                           username = input("> ")
                           username = find_credential(username)
                           Credential.credential_list.remove(username)
                           print(f" Credential with{username}has been moved to trash successfully")

                    elif short_code == "ex":
                           print("Logged out")
                           break
                    else:
                           print("Please check your input")    

                
        
if __name__ == '__main__':

    main()                                  
                       