from pymongo import *


# key
secret_key = 'new key @iw2#sd'

user_avatar_dir = 'static/user_avatar/'

# mongodb config
db_name = 'mongo_new'
client = MongoClient("mongodb://localhost:27017")
db = client[db_name]
