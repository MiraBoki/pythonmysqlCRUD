from databaseconfig import Database 
from mysql.connector import Error

class Staffs(Database):
    def create(self,name,email):
        
        try:
            self.connect()
            insert_sql = "INSERT INTO staffs (username,email) VALUES(%s,%s)"
            self.cursor.execute(insert_sql,(name,email))
            self.conn.commit()
            print(f"Data Inserted , ID is = : {self.cursor.lastrowid}")
        except Error as e:
            print("Error during insert : ",e)
        finally:
            self.close()

    def readall(self):
        
        try:
            self.connect()
            selectall_sql = "SELECT * FROM staffs"
            self.cursor.execute(selectall_sql)
            rows = self.cursor.fetchall()
            if rows:
                print("\n Staffs Lists :\n")
                # print(rows)
                for row in rows:
                    print(f"ID : {row[0]} , Name : {row[1]} , Email : {row[2]}")
            else:
                print("No Staffs Found!")
        except Error as e:
            print("Error during Fetch : ",e)
        finally:
            self.close()

    def update(self,userid,name,email):

        try: 
            self.connect()
            update_sql = "UPDATE staffs SET username=%s, email=%s WHERE id=%s"
            self.cursor.execute(update_sql,(name,email,userid))
            self.conn.commit()

            if self.cursor.rowcount > 0:
                print("Staff updated successfully!")
            else:
                print(f"No staff found with that ID.")

        except Error as e:
            print("Error during update : ",e)
        finally:
            self.close()

    def delete(self,deleteid):
        
        try:
            self.connect()
            delete_sql = "DELETE FROM staffs WHERE id=%s"
            self.cursor.execute(delete_sql,(deleteid,))
            self.conn.commit()

            if self.cursor.rowcount > 0:
                print("Staff deleted successfully!")
            else:
                print(f"No staff found with that ID.")

        except Error as e:
            print("Error during delete : ",e)
        finally:
            self.close()
        