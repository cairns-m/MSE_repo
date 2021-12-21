# a script to do python based access to the github api
# step 6 - Let's do a useful search

print("Demonstration python based mongodb access")

import pymongo              # for mongodb access
import pprint               # for pretty printing db data

#Let's get the user object from the db

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

githubuser = db.githubuser.find()

for user in db.githubuser.find({'location': {'$exists': True}}):
    pprint.pprint(user)
    print()

print("all done ")
