import pymssql
import credits as cr


conn = pymssql.connect(cr.server , cr.name,cr.password,cr.db)
cursor = conn.cursor()


cursor.execute("""
    USE test2
    select * from HICO69
""")
for row in cursor:
    print(row)


conn.commit()


conn.close()