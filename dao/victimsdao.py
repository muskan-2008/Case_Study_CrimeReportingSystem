from entity.victims import Victims

class VictimsDao(Victims):
    def __init__(self):
        super().__init__()

    def perform_victims_actions(self):
        while True:
            print("(Victims) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                print(self.create_victims_table())
            elif ch == 2:
                print(self.add_victims())
            elif ch == 3:
                print(self.update_victims())
            elif ch == 4:
                print(self.delete_victims())
            elif ch == 5:
                self.select_victims()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_victims_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Victims (
                victimid INT  PRIMARY KEY,
                firstname VARCHAR(50),
                lastname VARCHAR(50),
                dateofbirth DATE,
                gender VARCHAR(10),
                contactnumber VARCHAR(15))'''

            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('Victims Table Created successfully.')
        except Exception as e:
            print(f"Error creating Victims table: {e}")

    def add_victims(self):
        try:
            self.open()
            self.victimid = int(input('Enter Victim ID: '))
            self.firstname = input('Enter First Name: ')
            self.lastname = input('Enter Last Name: ')
            self.dateofbirth= input('Enter Date Of Birth: ')
            self.gender = input('Enter Gender: ')
            self.contactnumber = input('Enter Contact Number: ')
            data = [(self.victimid, self.firstname, self.lastname, self.dateofbirth,self.gender,self.contactnumber)]
            insert_str = '''INSERT INTO Victims(victimid,firstname,lastname,dateofbirth,gender,contactnumber)
                            VALUES(%s, %s, %s, %s,%s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.close()
            print('Victim Details Inserted successfully.')
        except Exception as e:
            return f"Error adding Victims{e}"

    def update_victims(self):
        try:
            self.open()
            victimid = int(input('Input Victim ID to be Updated: '))
            self.firstname = input('Enter First Name: ')
            self.lastname = input('Enter Last Name: ')
            self.dateofbirth = input('Enter Date Of Birth: ')
            self.gender = input('Enter Gender: ')
            self.contactnumber = input('Enter Contact Number: ')
            data = (self.firstname, self.lastname, self.dateofbirth ,self.gender,self.contactnumber,victimid)
            update_str = '''UPDATE Victims SET firstname=%s,lastname=%s,dateofbirth=%s,gender=%s, contactnumber=%s
                            WHERE victimid = %s'''
            self.stmt.execute(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error updating Victim: {e}"

    def delete_victims(self):
        try:
            self.open()
            victimid = int(input('Input Victim ID to be Deleted: '))
            delete_str = f'''DELETE FROM Victims WHERE victimid = {victimid}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error deleting Victim: {e}"

    def select_victims(self):
        try:
            select_str = '''SELECT * FROM Victims'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In Victims Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(f"Error selecting Victims: {e}")



