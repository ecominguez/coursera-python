from pymongo import MongoClient


print("\n******************** Start MyFirstQueryMongo\n")
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://spock:viruta64@cluster0.ccwcb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.business

fivestar = db.reviews.find_one({'rating': 4})
print(fivestar)
fivestar = db.reviews.find_one({'cuisine': 'American'})
print(fivestar)
cursorCuisine = db.reviews.find({'cuisine': 'American'})
print('Lista {}'.format(cursorCuisine.collection.count_documents))
print("\n******************** End MyFirstQueryMongo\n")

# The result will contain data similar to the following:

# {u'rating': 5,
#  u'_id': ObjectId('58e65383ea0b650c867ef195'),
#  u'name': u'Fish Salty Corporation', 
# u'cuisine': u'Sushi Bar'}