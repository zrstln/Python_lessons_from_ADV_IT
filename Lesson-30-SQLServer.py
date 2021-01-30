import pypyodbc

mySQLServer = "WS0360220802"
myDatabase = "BewardRecordCenter"

connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=' + mySQLServer + ';'
                              'Database=' + myDatabase + ';')
cursor = connection.cursor()
mySQLQuery = ("""
                SELECT TIMETAG, filesize, DEVICEIP
                FROM dbo.VIDEOARCHIVE
                WHERE filesize = '11122688'
                """)
cursor.execute(mySQLQuery)
results = cursor.fetchall()
for row in results:
    timetag = row[0]
    filesize = row[1]
    deviceip = row[2]
    print("----------------------------------------------------------------------------------------------------")
    print("|1-й столбец: " + str(timetag) + ";" + " |2-й столбец: " + str(filesize) + ";" + " |3-й столбец: " + str(
            deviceip))
    print("----------------------------------------------------------------------------------------------------")
    connection.close()
