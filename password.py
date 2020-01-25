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
        Method that takes in a name and returns a contact that matches that name.

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

class Credentials:
     """
    Class that generates new instances of credentials.
    """
