import mysql.connector

cnx = mysql.connector.connect(user='admin',password='admin1',host='192.168.0.185',database='College')
cursor = cnx.cursor()
query = ("select cName,state from College")
cursor.execute(query)

for (cName,state) in cursor:
    if state=="CA":
        print "Universidad {} del la soleada California".format(cName)
    else:
        print "Universidad {} del  estado de {}".format(cName,state)

cnx.close()