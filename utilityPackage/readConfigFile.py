import configparser
config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class ReadConfig_Class:

    @staticmethod
    def getUsername():
        Username = config.get('sign in','username')
        return Username

    @staticmethod
    def getPassword():
        Password = config.get('sign in','password')
        return Password



    @staticmethod
    def getUserNametoEdit():
        Username = config.get('Edit User', 'Username')
        return Username

    @staticmethod
    def getNewUserName():
        NewUsername = config.get('Edit User','NewUsername')
        return NewUsername

    @staticmethod
    def getNewPassword():
        NewPassword = config.get('Edit User','NewPassword')
        return NewPassword



    @staticmethod
    def getUserid_to_Create_cust():
        Userid  =config.get('Customer Mgmt Create','userid')
        return Userid




    @staticmethod
    def getCustomerId():
        Customerid = config.get('Customer Edit', 'Customerid')
        return Customerid

    @staticmethod
    def getCustNewFirstname():
        Cust_firstname = config.get('Customer Edit', 'CustNewFirstName')
        return Cust_firstname

    @staticmethod
    def getCustNewLastname():
        Cust_lastname = config.get('Customer Edit', 'CustNewLastName')
        return Cust_lastname

    @staticmethod
    def getCustNewDob():
        Cust_newdob = config.get('Customer Edit', 'CustNewDob')
        return Cust_newdob



    @staticmethod
    def getCustomerId_to_Del():
        CustomerId = config.get('Customer Delete', 'Customerid')
        return CustomerId




    @staticmethod
    def getAccountId():
        AccountId = config.get('Account Edit','AccountId')
        return AccountId

    @staticmethod
    def getNewAccountType():
        AccountType = config.get('Account Edit', 'AccountType')
        return AccountType

    @staticmethod
    def getNewBalance():
        Balance = config.get('Account Edit', 'Balance')
        return Balance




    @staticmethod
    def getTransferId():
        Transferid =config.get('Transfer Edit','transferId')
        return Transferid

    @staticmethod
    def getAmount():
        Amnt = config.get('Transfer Edit', 'Amount')
        return Amnt

    @staticmethod
    def getDescription():
        descript = config.get('Transfer Edit', 'Description')
        return descript