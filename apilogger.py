import os, sys
import datetime
from pathlib import Path
import csv

class API_Logger():
    
    def Logg_API_Call(self, key:str = '') -> bool:
        """
        Logg entry into api_calls.csv file and return True on success, False otherwise.
        """
        try:
            with open(Path.joinpath(Path().resolve(),'api_calls.csv'), 'a', newline='') as csvfile:
                logwriter = csv.writer(csvfile, delimiter='|', quotechar="'", quoting=csv.QUOTE_MINIMAL)
                dt = datetime.datetime.now()
                array = []
                array.append(str(datetime.datetime.now()))
                array.append(str(dt.strftime("%d"))) #Day
                array.append(str(dt.strftime("%b"))) #Month
                array.append(str(dt.year)) #Year
                array.append(str(dt.strftime("%X"))) #Time
                array.append(key)
                print(array)
                logwriter.writerow(array)
                return True
        except Exception as ex:
            print(ex.args)
            return False
    
    def Read_API_Calls(self):
        try:
            with open(Path.joinpath(Path().resolve(),'api_calls.csv'), newline='') as csvfile:
        
                loggreader = csv.reader(csvfile, delimiter='|', quotechar="'")
                return loggreader
                #for row in spamreader:
                #    print(row)
                    #print(', '.join(row))
        except Exception as ex:
            return ex.args

#logger = API_Logger()

#logger.Logg_API_Call("hello")
#logger.Read_API_Calls()