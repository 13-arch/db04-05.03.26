import pymssql
import credits as cr


conn = pymssql.connect(cr.server , cr.name,cr.password,cr.db)
cursor = conn.cursor()



cursor.execute("""
    USE test2
               
    CREATE TABLE HICO69(
    ID INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(20),
    groups INT,
    CONSTRAINT FK_1 FOREIGN KEY group_id REFERENCES HICO60.groups,
    )
                """)

conn.commit()


conn.close()

