#!/usr/bin/env python3.7
from password import User, Credential
import random
import getpass

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

def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()   

def del_credential(credential):
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

    ask= input(f"Hello {name}.Do you have an account? yes or no")
    print('\n')
          
if __name__ == '__main__':

    main()                                  
                       