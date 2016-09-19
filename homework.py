
import sqlite3

new_con = sqlite3.connect("cars.db")

cursor = new_con.cursor()

cursor.execute("""CREATE TABLE inventory
		(Make TEXT, Model TEXT, Quantity INT)
		""")

new_con.close()
