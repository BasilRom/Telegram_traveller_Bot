import sqlite3

conn1 = sqlite3.connect('promos.db')
cursor1 = conn1.cursor()

cursor1.execute('''CREATE TABLE IF NOT EXISTS histories 
            	(pers_id INTEGER PRIMARY KEY, 
            	name TEXT,
            	main_city TEXT,
            	boss TEXT,
            	symbol BLOB default 'files/book.jpg')''')




conn1.commit()

conn1.close()