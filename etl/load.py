import mysql.connector
from dotenv import load_dotenv
import os 


load_dotenv()

conn = mysql.connector.connect(
    host = os.getenv("host"),
    password = os.getenv("password"),
    port = os.getenv("port"),
    user = os.getenv("username"),
    database = os.getenv("database")
)

cursor = conn.cursor()

with open('data/formatted_holidays.sql') as file:
    sql_commands = file.read().split(';')

for command in sql_commands:
    command = command.strip()
    if command:
        try:
            cursor.execute(command)
        except mysql.connector.Error as err:
            print(f"Error executing command: {command}\n{err}")

# Commit and close connection
conn.commit()
cursor.close()
conn.close()


