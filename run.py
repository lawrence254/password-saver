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