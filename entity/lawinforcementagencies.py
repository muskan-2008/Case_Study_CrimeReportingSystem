from entity.officers import Officers

class LawInforcementAgencies(Officers):
    def __init__(self):
        super().__init__()
        self.agencyid=0
        self.agencyname=' '
        self.jurisdiction=' '
        self.contactnumber=0
        self.officerid=0

    #Setters

    def set_agencyid(self,value):
        self.agencyid=value

    def set_agencyname(self, value):
        self.agencyname = value

    def set_jurisdiction(self, value):
        self.jurisdiction= value

    def set_contactnumber(self, value):
        self.contactnumber= value

    def set_officerid(self, value):
        self.officerid= value


    #Getters

    def get_agencyid(self):
        return self.agencyid

    def get_agencyname(self):
        return self.agencyname

    def get_jurisdiction(self):
        return self.jurisdiction

    def get_contactnumber(self):
        return self.contactnumber

    def get_officerid(self):
        return self.officerid


    def str(self):
        return f'Agency ID:{self.agencyid} Agency Name:{self.agencyname} Jurisdiction:{self.jurisdiction}\n ' \
               f'Contact Number:{self.contactnumber} Officer ID:{self.officerid}'
