import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://admin:secret@localhost:27017/")

# Access a specific database
db = client["your_database_name"]

# Access a collection (similar to a table in relational databases)
collection = db["your_collection_name"]

# Processed data to be inserted into the database
data = {"key1": "value1", "key2": "value2"}

# Insert the processed data into the collection
collection.insert_one(data)
