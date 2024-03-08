from entity.reports import Reports

class ReportsDao(Reports):
    def __init__(self):
        super().__init__()

    def perform_reports_actions(self):
        while True:
            print("(Reports) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_reports_table()
            elif ch == 2:
                print(self.add_reports())
            elif ch == 3:
                print(self.update_reports())
            elif ch == 4:
                print(self.delete_reports())
            elif ch == 5:
                self.select_reports()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_reports_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Reports (
                reportid INT  PRIMARY KEY,
                incidentid INT,
                reportingofficer INT,
                reportdate date,
                reportdetails VARCHAR(200),
                status VARCHAR(50),              
                FOREIGN KEY(reportingofficer) REFERENCES Officers(officerid) ON DELETE CASCADE ON UPDATE CASCADE)'''

            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('Reports Table Created successfully.')
        except Exception as e:
            print(f"Error creating Reports table: {e}")

    def add_reports(self):
        try:
            self.open()
            self.reportid = int(input('Enter Report ID: '))
            self.incidentid= int(input('Enter Incident ID: '))
            self.reportingofficer= int(input('Enter Reporting Officer ID: '))
            self.reportdate= input('Enter Report Date: ')
            self.reportdetails = input('Enter Report Details: ')
            self.status = input('Enter Status: ')
            data = [(self.reportid, self.incidentid, self.reportingofficer, self.reportdate,self.reportdetails,self.status)]
            insert_str = '''INSERT INTO Reports(reportid,incidentid,reportingofficer,reportdate,reportdetails,status)
                            VALUES(%s, %s, %s, %s,%s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error adding Report{e}"

    def update_reports(self):
        try:
            self.open()
            reportid = int(input('Input Report ID to be Updated: '))
            self.incidentid = input('Enter Incident ID: ')
            self.reportingofficer = input('Enter Reporting Officer: ')
            self.reportdate = int(input('Enter Report Date: '))
            self.reportdetails = int(input('Enter Report Details: '))
            self.status = input('Enter Status: ')
            data = [(self.incidentid, self.reportingofficer, self.reportdate ,self.reportdetails,self.status,reportid)]
            update_str = '''UPDATE Reports SET incidentid=s%,reportingofficer=s%,reportdate=s%,reportdetails=%s, status=%s
                            WHERE reportid = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error updating Report: {e}"

    def delete_reports(self):
        try:
            self.open()
            reportid = int(input('Input Report ID to be Deleted: '))
            delete_str = f'''DELETE FROM Reports WHERE reportid = {reportid}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error deleting Report: {e}"

    def select_reports(self):
        try:
            select_str = '''SELECT * FROM Reports'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In Reports Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(f"Error selecting Reports: {e}")



