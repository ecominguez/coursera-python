import mysql.connector

cnx = mysql.connector.connect(user='admin',password='admin1',host='192.168.0.185',database='College')
cursor = cnx.cursor()
query = ("select cName from College")
cursor.execute(query)
for (cName) in cursor:
    print "Universidad {}".format(cName[0])
cnx.close()