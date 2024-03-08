from entity.officers import Officers

class OfficersDao(Officers):
    def __init__(self):
        super().__init__()

    def perform_officers_actions(self):
        while True:
            print("(Officers) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                print(self.create_officers_table())
            elif ch == 2:
                print(self.add_officers())
            elif ch == 3:
                print(self.update_officers())
            elif ch == 4:
                print(self.delete_officers())
            elif ch == 5:
                self.select_officers()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_officers_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Officers (
                officerid INT  PRIMARY KEY,
                firstname VARCHAR(50),
                lastname VARCHAR(50),
                badgenumber INT,
                rank_ INT,
                contactnumber VARCHAR(15))'''

            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('Officers Table Created successfully.')
        except Exception as e:
            print(f"Error creating Officers table: {e}")

    def add_officers(self):
        try:
            self.open()
            self.officerid = int(input('Enter Officer ID: '))
            self.firstname = input('Enter First Name: ')
            self.lastname = input('Enter Last Name: ')
            self.bagdenumber= int(input('Enter Badge Number: '))
            self.rank_ = int(input('Enter Rank: '))
            self.contactnumber = input('Enter Contact Number: ')
            data = [(self.officerid, self.firstname, self.lastname, self.badgenumber,self.rank_,self.contactnumber)]
            insert_str = '''INSERT INTO Officers(officerid,firstname,lastname,badgenumber,rank_,contactnumber)
                            VALUES(%s, %s, %s, %s,%s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error adding Officer{e}"

    def update_officers(self):
        try:
            self.open()
            officerid = int(input('Input Officer ID to be Updated: '))
            self.firstname = input('Enter First Name: ')
            self.lastname = input('Enter Last Name: ')
            self.badgenumber = int(input('Enter Location: '))
            self.rank_ = int(input('Enter Rank: '))
            self.contactnumber = input('Enter Contact Number: ')
            data = [(self.firstname, self.lastname, self.badgenumber ,self.rank_,self.contactnumber,officerid)]
            update_str = '''UPDATE Officers SET firstname=%s,lastname=%s,badgenumber=%s,rank_=%s, contactnumber=%s
                            WHERE officerid = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error updating Officer: {e}"

    def delete_officers(self):
        try:
            self.open()
            officerid = int(input('Input Officer ID to be Deleted: '))
            delete_str = f'''DELETE FROM Officers WHERE officerid = {officerid}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error deleting Officer: {e}"

    def select_officers(self):
        try:
            select_str = '''SELECT * FROM Officers'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In Officers Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(f"Error selecting Officers: {e}")



