from pymongo import MongoClient
from pymongo.results import InsertManyResult
from bson.objectid import ObjectId

class MongoDBHandler:
    def __init__(self, database_url, database_name):
        self.database_url = database_url
        self.database_name = database_name
        self.client = None

    def __enter__(self):
        self.client = MongoClient(self.database_url)
        self.db = self.client[self.database_name]
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()

    def create_document(self, collection_name, data):
        collection = self.db[collection_name]
        result = collection.insert_many(data)
        if isinstance(result, InsertManyResult):
            return result.inserted_ids
        else:
            return None

    def read_documents(self, collection_name, query=None):
        collection = self.db[collection_name]
        if query:
            documents = collection.find(query)
        else:
            documents = collection.find()
        return list(documents)

    def read_document_by_id(self, collection_name, document_id):
        collection = self.db[collection_name]
        document = collection.find_one({"_id": ObjectId(document_id)})
        return document

    def update_document(self, collection_name, document_id, data):
        collection = self.db[collection_name]
        result = collection.update_one({"_id": ObjectId(document_id)}, {"$set": data})
        return result.modified_count

    def delete_document(self, collection_name, document_id):
        collection = self.db[collection_name]
        result = collection.delete_one({"_id": ObjectId(document_id)})
        return result.deleted_count