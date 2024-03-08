from dao.evidencedao import EvidenceDao
from dao.incidentsdao import IncidentsDao
from dao.lawinforcementagenciesdao import LawInforcementAgenciesDao
from dao.officersdao import OfficersDao
from dao.reportsdao import ReportsDao
from dao.suspectsdao import SuspectsDao
from dao.victimsdao import VictimsDao
from exception.incidentnumbernotfoundexception import IncidentNumberNotFound

class  CrimeAnalysisServiceImpl(EvidenceDao,IncidentsDao,LawInforcementAgenciesDao,OfficersDao,ReportsDao,SuspectsDao,VictimsDao,IncidentNumberNotFound):

#Update Incident Status

    def updateincidentstatus(self):
       try:
          self.open()
          incidentid = int(input('Input Incident ID to be Updated: '))
          self.status = input('Enter Status: ')
          data = [( self.status, incidentid)]
          update_str = '''UPDATE Incidents SET  status=%s
                           WHERE incidentid = %s'''
          self.stmt.executemany(update_str, data)
          self.conn.commit()
          self.close()
          return True
       except Exception as e:
          return f"Error updating Incident: {e}"

# Get Incidents within a range
    def getIncidentsInDateRange(self):
       try:
          print('Enter Start Date (YYYY-MM-DD): ')
          startdate = input()
          print('Enter End Date (YYYY-MM-DD): ')
          enddate = input()
          self.open()
          select_str = f'''SELECT * FROM Incidents WHERE incidentdate BETWEEN %s AND %s'''
          self.stmt.execute(select_str, (startdate, enddate))
          records = self.stmt.fetchall()
          self.close()
          print("Records in table")
          for i in records:
             print(i)
       except Exception as e:
           print(e)



#Search Incidents
    def searchIncidents(self):
       try:
          self.open()
          incidenttype = input('Input Incident Type to see the details: ')
          data = f"'{incidenttype}'"
          select_str = f'''SELECT * FROM Incidents WHERE incidenttype={data} '''
          self.stmt.execute(select_str)
          records = self.stmt.fetchall()
          self.close()
          return records

       except Exception as e:
          print(e)

# Generate Incident Reports
    def generatIncidentReport(self, incidentid):

       print('Enter Incident ID to get Reports: ')
       try:
          self.open()
          select_str = f'''SELECT * FROM Reports WHERE incidentid={incidentid}'''
          self.stmt.execute(select_str)
          records = self.stmt.fetchall()
          self.close()
          if not records:
             raise IncidentNumberNotFound
          return records
       except IncidentNumberNotFound as e:
          return e
       except Exception as e:
          print(e)
          return None
