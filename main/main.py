from dao.crimeanalysisserviceimpl import CrimeAnalysisServiceImpl
from dao.evidencedao import EvidenceDao
from dao.incidentsdao import IncidentsDao
from dao.lawinforcementagenciesdao import LawInforcementAgenciesDao
from dao.officersdao import OfficersDao
from dao.reportsdao import ReportsDao
from dao.suspectsdao import SuspectsDao
from dao.victimsdao import VictimsDao
from exception.incidentnumbernotfoundexception import IncidentNumberNotFound
from util.DBConnUtil import DBConnection

def main():

    dbconnection = DBConnection()

    try:
        dbconnection.open()
        print("--Database Is Connected:--")
    except Exception as e:
        print(e)

    try:
        print("=" * 30)
        print("Crime Analysis and Reporting System")
        print("=" * 30)
        print("Welcome to Crime Analysis and Reporting System!")

        crime_report_system = CrimeAnalysisServiceImpl()

        while True:
            print("1.Incidents\n2.Victims\n3.Suspects\n4.LawInforcementAgencies\n5.Officers\n6.Evidence\n7.Reports\n0.I want to Manipulate the Data")
            ch = int(input("Enter choice: "))
            if ch == 1:
                i = IncidentsDao()
                i.perform_incidents_actions()
            elif ch == 2:
                v = VictimsDao()
                v.perform_victims_actions()
            elif ch == 3:
                s = SuspectsDao()
                s.perform_suspects_actions()
            elif ch == 4:
                l = LawInforcementAgenciesDao()
                l.perform_lia_actions()
            elif ch == 5:
                o = OfficersDao()
                o.perform_officers_actions()
            elif ch == 6:
                e = EvidenceDao()
                e.perform_evidence_actions()
            elif ch == 7:
                r = ReportsDao()
                r.perform_reports_actions()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

        crime_report_system=CrimeAnalysisServiceImpl()

        while True:
            print("=" * 10)
            print("---MENU---")
            print("=" * 10)
            print("1.Update Incident Status\n2.Get Incidents in Range\n3.Search Incidents\n4.Generate Incident Reports\n0.Exit")
            ch = int(input("Enter choice: "))
            if ch == 1:
                print(crime_report_system.updateincidentstatus())
            elif ch == 2:
                print(crime_report_system.getIncidentsInDateRange())
            elif ch == 3:
                print(crime_report_system.searchIncidents())
            elif ch == 4:
                print(crime_report_system.generatIncidentReport(int(input('Enter Incident ID to see Reports: '))))
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    except IncidentNumberNotFound as e:
        print(e)

    finally:
        dbconnection.close()
        print("Thankyou for visiting Crime Report and Analysis System!")
        print("--Connection Is Closed:--")


if __name__ == "__main__":
    main()
