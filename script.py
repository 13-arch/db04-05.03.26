import pymssql
import credits as cr


conn = pymssql.connect(cr.server , cr.user,cr.password,cr.db)
cursor = conn.cursor()

cursor.execute("""
    USE TEST

    CREATE TABLE TABLE3(
    ID IN UNIQUE IDENTITY(1,1),
    SURNAME NVARCHAR(50),
    )

""")
conn.commit()


conn.close()