
import mysql.connector as sql

conn = (sql.connect(
    host="localhost",
    user="root",
    password="Samay@2002",
    database="mysql"
))

if conn.is_connected():
    print("connection Established")
print(conn)
cursor_variable = conn.cursor()
# cursor_variable.execute("""
# CREATE TABLE employees5 (
#     emp_id INT NOT NULL PRIMARY KEY,
#     emp_name VARCHAR(55) NOT NULL,
#     hire_date DATE NOT NULL,
#     salary INT,
#     dept_id INT
# );
# """)
cursor_variable.execute("""
INSERT INTO employees5 values (1, 'samay','2025-09-15', 40000, 101);""")
conn.commit()
# for DML commands
