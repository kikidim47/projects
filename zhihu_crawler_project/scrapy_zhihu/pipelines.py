import pymongo

class MongoDBPipeline:
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client['zhihu']
        self.collection = self.db['hot_questions']

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
