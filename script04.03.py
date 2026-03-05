import pymssql
import credits as cr


conn = pymssql.connect(cr.server , cr.name,cr.password,cr.db)
cursor = conn.cursor()



# cursor.execute("""
#     USE test2
               
#     CREATE TABLE groups_HICO69(
#     group_id INT IDENTITY(1000,1) primary key,
#     Name NVARCHAR(5),
#     )
#                 """)

# cursor.execute("""
#     USE test2
               
#     CREATE TABLE HICO69(
#     ID INT IDENTITY(1,1) PRIMARY KEY,
#     name NVARCHAR(20),
#     groups INT,
#     CONSTRAINT FK_HICO69 FOREIGN KEY (groups) REFERENCES groups_HICO69(group_id),
#     )
#                 """)

cursor.execute("""
    USE test2

    insert into groups_HICO69 values ('k13')
    insert into HICO69 values ('senya',1000)
    select * from HICO69
""")



conn.commit()


conn.close()