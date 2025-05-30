import os, sys
import datetime
from pathlib import Path
import csv, sqlite3

DATABASE_NAME = ""
TABLE_NAME_KEYS = ""
TABLE_NAME_LOGG = ""

class API_Handler():
     
    def __init__(self, database_name: str="", table_name_keys: str="", table_name_logg:str="") -> None:
        self.DATABASE_NAME = database_name 
        self.TABLE_NAME_KEYS = table_name_keys
        self.TABLE_NAME_LOGG = table_name_logg
        tbl_keys = database_name + "." + table_name_keys
        tbl_logg = database_name + "." + table_name_logg
        try:
            #Create or Connect Database
            with sqlite3.connect(self.DATABASE_NAME) as conn:
                print("db created: success")
                sql = "CREATE TABLE IF NOT EXISTS " + table_name_keys + " (id INTEGER PRIMARY KEY AUTOINCREMENT, user_name text (64) NOT NULL, api_key text (64) NOT NULL,is_active INT NOT NULL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);"
                cursor = conn.cursor()
                cursor.execute(sql)
                print("key table created: success")
                sql = "CREATE TABLE IF NOT EXISTS " + table_name_logg + " (id INTEGER PRIMARY KEY AUTOINCREMENT, api_key text (64) NOT NULL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)"
                cursor = conn.cursor()
                cursor.execute(sql)
                print("logg table created: success")
                conn.commit()
                return None

        except sqlite3.OperationalError as e:
            print("Failed to open database:", e)
            return None
        
       

    def Insert_Logg(self, key:str = ""):
        try:
            with sqlite3.connect(self.DATABASE_NAME) as conn:
                sql = "INSERT INTO " + self.TABLE_NAME_LOGG + "(api_key) VALUES (?);"
                cursor = conn.cursor()
                args = (key,)
                cursor.execute(sql, args)
                conn.commit()
                print ("Record Added into Logg table")
                return True
        except Exception as ex:
            print("error occ:", ex)
            return False

    def Insert_Key(self, user_name:str="", key:str = ""):
        try:
            with sqlite3.connect(self.DATABASE_NAME) as conn:
                sql = "INSERT INTO " + self.TABLE_NAME_KEYS + "(api_key, user_name, is_active) VALUES (?,?,?);"
                cursor = conn.cursor()
                args = (key, user_name, 1,)
                cursor.execute(sql, args)
                conn.commit()
                print ("Record Added into Keys table")
                return True
        except Exception as ex:
            print("error occ:", ex)
            return False

    def Delete_Key(self, key:str = ""):
        try:
            with sqlite3.connect(self.DATABASE_NAME) as conn:
                sql = "DELETE FROM " + self.TABLE_NAME_KEYS + " WHERE api_key=?;"
                cursor = conn.cursor()
                args = (key,)
                cursor.execute(sql, args)
                conn.commit()
                print ("Record deleted from Keys table")
                return True
        except Exception as ex:
            print("error occ:", ex)
            return False

    def Activate_Key(self, key:str = ""):
        try:
            with sqlite3.connect(self.DATABASE_NAME) as conn:
                sql = "UPDATE " + self.TABLE_NAME_KEYS + " SET is_active = 1 WHERE api_key=?;"
                cursor = conn.cursor()
                args = (key,)
                cursor.execute(sql, args)
                conn.commit()
                print ("Record deleted from Keys table")
                return True
        except Exception as ex:
            print("error occ:", ex)
            return False

    def Deactivate_Key(self, key:str = ""):
        try:
            with sqlite3.connect(self.DATABASE_NAME) as conn:
                sql = "UPDATE " + self.TABLE_NAME_KEYS + " SET is_active = 0 WHERE api_key=?;"
                cursor = conn.cursor()
                args = (key,)
                cursor.execute(sql, args)
                conn.commit()
                print ("Record deleted from Keys table")
                return True
        except Exception as ex:
            print("error occ:", ex)
            return False

    def List_Keys_table (self):
        try:
            with sqlite3.connect(self.DATABASE_NAME) as conn:
                sql = "SELECT * FROM " + self.TABLE_NAME_KEYS
                cursor = conn.cursor()
                cursor.execute(sql)
                recs = cursor.fetchall()
                return recs
        except Exception as ex:
            print("error occ:", ex)
            return None


    def Print_Keys_table (self):
        try:
            with sqlite3.connect(self.DATABASE_NAME) as conn:
                sql = "SELECT * FROM " + self.TABLE_NAME_KEYS
                cursor = conn.cursor()
                cursor.execute(sql)
                recs = cursor.fetchall()
                print ("Records Printed Keys Table")
        except Exception as ex:
            print("error occ:", ex)

    def Print_Logg_table (self):
        try:
            with sqlite3.connect(self.DATABASE_NAME) as conn:
                sql = "SELECT * FROM " + self.TABLE_NAME_LOGG
                cursor = conn.cursor()
                cursor.execute(sql)
                recs = cursor.fetchall()
                print ("Records Printed Logg Table")
        except Exception as ex:
            print("error occ:", ex)

    def Drop_Keys_Table(self):
        try:
            with sqlite3.connect(self.DATABASE_NAME) as conn:
                sql = "DROP TABLE IF EXISTS " + self.TABLE_NAME_KEYS
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
                print("dropped table")
                return True
        except Exception as ex:
            print("error occ:", ex)
            return False

    def Key_Exists(self, key: str=""):
        try:
            with sqlite3.connect(self.DATABASE_NAME) as conn:
                sql = "SELECT * FROM " + self.TABLE_NAME_KEYS + " WHERE api_key=? AND is_active=1"
                cursor = conn.cursor()
                args = (key,)
                cursor.execute(sql, args)
                recs = cursor.fetchall()
                
                if recs:
                #    for rec in recs:
                    print ("Record found.")
                    return True
                else:
                    print ("Record NOT found.")
                    return False
        except Exception as ex:
            print("error occ:", ex)
            return False

#apih = API_Handler(database_name="passpic_api.db",table_name_keys="tbl_keys", table_name_logg="tbl_log")
#apih.Insert_Key("Khalid Chandio2", "keykeykeykey_2");
#apih.Insert_Logg("keykeykeykey_2")
#apih.Delete_Key("keykeykeykey_2")
#apih.Activate_Key("keykeykeykey_2")
#apih.Deactivate_Key("keykeykeykey_2")
#apih.Print_Keys_table()
#apih.Print_Logg_table()
#apih.Drop_Keys_Table()



