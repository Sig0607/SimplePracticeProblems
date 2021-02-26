#Superclass that creates objects 
# 1) Create a Superclass called BankAccount with variables fname, lname, and address and a function or method display

# to display fname, lname, and address.

# 2) Create a 1st Subclass called CheckingAccount with variable checking_account_number and 3 functions; function

# deposit() with d_amt as parameter and withdrawal() with w_amt as parameter and a display function to display the current balance, the d_amt, and the d_amt.

# set the original balances of the following variables as follow

#         self.checking_balance = 500
#         self.d_amt = 0
#         self.w_amt = 0

# 3) Create a 2nd Subclass called SavingAccount with it own separate variables : saving_account_number, and

#         self.saving_balance = 300
#         self.saving_deposit = 0
#         self.saving_withdrawal = 0
#         self.interest_rate = 1.04

# This class also has 3 functions:  s_deposit(), s_withdraw(), and display() to display the saving_balance, the s_deposit, the s_withdrawal, and interest_rate.

# create 3 objects for this exercise.. 1 object for the BankAccount class, 1 object for the CheckingAccount class and 1 object for the SavingAccount class to test your bankAccount file and classes..

# Use the keyword super() to call the Superclass constructor and/or functions from your subclass functions.

# Write a clear and easy to read code, test them and if passed, submit the for credit.
class bankaccount():
    #Iniatilize the variables
    def __init__(self, fname, lname, address):
        self.fname=fname
        self.lname=lname
        self.address=address
    #display function basically displays the variables iniatlized in the initate fucntion
    def display(self):
        print(self.fname+" "+ self.lname+","+self.address)
#First object we give it 3 strings so it can feed into the init function
Rocket=bankaccount("Kevin","Yang","adressno")
Rocket.display()
#Create a subclass by passing a parent class through a class in this case Bankaccount
class Checkingaccount(bankaccount):
    #this here iniatilizes a function and therfore overides the init from the parent class 
    def __init__(self,fname,lname,address,checking_account_number,checking_balance,d_amt,w_amt):
        self.checking_account_number=checking_account_number
        self.checking_balance=500
        self.d_amt=0
        self.w_amt=0
        #To iniatlize a both inits you need to use the super function() it instead of letting the 
        #child class/function always override instead lets the one of higher inheritance over ride 
        super().__init__(fname,lname,address)
    #this takes the paramater d_amt which was iniatilized
    def deposit(self,d_amt):
        #we use self.checking_account instead of checking_account becuase the self function saves it to the
        #class/object instead of just this one variable allowing it to be used in other functions
        self.checking_account_number=self.checking_account_number+d_amt
        print(self.checking_account_number)
    def withdrawal(self,w_amt):
        self.checking_account_number=self.checking_account_number-w_amt
        print(self.checking_account_number)
Yoru=Checkingaccount("Yoru","Noice","addressyes",1000,500,0,0)
Yoru.deposit(50)
Yoru.withdrawal(100)
#Creating the subclass SavingAccount passing through the parent class as an argument
class Savingaccount(bankaccount):
    def __init__(self,fname,lname,address,saving_balance,saving_deposit,saving_withdrawal,interest_rate):
        self.saving_balance=300
        self.saving_deposit=0
        self.saving_withdrawal=0
        self.interest_rate=1.04
        #using the super function to have both init functions so the parent function overrides the child function
        super().__init__(fname,lname,address)
    def s_deposit(self, saving_deposit):
        #we update thes self.saing_deposit to equal teh saving deposit so we can display it in a later function
        #since remember self. is the only way to use a variable within a class in multiple functions
        self.saving_deposit=saving_deposit
        self.saving_balance=self.saving_balance+self.saving_deposit
        print(self.saving_balance)
    def s_withdraw(self,saving_withdrawal):
        self.saving_withdrawal=saving_withdrawal
        self.saving_balance=self.saving_balance-self.saving_withdrawal
        print(self.saving_balance)
    def display(self):
        print(self.saving_balance,self.saving_deposit,self.saving_withdrawal,self.interest_rate)
Kekw=Savingaccount("Kayle","Hello","yoruaddress",300,0,0,1.04)
Kekw.s_deposit(90)