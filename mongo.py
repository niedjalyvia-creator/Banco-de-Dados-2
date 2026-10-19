from pymongo import MongoClient
uri = "mongodb+srv://niedjalyvia_db_user:2lZFn461rMwkNYcB@bd2.hdqka3d.mongodb.net/"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)