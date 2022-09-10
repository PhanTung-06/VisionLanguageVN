import pyodbc
import pandas as pd

db_driver = '{Microsoft Access Driver (*.mdb, *.accdb}'
db_path = '"F:\\Thesis\\data_lmdb_release\\data_lmdb_release\\validation\\data.mdb"'
conn_str = (rf'DRIVER={db_driver};'
            rf'DBQ={db_path};'
            r'Mode=Read;')

conn = pyodbc.connect(conn_str)

df = pd.read_sql(sql="select * from test_table", con=conn)
print(df)

conn.close()