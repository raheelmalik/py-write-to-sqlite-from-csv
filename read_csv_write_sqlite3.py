import pandas
import os
import glob
import time
import sqlite3
import datetime

low_memory=False
start_time = "start time: " + time.ctime()

csv_path = 'C:\\Users\\raheel\\Downloads\\'

files = glob.glob(csv_path + "\\extract*.csv")
files.sort(key=os.path.getctime)   #sort by create time
number_of_files = len(files) #count how many files

create_times = []

df = pandas.read_csv(files[-1])  #read csv
df['extract_datetime'] = str(datetime.datetime.now()) #add column	with the now timestamp

df['Last Found'] = pandas.to_datetime(df['Last Found'])
df['First Found'] = pandas.to_datetime(df['First Found'])
df['extract_datetime'] = pandas.to_datetime(df['extract_datetime'])

#list column names here
table = df[['IP Address','NetBIOS Name','Severity','Title','Port','Protocol','First Found','Last Found','Last Scanned With Scanner Profile','Last Status','Hidden','extract_datetime']]

import sqlite3
conn = sqlite3.connect('c:\\users\\raheel\\downloads\findings.sqlite')
from pandas.io import sql

#replace table showing latest data
sql.to_sql(table,name='latest',con=conn,if_exists='replace')
#append table maintaining historical data
sql.to_sql(table,name='vulns',con=conn,if_exists='append')
