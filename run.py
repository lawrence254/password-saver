#!/usr/bin/env python3.7

def create_user(name,username,password):
    '''
    Function to create a new user
    '''
    new_user = User(name,username,password)
    return new_user