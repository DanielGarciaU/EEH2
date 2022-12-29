import pandas as pd
import pyodbc 

conn_str = ("Driver={SQL Server};"
            "Server=ASVRDB03;"
            "Database=CONTROLENERGIA;"
            "UID=daniel.garcia;"
            "PWD=Daniel2022*;")
conn = pyodbc.connect(conn_str)

df = pd.read_sql('SELECT top 100* FROM historico_consumos', conn)

print(df)
print(df)
print('mi mamá me mima')
print(type(df))