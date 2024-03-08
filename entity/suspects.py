from util.DBConnUtil import DBConnection
class Suspects(DBConnection):
    def __init__(self):
        super().__init__()
        self.suspectid=0
        self.firstname=' '
        self.lastname=' '
        self.dateofbirth=' '
        self.gender=' '
        self.contactnumber=0

    #Setters

    def set_suspectid(self,value):
        self.suspectid=value

    def set_firstname(self, value):
        self.firstname = value

    def set_lastname(self, value):
        self.lastname = value

    def set_dateofbirth(self, value):
        self.dateofbirth= value

    def set_gender(self, value):
        self.gender = value

    def set_contactnumber(self, value):
        self.contactnumber = value


    #Getters

    def get_suspectid(self):
        return self.suspectid

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_dateofbirth(self):
        return self.dateofbirth

    def get_gender(self):
        return self.gender

    def get_contactnumber(self):
        return self.contactnumber

    def str(self):
        return f'Suspect ID:{self.suspectid} First Name:{self.firstname} Last Name:{self.lastname}\n ' \
               f'Date Of Birth:{self.dateofbirth} Gender:{self.gender} Contact Number:{self.contactnumber}'


