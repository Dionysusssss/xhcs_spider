# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class Xhcs2520Pipeline(object):
    def __init__(self):
        # csv文件的位置,无需事先创建
        store_file = "/root/xhcs/data/data_2520.csv"
        # 打开(创建)文件
        self.file = open(store_file, "a", encoding="utf-8", newline='')
        # csv写法
        self.writer = csv.writer(self.file)

    def process_item(self, item, spider):
        # 判断字段值不为空再写入文件
        if item['grade']:
            if item['quantity'] == None and item['weight'] == None:
                self.writer.writerow(
                    [item['grade'], item["size"], "0", item['company'], "0", item['area'], item['date']])
            elif item['quantity'] == None and item['weight'] != None:
                self.writer.writerow(
                    [item['grade'], item["size"], "0", item['company'], item['weight'][:-2], item['area'],
                     item['date']])
            elif item['quantity'] != None and item['weight'] == None:
                self.writer.writerow(
                    [item['grade'], item["size"], item['quantity'][:-1], item['company'], "0", item['area'],
                     item['date']])
            else:
                self.writer.writerow(
                    [item['grade'], item['size'], item['quantity'][:-1], item['company'], item['weight'][:-2],
                     item['area'], item['date']])
        return item

    def close_spider(self, spider):
        # 关闭爬虫时顺便将文件保存退出
        self.file.close()