import sqlite3


conn = sqlite3.connect('GITIF.db')


c = conn.cursor()

c.execute("""CREATE TABLE gitify(
          repo_name TEXT,
          repo_url TEXT,
          fork_count TEXT,
          stars_count TEXT
          )""")
 
print("Task completed.")
conn.commit()

conn.close()