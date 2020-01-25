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
    def find_by_name(cls,name):
        '''
        Method that takes in a name and returns a credential that matches that name.

        Args:
            name:  name to search for
        Returns :
            Credential that matches the name.
        '''

        for credential in cls.credential_list:
            if credential.name == name:
                return credential   
       
    