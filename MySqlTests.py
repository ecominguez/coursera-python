import mysql.connector

print("************************antes")
try:
    cnx = mysql.connector.connect(user='admin', password='admin1', host='192.168.0.185', database='College')
except SystemExit as e:
    print(e)
    raise
print("************************despues")
cursor = cnx.cursor()
query = ("select cName,state from College")
cursor.execute(query)

for (cName, state) in cursor:
    if state == "CA":
        print("Universidad {} del la soleada California".format(cName))
    else:
        print("Universidad {} del  estado de {}".format(cName, state))

print("Movies -----------------------")

query = ("select mId,title,rID,stars,name from Movie join Rating using(mId) join Reviewer using(rID) order by mId")
cursor.execute(query)
keepGoing= True
row = cursor.fetchone()
movieId=row
JCR=False
while keepGoing:
    # Esto esta comenado a propósito print "1- Id: {} Pelicula: {} Rating:{} Reviewer: {} {}".format(row[0],row[1],row[3],row[2],row[4])

    if (movieId[0]==row[0]):
        if (row[4]=="James Cameron"):
            JCR=True
    else:
        if not JCR:
            print("Pelicula {} sin puntaje por Cameron".format(movieId[1]))
        movieId=row
        JCR=row[4]=="James Cameron"
    row=cursor.fetchone()
    keepGoing= row is not None
if not JCR:
    print("Pelicula {} sin puntaje por Cameron".format(movieId[1]))

cnx.close()
