# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class InflearnTutorialPipeline(object):
    def __init__(self):
        self.csvwriter = csv.writer(open("dmoz_result.csv", "w"))
        self.csvwriter.writerow(["title", "link", "desc"])

    def process_item(self, item, spider):
        row = []
        row.append(item["title"])
        row.append(item["link"])
        row.append(item["desc"])
        self.csvwriter.writerow(row)
        return item
