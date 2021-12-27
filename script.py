# a script to do python based access to the github api
# let's start with a simple hello world app to get ourselves going.
# we have to pip install PyGithub on the command line.

print("Demonstration python based github api access")

# import Github from the PyGithub library

from github import Github   # github api access
import json                 # for converting a dictionary to a string
import pymongo              # for mongodb access
import os
# we initialise a PyGithub Github object with our access token.


#g = Github("token")
tk = os.getenv('GITHUB_PAT')
g = Github(tk)


# Let's get the user object and build a data dictionary
usr = g.get_user()

dct = {'user': usr.login,
       'fullname': usr.name,
       'location': usr.location,
       'company': usr.company}

print("dictionary is " + json.dumps(dct))

# now let's store the dictionary in a mongodb

# first we need to remove null fields from the dictionary, because
# if we don't we'll end up with null fields in the db. This will cause us
# lots of debugging problems later. The convention is only store actual data
# in the database.

for k, v in dict(dct).items():
    if v is None:
        del dct[k]

print("cleaned dictionary is " + json.dumps(dct))

# now let's store the data.

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

db.githubuser.insert_many([dct])
print("all done :) ")
