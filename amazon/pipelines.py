# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import pymongo
# from scrapy.conf import settings


# class AmazonPipeline(object):
#     def __init__(self):
#         host = settings["MONGODB_HOST"]
#         port = settings["MONGODB_PORT"]
#         dbname = settings["MONGODB_DBNAME"]
#         sheetname = settings["MONGODB_SHEETNAME"]
#         # 创建MONGODB数据库链接
#         client = pymongo.MongoClient(host=host, port=port)
#         # 指定数据库
#         mydb = client[dbname]
#         # 存放数据的数据库表名
#         self.post = mydb[sheetname]
#
#     def process_item(self, item, spider):
#         data = dict(item)
#         self.post.insert(data)
#         return item


import json

class AmazonPipeline(object):

    def __init__(self):
        self.file = open('items.json', 'w')

    def process_item(self, item, spider):
        line: str = json.dumps(dict(item)) + "\n"
        # print(line)
        self.file.write(line)
        return item