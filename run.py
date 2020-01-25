#!/usr/bin/env python3.7

def create_user(name,username,password):
    '''
    Function to create a new user
    '''
    new_user = User(name,username,password)
    return new_user

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

def find_user(name):
    '''
    Function that finds a user by name and returns the user
    '''
    return User.find_by_name(name)  

def check_existing_users(name):
    '''
    Function that check if a user exists with that name and return a Boolean
    '''
    return User.user_exist(name)  


def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()  

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