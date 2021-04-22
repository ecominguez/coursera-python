from pymongo import MongoClient

# pprint library is used to make the output look more pretty
from pprint import pprint

print("\n******************** Start\n")

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://spock:viruta64@cluster0.ccwcb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.test


db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
print("\n******************** End\n")