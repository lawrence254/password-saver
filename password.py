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
        
          