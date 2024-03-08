from entity.evidence import Evidence

class EvidenceDao(Evidence):
    def __init__(self):
        super().__init__()

    def perform_evidence_actions(self):
        while True:
            print("(Evidence) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_evidence_table()
            elif ch == 2:
                print(self.add_evidence())
            elif ch == 3:
                print(self.update_evidence())
            elif ch == 4:
                print(self.delete_evidence())
            elif ch == 5:
                self.select_evidence()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_evidence_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Evidence (
                evidenceid INT  PRIMARY KEY,
                description VARCHAR(255),
                locationfound VARCHAR(255),
                incidentid INT,
                FOREIGN KEY(incidentid) REFERENCES Incidents(incidentid) ON DELETE CASCADE ON UPDATE CASCADE)'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('Evidence Table Created successfully.')
        except Exception as e:
            print(f"Error creating Evidence table: {e}")

    def add_evidence(self):
        try:
            self.open()
            self.evidenceid = int(input('Enter Evidence ID: '))
            self.description = input('Enter Description: ')
            self.locationfound = input('Enter Location Found: ')
            self.incidentid = int(input('Enter Incident ID: '))

            data = [(self.evidenceid, self.description, self.locationfound, self.incidentid)]
            insert_str = '''INSERT INTO Evidence(evidenceid,description,locationfound,incidentid)
                            VALUES(%s, %s, %s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error adding Evidence: {e}"

    def update_evidence(self):
        try:
            self.open()
            evidenceid = int(input('Input Evidence ID to be Updated: '))
            self.description = int(input('Enter Description: '))
            self.locationfound = int(input('Enter Location Found: '))
            self.incidentid = input('Enter Incident ID: ')

            data = [(self.description, self.locationfound, self.incidentid,evidenceid)]
            update_str = '''UPDATE Evidence SET description=%s, locationfound=%s, incidentid=%s
                            WHERE evidenceid = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error updating Evidence: {e}"

    def delete_evidence(self):
        try:
            self.open()
            evidenceid = int(input('Input Evidence ID to be Deleted: '))
            delete_str = f'''DELETE FROM Evidence WHERE evidenceid = {evidenceid}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error deleting Evidence: {e}"

    def select_evidence(self):
        try:
            select_str = '''SELECT * FROM Evidence'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In Evidence Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(f"Error selecting Evidence: {e}")



