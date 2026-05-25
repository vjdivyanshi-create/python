import sqlite3
conn = sqlite3.connect("db1.db")

#create the database table
# sql = """
# CREATE TABLE emp(
# id integer primary key autoincrement,
# name varchar(50),
# mob varchar(20),
# city varchar(50)
# )
# """
# conn.execute(sql)
# conn.close()

# insert data into the table
# sql = """
# insert into emp(name,mob,city) values('john doe','1234567890','new york'),('jane smith','0987654321','los angeles'),('michael brown','1122334455','chicago'),('lisa jones','2233445566','houston'),('emma davis','3344556677','phoenix')"""
# conn.execute(sql)
# conn.commit()
# conn.close()


#read data from the table
# sql = "select * from emp"
# cursor = conn.execute(sql)  
# for row in cursor:
#     print(row)

# conn.commit()
# conn.close()


#delete data from the table
# sql = "Delete from emp where id = 3"
# conn.execute(sql)   
# conn.commit()
# conn.close()

# read again
# sql = "select * from emp"
# cursor = conn.execute(sql)  
# for row in cursor:
#     print(row)

# conn.commit()
# conn.close()

#Query
sql = "select name from emp where city = 'new york'"
cursor = conn.execute(sql)
for row in cursor:
    print(row)
conn.commit()
conn.close()


nm = "python"
