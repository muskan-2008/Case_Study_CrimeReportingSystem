class IncidentNumberNotFound(Exception):
    def __init__(self):
        super().__init__(f'Incident ID not found')