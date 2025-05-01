from .apiHandler import API_Handler

apih = API_Handler(database_name="passpic_api.db",table_name_keys="tbl_keys", table_name_logg="tbl_log")

from tkinter import Tk

if __name__ == "__main__":
    application.run()