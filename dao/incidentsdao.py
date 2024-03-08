from entity.incidents import Incidents

class IncidentsDao(Incidents):
    def __init__(self):
        super().__init__()

    def perform_incidents_actions(self):
        while True:
            print("(Incidents) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_incidents_table()
            elif ch == 2:
                print(self.add_incidents())
            elif ch == 3:
                print(self.update_incidents())
            elif ch == 4:
                print(self.delete_incidents())
            elif ch == 5:
                self.select_incidents()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_incidents_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Incidents (
                incidentid INT  PRIMARY KEY,
                incidenttype VARCHAR(50),
                incidentdate DATE,
                location VARCHAR(100),
                description VARCHAR(255),
                status VARCHAR(50),
                victimid INT,
                suspectid INT,
                FOREIGN KEY(victimid) REFERENCES Victims(victimid) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY(suspectid) REFERENCES Suspects(suspectid) ON DELETE CASCADE ON UPDATE CASCADE)'''

            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('Incidents Table Created successfully.')
        except Exception as e:
            print(f"Error creating Incidents table: {e}")

    def add_incidents(self):
        try:
            self.open()
            self.incidentid = int(input('Enter Incident ID: '))
            self.incidenttype = input('Enter Incident Type: ')
            self.incidentdate = input('Enter Incident Date: ')
            self.location= input('Enter Location: ')
            self.description = input('Enter Description: ')
            self.status = input('Enter Status: ')
            self.victimid = int(input('Enter Victim ID: '))
            self.suspectid = int(input('Enter Suspect ID: '))
            data = [(self.incidentid, self.incidenttype, self.incidentdate, self.location,self.description,self.status,self.victimid,self.suspectid)]
            insert_str = '''INSERT INTO Incidents(incidentid,incidenttype,incidentdate,location,description,status,victimid,suspectid)
                            VALUES(%s, %s, %s, %s,%s, %s, %s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error adding Incident{e}"

    def update_incidents(self):
        try:
            self.open()
            incidentid = int(input('Input Incident ID to be Updated: '))
            self.incidenttype = input('Enter Description: ')
            self.incidentdate = input('Enter Incident Date: ')
            self.location = input('Enter Location: ')
            self.description = input('Enter Description: ')
            self.status = input('Enter Status: ')
            self.victimid = int(input('Enter Victim ID: '))
            self.suspectid= int(input('Enter Suspect ID: '))
            data = [(self.incidenttype, self.incidentdate, self.location ,self.description,self.status,self.victimid,self.suspectid,incidentid)]
            update_str = '''UPDATE Incidents SET incidenttype=s%,incidentdate=s%,location=s%,description=%s, status=%s, victimid=%s,suspectid=s%
                            WHERE incidentid = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error updating Incident: {e}"

    def delete_incidents(self):
        try:
            self.open()
            incidentid = int(input('Input Incident ID to be Deleted: '))
            delete_str = f'''DELETE FROM Incident WHERE incidentid = {incidentid}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error deleting Incident: {e}"

    def select_incidents(self):
        try:
            select_str = '''SELECT * FROM Incidents'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In Incidents Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(f"Error selecting Incidents: {e}")



