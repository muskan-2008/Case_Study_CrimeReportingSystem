from entity.incidents import Incidents

class Evidence(Incidents):
    def __init__(self):
        super().__init__()
        self.evidenceid=0
        self.description=' '
        self.locationfound=' '
        self.incidentid=0

    #Setters

    def set_evidenceid(self,value):
        self.evidenceid=value

    def set_description(self, value):
        self.description= value

    def set_locationfound(self, value):
        self.locationfound = value

    def set_incidentid(self, value):
        self.incidentid =value


    #Getters

    def get_evidenceid(self):
        return self.evidenceid

    def get_description(self):
        return self.description

    def get_locationfound(self):
        return self.locationfound

    def get_incidentid(self):
        return self.incidentid
    def str(self):
        return f'Evidence ID:{self.evidenceid} Description:{self.description} Location Found:{self.locationfound}\n ' \
               f'Incident ID:{self.incidentid}'
