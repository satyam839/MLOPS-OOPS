class Chatbook:
    __user_id = 0
    def __init__(self):
        # here name is encapsulated or hidden attribute 
        self.__name = "Default User"
        self.id = Chatbook.__user_id
        Chatbook.__user_id+=1
        self.username = ""
        self.password = ""
        self.loggedin = False
        #self.menu()
    def getter(self):
        return self.__name
    def setter(self,value):
        self.__name = value
    @staticmethod
    def get_ter():
        return Chatbook.__user_id
    @staticmethod
    def set_ter(valu):
        Chatbook.__user_id = valu
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
            self.my_post()
        elif user_input == "4":
            self.sending()
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
    def my_post(self):
        if self.loggedin == True:
            txt = input("enter your post here -> ")
            print(f"following content has been posted -> {txt}")
        else:
            print("you need to signin first to post something....")
        print("\n")
        self.menu()  
    def sending(self):
        if self.loggedin == True :
            txt = input("enter your message here -> ")
            frnd = input("whom to send the msg -> ")
            print(f"your message has been sent to {frnd}")
        else:
            print("you need to signin first to send the message")
        print("\n")
        self.menu()

                

obj = Chatbook()         
                     