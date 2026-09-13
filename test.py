import sqlite3
import pandas as pd

conn = sqlite3.connect("autodata.db")

df = pd.read_sql("SELECT * FROM ajoneuvot LIMIT 5", conn)

print(df)