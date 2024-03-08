from entity.incidents import Incidents
from entity.officers import Officers
class Reports(Incidents, Officers):
    def __init__(self):
        super().__init__()
        self.reportid=0
        self.incidentid=0
        self.reportingofficer=0
        self.reportdate=' '
        self.reportdetails=' '
        self.status=' '

    #Setters

    def set_reportid(self,value):
        self.reportid=value

    def set_incidentid(self, value):
        self.incidentid = value

    def set_reportingofficer(self, value):
        self.reportingofficer= value

    def set_reportdate(self, value):
        self.reportdate= value

    def set_reportdetails(self, value):
        self.reportdetails= value

    def set_status(self, value):
        self.status= value


    #Getters

    def get_reportid(self):
        return self.reportid

    def get_incidentid(self):
        return self.incidentid

    def get_reportingofficer(self):
        return self.reportingofficer

    def get_reportdate(self):
        return self.reportdate

    def get_reportdetails(self):
        return self.reportdetails

    def get_status(self):
        return self.status



    def str(self):
        return f'Report ID:{self.reportid} Incident ID:{self.incidentid} Reporting Officer:{self.reportingofficer}\n ' \
               f'Report Date:{self.reportdate} Report Details:{self.reportdetails} Status:{self.status}'


