from pymongo import MongoClient
from pprint import pprint

client  = MongoClient('localhost',27017)
db = client['users_db_280']
users = db.users280

# users.insert_one({'author':'Spec_author'})
#
# users.insert_many([{"author": "Peter",
#                "age" : 56,
#                "text": "Wildberry is cool!",
#                "tags": ['cool'],
#                "date": '28.11.1970'},
#
#                     {"author": "John",
#                "age" : 28,
#                "title": "Hot Cool!!!",
#                "text": "easy too!",
#                "date": '13.03.2015'}])

# new_author =     {"author": "John",
#                "age" : 28,
#                "title": "Hot Cool!!!",
#                "text": "easy too!",
#                "date": '13.03.2015'}

# id_user = users.update_many({'author':'Black'},{'$set':{'age':68}})
# print(id_user)
users.find({'age':{'$gt':15}}).sort('author').limit(3)


# objects = users.find()
# for obj in objects:
#     pprint(obj)

# .count_documents
