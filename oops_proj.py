class Chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()
    def menu(self):
        user_input = input("""
Welcome to Chatbook !! How would you like to proceed ?
1. Press 1 to Signup
2. Press 2 to Signin
3. Press 3 to write a post
4. Press 4 to message a friend
5. Press any other key to exist """)
        if user_input == "1":
            self.Signup()
        elif user_input == "2":
            self.Signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
    def Signup(self):
        email = input("Enter your Email here -> ")
        pas = input("set your password -> ")
        self.username = email
        self.password = pas
        print("Signup succesfully ")
        print("\n")
        self.menu()
    def Signin(self):
        if self.username == "" and self.password == "":
            print("Please signup first by pressing 1 in the main menu")
        else:
            usrname = input("enter your email/username here -> ")
            psd = input("enter your password here -> ")
            if self.username == usrname and self.password == psd:
                print("Sign in successfully")
                self.loggedin = True
            else:
                print("please input correct credentials") 
        print("\n")
        self.menu()       
                

obj = Chatbook()                               