import pymssql
import credits as cr


conn = pymssql.connect(cr.server , cr.name,cr.password,cr.db)
cursor = conn.cursor()


cursor.execute("""
    USE test2
    CREATE TABLE Motherboard_HICO69(
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Motherboard NVARCHAR(15),
    )    
                """)

cursor.execute("""
    USE test2
    CREATE TABLE CPU_HICO69(
    ID INT IDENTITY(1,1) PRIMARY KEY,
    CPU NVARCHAR(15),
    )   
                """)

cursor.execute("""
    USE test2
    CREATE TABLE PowerUnit_HICO69(
    ID INT IDENTITY(1,1) PRIMARY KEY,
    PowerUnit NVARCHAR(15),
    )   
                """)    

cursor.execute("""
    USE test2
    CREATE TABLE Body_HICO69(
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Body NVARCHAR(15),
    )   
""")  

cursor.execute("""
    USE test2
    CREATE TABLE RAM_HICO69(
    ID INT IDENTITY(1,1) PRIMARY KEY,
    RAM NVARCHAR(15),
    )   
""") 
 

cursor.execute("""
    USE test2
    CREATE TABLE GPU_HICO69(
    ID INT IDENTITY(1,1) PRIMARY KEY,
    GPU NVARCHAR(15),
    )   
""")  

cursor.execute("""
    USE test2
    CREATE TABLE Storage_HICO69(
    ID INT IDENTITY(1,1) PRIMARY KEY,
    HDD NVARCHAR(15),
    SSD NVARCHAR(15),
    )   
""")  

cursor.execute("""
    USE test2
    ID
    CREATE TABLE Comp_HICO69(
    Motherboard INT,
    CPU INT,
    RAM INT,
    GPU INT,
    Storage INT,
    PowerUnit INT,
    Body INT,
    CONSTRAINT FK_1HICO69 FOREIGN KEY (Motherboard) REFERENCES Motherboard_HICO69(ID),
    CONSTRAINT FK_2HICO69 FOREIGN KEY (CPU) REFERENCES CPU_HICO69(ID),
    CONSTRAINT FK_3HICO69 FOREIGN KEY (RAM) REFERENCES RAM_HICO69(ID),
    CONSTRAINT FK_4HICO69 FOREIGN KEY (GPU) REFERENCES GPU_HICO69(ID),
    CONSTRAINT FK_5HICO69 FOREIGN KEY (Storage) REFERENCES Storage_HICO69(ID),
    CONSTRAINT FK_6HICO69 FOREIGN KEY (PowerUnit) REFERENCES PowerUnit_HICO69(ID),
    CONSTRAINT FK_7HICO69 FOREIGN KEY (Body) REFERENCES Body_HICO69(ID),
    )   
""")  

cursor.execute("""
    USE test2
    INSERT INTO Motherboard_HICO69 VALUES ('SENYA')
    INSERT INTO CPU_HICO69 VALUES ('SENYA')
    INSERT INTO RAM_HICO69 VALUES ('SENYA')
    INSERT INTO GPU_HICO69 VALUES ('SENYA')
    INSERT INTO Storage_HICO69 VALUES ('SENYA','BLAT')
    INSERT INTO PowerUnit_HICO69 VALUES ('SENYA')
    INSERT INTO Body_HICO69 VALUES ('SENYA')
    )   
""")
for row in cursor:
    print(row)


conn.commit()


conn.close()