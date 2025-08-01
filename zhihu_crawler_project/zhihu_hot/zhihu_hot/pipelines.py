# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class ZhihuHotPipeline:
#     def process_item(self, item, spider):
#         return item



# 2
# from pymongo.mongo_client import MongoClient

# class ZhihuHotPipeline:
#     def open_spider(self, spider):
#         # Initialize MongoDB connection
#         self.client = MongoClient("mongodb+srv://tomdragon693:<db_password>@cluster0.0dtehzn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#         self.db = self.client['zhihu_hot']
#         self.collection = self.db['hot_items']

#     def process_item(self, item, spider):
#         self.col.update_one(
#             {"url": item["url"], "timestamp": item["timestamp"]},
#             {"$set": dict(item)},
#             upsert=True
#         )
#         return item

#     def close_spider(self, spider):
#         # Close the MongoDB connection when the spider is closed
#         self.client.close()

# 3
import json

class ZhihuHotPipeline:
    def open_spider(self, spider):
        # 打开文本文件用于写入（追加模式）
        self.file = open('zhihu_hotlist.txt', 'a', encoding='utf-8')

    def process_item(self, hot_item, spider):
        # 将每条 item 转为 JSON 字符串并写入一行
        print(hot_item)
        line = json.dumps(dict(hot_item), ensure_ascii=False)
        self.file.write(line + '\n')
        return hot_item

    def close_spider(self, spider):
        # 关闭文件
        self.file.close()