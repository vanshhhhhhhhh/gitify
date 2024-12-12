import sqlite3


conn = sqlite3.connect('GITIF.db')


c = conn.cursor()

c.execute("SELECT * FROM gitify")
infos = c.fetchall()

for info in infos:
    print("Name :"+" "+info[0]+ " | "+ "URL :"+" "+info[1]+" | "+"Fork Count :"+" "+ info[2] +" | "+"Stars Count :"+" "+info[3])
    
 
print("Task completed.")
conn.commit()

conn.close()