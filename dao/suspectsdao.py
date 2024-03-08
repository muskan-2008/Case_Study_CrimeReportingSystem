from entity.suspects import Suspects

class SuspectsDao(Suspects):
    def __init__(self):
        super().__init__()

    def perform_suspects_actions(self):
        while True:
            print("(Suspects) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_suspects_table()
            elif ch == 2:
                print(self.add_suspects())
            elif ch == 3:
                print(self.update_suspects())
            elif ch == 4:
                print(self.delete_suspects())
            elif ch == 5:
                self.select_suspects()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_suspects_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Suspects (
                suspectid INT  PRIMARY KEY,
                firstname VARCHAR(50),
                lastname VARCHAR(50),
                dateofbirth DATE,
                gender VARCHAR(10),
                contactnumber VARCHAR(15))'''

            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('Suspects Table Created successfully.')
        except Exception as e:
            print(f"Error creating Suspects table: {e}")

    def add_suspects(self):
        try:
            self.open()
            self.suspectid = int(input('Enter Suspect ID: '))
            self.firstname = input('Enter First Name: ')
            self.lastname = input('Enter Last Name: ')
            self.dateofbirth= input('Enter Date Of Birth: ')
            self.gender = input('Enter Gender: ')
            self.contactnumber = input('Enter Contact Number: ')
            data = [(self.suspectid, self.firstname, self.lastname, self.dateofbirth,self.gender,self.contactnumber)]
            insert_str = '''INSERT INTO Suspects(suspectid,firstname,lastname,dateofbirth,gender,contactnumber)
                            VALUES(%s, %s, %s, %s,%s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error adding Suspect{e}"

    def update_suspects(self):
        try:
            self.open()
            suspectid = int(input('Input Suspect ID to be Updated: '))
            self.firstname = input('Enter First Name: ')
            self.lastname = input('Enter Last Name: ')
            self.dateofbirth = input('Enter Date Of Birth: ')
            self.gender = input('Enter Gender: ')
            self.contactnumber = input('Enter Contact Number: ')
            data = [(self.firstname, self.lastname, self.dateofbirth ,self.gender,self.contactnumber,suspectid)]
            update_str = '''UPDATE Suspects SET firstname=%s,lastname=%s,dateofbirth=%s,gender=%s, contactnumber=%s
                            WHERE suspectid = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error updating Suspect: {e}"

    def delete_suspects(self):
        try:
            self.open()
            suspectid = int(input('Input Suspect ID to be Deleted: '))
            delete_str = f'''DELETE FROM Suspects WHERE suspectid = {suspectid}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return f"Error deleting Suspect: {e}"

    def select_suspects(self):
        try:
            select_str = '''SELECT * FROM Suspects'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In Suspects Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(f"Error selecting Suspects: {e}")



