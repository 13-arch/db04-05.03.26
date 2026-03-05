import pymssql
import credits as cr


conn = pymssql.connect(cr.server , cr.name,cr.password,cr.db)
cursor = conn.cursor()


cursor.execute("""
    USE test2
               
    CREATE TABLE faculty_HICO69(
    faculty_id INT IDENTITY(1,1) PRIMARY KEY,
    faculty_name NVARCHAR(15),
    )
                """)

cursor.execute("""
    USE test2
               
    CREATE TABLE GRoupsHICO69(
    group_ID INT IDENTITY(1,1) PRIMARY KEY,
    group_name NVARCHAR(20),
    faculty INT,
    CONSTRAINT KEY1_HICO69 FOREIGN KEY (faculty) REFERENCES faculty_HICO69(faculty_id),
    )
                """)

cursor.execute("""
    USE test2
               
    CREATE TABLE Students_HICO69(
    ID INT IDENTITY(1,1) PRIMARY KEY,
    stud_name NVARCHAR(20),
    groupz INT,
    faculty INT,
    CONSTRAINT KEY2_HICO69 FOREIGN KEY (groupz) REFERENCES GRoupsHICO69(group_ID),
    )
                """)    

cursor.execute("""
    use test2

    insert into Students_HICO69 values('senya')
""")            
for row in cursor:
    print(row)


conn.commit()


conn.close()