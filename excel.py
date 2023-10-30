import sqlite3
import pandas as pd
from database.query import CREATE_ITINERARY
conn = sqlite3.connect('toursandtravels.db')
# conn.execute("DROP TABLE IF EXISTS ITINEARAY")
print("table")
# conn.execute(CREATE_ITINERARY)
print("yay")
excel_file = "itinerary.xlsx"


df = pd.read_excel(excel_file)
df.to_sql('ITINERARY', conn, if_exists = "append", index=False)
conn.commit()
conn.close()
print("done")
