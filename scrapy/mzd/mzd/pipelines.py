# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy 
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
 


class OneClass(object):
	"""docstring for OneClass""" 
	def get_name(self, str):	
		print str + '=============='
		
class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
    	print "----aa---"
    	print item
    	print "----bb---"
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item