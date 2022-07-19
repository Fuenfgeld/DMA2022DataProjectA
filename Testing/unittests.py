import sqlite3
import unittest
import pandas as pd
import datetime
import logging

#Die Tests überprüfen, wie viele Einträge (Rows) in der einzulesenen CSV Datei vorhanden sind. Danach wird überprüft, wie viele Rows in der Tabelle in der Datenbank vorhanden sind. Diese beiden
#Werte müssen identisch sein.
#Die Faktentabelle setzt sich nur aus bestimmten Tabellen zusammen, auch hier wird überprüft wie viele Rows in der Faktentabelle vorhanden sind. Dieser Wert wird dann mit dem Wert der
#aufaddierten Rows der genutzten Tabellen verglichen.

#setup für Tests
logging.basicConfig(filename="../Logs/log.txt", level=logging.DEBUG)
conn = sqlite3.connect('../datawarehouse.db')
logging.debug(" "+str(datetime.datetime.now()) + " unittests.py opened a connection to the database")

class unitTestingBreastCancerClass(unittest.TestCase):

    def test_careplans(self):
        tablename = "careplans"
        number_of_rows_in_df, number_of_rows_in_csv = get_counts(tablename)
        self.assertEqual(number_of_rows_in_df, number_of_rows_in_csv)

    def test_conditions(self):
        tablename = "conditions"
        number_of_rows_in_df, number_of_rows_in_csv = get_counts(tablename)
        self.assertEqual(number_of_rows_in_df, number_of_rows_in_csv)

    def test_immunizations(self):
        tablename = "immunizations"
        number_of_rows_in_df, number_of_rows_in_csv = get_counts(tablename)
        self.assertEqual(number_of_rows_in_df, number_of_rows_in_csv)

    def test_medications(self):
        tablename = "medications"
        number_of_rows_in_df, number_of_rows_in_csv = get_counts(tablename)
        self.assertEqual(number_of_rows_in_df, number_of_rows_in_csv)    

    def test_observations(self):
        tablename = "observations"
        number_of_rows_in_df, number_of_rows_in_csv = get_counts(tablename)
        self.assertEqual(number_of_rows_in_df, number_of_rows_in_csv)   

    def test_patients(self):
        tablename = "patients"
        number_of_rows_in_df, number_of_rows_in_csv = get_counts(tablename)
        self.assertEqual(number_of_rows_in_df, number_of_rows_in_csv)

    def test_facts(self):
        tablename = "facts_table"
        list_of_tables_used_in_facts = ["careplans", "conditions", "immunizations", "observations"]
        sum_of_rows = 0
        for table in list_of_tables_used_in_facts:
            sum_of_rows += get_row_count(table)  
        number_of_rows_in_df = get_row_count(tablename)
        self.assertEqual(number_of_rows_in_df, sum_of_rows),

    @classmethod
    def tearDownClass(cls):
        conn.close
        logging.debug(" "+str(datetime.datetime.now()) + " unittests.py closed the connection to the database")
    

def get_counts(tablename):
    number_of_rows_in_df = get_row_count(tablename)
    number_of_rows_in_csv = get_csv_length(tablename)
    return number_of_rows_in_df, number_of_rows_in_csv

def get_row_count(tablename):
    number_of_rows_in_df = pd.read_sql_query("SELECT COUNT(*) FROM {}".format(tablename), conn)["COUNT(*)"][0] 
    return number_of_rows_in_df

def get_csv_length(tablename):
    csv_length = len(pd.read_csv('../Daten/{}.csv'.format(tablename), sep=","))
    return csv_length



if __name__ == '__main__':
    unittest.main() 
    