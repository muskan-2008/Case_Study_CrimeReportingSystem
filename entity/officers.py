from util.DBConnUtil import DBConnection
class Officers(DBConnection):
    def __init__(self):
        super().__init__()
        self.officerid=0
        self.firstname=' '
        self.lastname=' '
        self.badgenumber=0
        self.rank_=0
        self.contactnumber=0

    #Setters

    def set_officerid(self,value):
        self.officerid=value

    def set_firstname(self, value):
        self.firstname = value

    def set_lastname(self, value):
        self.lastname = value

    def set_badgenumber(self, value):
        self.badgenumber= value

    def set_rank_(self, value):
        self.rank_ = value

    def set_contactnumber(self, value):
        self.contactnumber = value




    #Getters

    def get_officerid(self):
        return self.officerid

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_badgenumber(self):
        return self.badgenumber

    def get_rank_(self):
        return self.rank_

    def get_contactnumber(self):
        return self.contactnumber

    def str(self):
        return f'Officer ID:{self.officerid} First Name:{self.firstname} Last Name:{self.lastname}\n ' \
               f'Badge Number:{self.badgenumber} Rank:{self.rank_} Contact Number:{self.contactnumber}'


