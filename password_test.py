import unittest
from password import User , Credential

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Langat","justo01","justo12345") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.name,"Langat")
        self.assertEqual(self.new_user.username,"justo01")
        self.assertEqual(self.new_user.password,"justo12345")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)
    
    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    # other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Langat","justo01","justo12345") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)    

    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Langat","justo01","justo12345") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)

    def test_find_user_by_name(self):
        '''
        test to check if we can find a user by name and display information
        '''
        self.new_user.save_user()
        test_user = User("Langat","justo01","justo12345") # new user
        test_user.save_user()

        found_user = User.find_by_name("Langat")

        self.assertEqual(found_user.username,test_user.username)   

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User("Langat","justo01","justo12345") # new user
        test_user.save_user()

        user_exists = User.user_exist("Langat")

        self.assertTrue(user_exists)  


class TestCredential(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("Langat","twitter","justo01","justo12345") # create credential object  

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.name,"Langat")
        self.assertEqual(self.new_credential.account,"twitter")
        self.assertEqual(self.new_credential.username,"justo01")
        self.assertEqual(self.new_credential.password,"justo12345")    

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the user object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)     

    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []    

    # other test cases here
    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Langat","twitter","justo01","justo12345") # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)  

    def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credential from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Langat","twitter","justo01","justo12345") # new credential
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting a credential object
            self.assertEqual(len(Credential.credential_list),1)    

    def test_find_credential_by_name(self):
        '''
        test to check if we can find a credential by name and display information
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Langat","twitter","justo01","justo12345") # new credential
        test_credential.save_credential()

        found_credential = Credential.find_by_name("Langat")

        self.assertEqual(found_credential.username,test_credential.username)                         


if __name__ ==  '__main__':
    unittest.main()




