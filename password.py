class User:

    """
    Class that generates new instances of users.
    """

    user_list = [] # Empty user list

    def __init__(self,name,username,password):

      # docstring removed for simplicity

        self.name = name
        self.username = username
        self.password = password
        
     # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
        
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    # def get_all_users():
    #     pass

    @classmethod
    def find_by_name(cls,name):
        '''
        Method that takes in a name and returns a user that matches that name.

        Args:
            name:  name to search for
        Returns :
            User that matches the name.
        '''

        for user in cls.user_list:
            if user.name == name:
                return user   

    @classmethod
    def user_exist(cls,name):
        '''
        Method that checks if a user exists from the user list.
        Args:
            name: name to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.name == name:
                    return True

        return False   


class Credential:
    
    """
    Class that generates new instances of credential.
    """
    
    credential_list=[]
    
    def __init__(self, name, account, username, password):
        # docstring removed for simplicity
        self.name = name
        self.account= account
        self.username = username
        self.password = password
    
        # Init method up here
    def save_credential(self):
    
        '''
        save_user method saves credential objects into credential_list
        '''
    
        Credential.credential_list.append(self)  

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)   

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a credential that matches that username.

        Args:
            username:  username to search for
        Returns :
            Credential that matches the username.
        '''

        for credential in cls.credential_list:
            if credential.username == username:
                return credential  

    @classmethod
    def credential_exist(cls,name):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            name: name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.name == name:
                    return True

        return False  

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list   
