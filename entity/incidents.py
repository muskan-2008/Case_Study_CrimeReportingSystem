from entity.suspects import Suspects
from entity.victims import Victims

class Incidents(Suspects, Victims):
    def __init__(self):
        super().__init__()
        self.incidentid=0
        self.incidenttype=' '
        self.incidentdate=' '
        self.location=' '
        self.description=' '
        self.status=' '
        self.victimid=0
        self.suspectid = 0
    #Setters

    def set_incidentid(self,value):
        self.incidentid=value

    def set_incidenttype(self, value):
        self.incidenttype = value

    def set_incidentdate(self, value):
        self.incidentdate = value

    def set_location(self, value):
        self.location= value

    def set_description(self, value):
        self.description = value

    def set_status(self, value):
        self.status = value

    def set_victimid(self, value):
        self.victimid = value

    def set_suspectid(self, value):
        self.suspectid = value

    #Getters

    def get_incidentid(self):
        return self.incidentid

    def get_incidenttype(self):
        return self.incidenttype

    def get_incidentdate(self):
        return self.incidentdate

    def get_location(self):
        return self.location

    def get_description(self):
        return self.description

    def get_status(self):
        return self.status

    def get_victimid(self):
        return self.victimid

    def get_suspectid(self):
        return self.suspectid

    def str(self):
        return f'Incident ID:{self.incidentid} Incident Type:{self.incidenttype} Incident Date:{self.incidentdate}\n ' \
               f'Location:{self.location} Description:{self.description} Status:{self.status} Victim ID:{self.victimid} Suspect ID:{self.suspectid}'


