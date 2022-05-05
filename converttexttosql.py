import sqlite3

print('''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░╔══╗░░░╔╗░░╔╗░░░░╔══╦══╦╗░░
░╚╗╔╬═╦╦╣╚╗░║╚╦═╗░║══╣╔╗║║░░
░░║║║╩╬║╣╔╣░║╔╣╬║░╠══║╚╝║╚╗░
░░╚╝╚═╩╩╩═╝░╚═╩═╝░╚══╩═╗╠═╝░
░░░░░░░░░░░░░░░░░░░░░░░╚╝░░░
''')

sql_file_name = input("Enter Data Base name: ")
file_path = input("Enter text file path: ")

con = sqlite3.connect(f"{sql_file_name}.db")
cur = con.cursor()
sql = """
                                CREATE TABLE IF NOT EXISTS data_table(
                                    record text)
                                """
cur.execute(sql)
con.commit()

counter = 0
file = open(file_path, "r", encoding="UTF-8")
lines = file.readlines()

for hash in lines:
    hash = hash.replace("\n", "")
    counter += 1
    cur.execute("SELECT * FROM data_table WHERE record = ?", [(hash)])

    if not cur.fetchall():
        print(f"{counter}. Adding to database: {hash}")
        cur.execute("INSERT INTO data_table (record) VALUES (?)", [(hash)])
        con.commit()
    else:
        print(f"Record already in Data Base skipping: {hash}")

print("\n\n==================Finished!==================")