import mysql.connector
from mysql.connector import Error

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(sid,song_name):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='songs',
                                             user='root',
                                             password='dhoni777')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO songs
                          (sid,song_name) VALUES (%s,%s)"""

        empPicture = convertToBinaryData(song_name)

        # Convert data into tuple format
        insert_blob_tuple = (sid,song_name)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB(5,r'C:\Users\Sachin\Music\Full Song KHAIRIYAT (BONUS TRACK) CHHICHHORE Sushant, Shraddha Pritam, Amitabh BArijit S.mp3')



