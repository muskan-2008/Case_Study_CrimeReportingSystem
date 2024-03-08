from entity.lawinforcementagencies import LawInforcementAgencies

class LawInforcementAgenciesDao(LawInforcementAgencies):
    def __init__(self):
        super().__init__()

    def perform_lia_actions(self):
        while True:
            print("(LawInforcementAgencies) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_lia_table()
            elif ch == 2:
                print(self.add_lia())
            elif ch == 3:
                print(self.update_lia())
            elif ch == 4:
                print(self.delete_lia())
            elif ch == 5:
                self.select_lia()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_lia_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS LawInforcementAgencies (
                agencyid INT  PRIMARY KEY,
                agencyname VARCHAR(100),
                jurisdiction VARCHAR(255),
                contactnumber VARCHAR(15),
                officerid INT,
                FOREIGN KEY(officerid) REFERENCES Officers(officerid) ON DELETE CASCADE ON UPDATE CASCADE)'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('LawInforcementAgencies Table Created successfully.')
        except Exception as e:
            print(f"Error creating LawInforcementAgencies table: {e}")

    def add_lia(self):
        try:
            self.open()
            self.agencyid = int(input('Enter Agency ID: '))
            self.agencyname = input('Enter Agency Name: ')
            self.jurisdiction = input('Enter Jurisdiction: ')
            self.contactnumber = input('Enter Contact Number: ')
            self.officerid=int(input('Enter Officer ID'))

            data = [(self.agencyid, self.agencyname, self.jurisdiction, self.contactnumber,self.officerid)]
            insert_str = '''INSERT INTO LawInforcementAgencies(agencyid,agencyname,jurisdiction,contactnumber,officerid)
                            VALUES(%s, %s, %s, %s,%s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error adding LawInforcementAgencies: {e}"

    def update_lia(self):
        try:
            self.open()
            agencyid = int(input('Input Agency ID to be Updated: '))
            self.agencyname = input('Enter Agency Name: ')
            self.jurisdiction = input('Enter Jurisdiction: ')
            self.contactnumber = input('Enter Contact Number: ')
            self.officerid = int(input('Enter Officer ID: '))

            data = [(self.agencyname, self.jurisdiction, self.contactnumber,self.officerid,agencyid)]
            update_str = '''UPDATE LawInforcementAgencies SET agencyname=%s, jurisdiction=%s, contactnumber=%s, officerid=s%
                            WHERE agencyid = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error updating LawInforcementAgencies: {e}"

    def delete_lia(self):
        try:
            self.open()
            agencyid = int(input('Input Agency ID to be Deleted: '))
            delete_str = f'''DELETE FROM LawInforcementAgencies WHERE agencyid = {agencyid}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error deleting LawInforcementAgencies: {e}"

    def select_lia(self):
        try:
            select_str = '''SELECT * FROM LawInforcementAgencies'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In LawInforcementAgencies Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(f"Error selecting LawInforcementAgencies: {e}")



