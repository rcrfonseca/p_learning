#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import datetime
import pprint

from pymongo import MongoClient
from bson.objectid import ObjectId

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.posts.find_one({'_id': ObjectId(post_id)})

client = MongoClient()

#client = MongoClient('localhost', 27017)

#client = MongoClient('mongodb://localhost:27017/')

db = client.test_database



"""
If your database name is such that using attribute style access won’t work (like test-database), you can use dictionary style access instead:

>>> db = client['test-database']
"""

collection = db.test_collection


post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

#inserting doc
#verifying object_id of doc
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print (post_id)

#We can verify this by listing all of the collections in our database:
collection_names = db.collection_names(include_system_collections=False)
print (collection_names)

#prints the content of collection
pprint.pprint(posts.find_one())

pprint.pprint(posts.find_one({"author": "Mike"}))

pprint.pprint(posts.find_one({"author": "Eliot"}))

pprint.pprint(posts.find_one({"_id": post_id}))

post_id_as_str = str(post_id)
pprint.pprint(posts.find_one({"_id": post_id_as_str})) # No result

new_posts = [{"author": "Mike",
               "text": "Another post!",
               "tags": ["bulk", "insert"],
               "date": datetime.datetime(2009, 11, 12, 11, 14)},
              {"author": "Eliot",
               "title": "MongoDB is fun",
               "text": "and pretty easy too!",
               "date": datetime.datetime(2009, 11, 10, 10, 45)}]

result = posts.insert_many(new_posts)

print ("===================================================\n")

print(result.inserted_ids)

print ("===================================================\n")

for post in posts.find():
	pprint.pprint(post)

print ("===================================================\n")

for post in posts.find({"author": "Mike"}):
    pprint.pprint(post)

print ("===================================================\n")

pprint.pprint(posts.count())

posts.find({"author": "Mike"}).count()

print ("===================================================\n")

d = datetime.datetime(2009, 11, 12, 12)

for post in posts.find({"date": {"$lt": d}}).sort("author"):
	pprint.pprint(post)

#create indexes. To create index, do not need to create collection first, 
#the index operation will do that

result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],unique=True)

print ("===================================================\n")

#printing the list of indexes in a collection
pprint.pprint(sorted(list(db.profiles.index_information())))

#inserting new objects in profiles collection
user_profiles = [
     {'user_id': 211, 'name': 'Luke'},
     {'user_id': 212, 'name': 'Ziltoid'}]
result = db.profiles.insert_many(user_profiles)

print ("===================================================\n")

new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
result = db.profiles.insert_one(new_profile)  # This is fine.
result = db.profiles.insert_one(duplicate_profile)