import mysql.connector

cnx = mysql.connector.connect(user='root',password='password',host='localhost',database='College')
cursor = cnx.cursor()
query = ("select cName from College")
cursor.execute(query)
for (cName) in cursor:
    print "Universidad {}".format(cName[0])
    print type(cName)
cnx.close()
