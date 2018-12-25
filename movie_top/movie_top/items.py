# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieTopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field();	
    motto = scrapy.Field();
    name_all = scrapy.Field();
    director = scrapy.Field();
    grader = scrapy.Field();
    image_url = scrapy.Field();
    a_href  = scrapy.Field();

    # image_urls = scrapy.Field()
    # images = scrapy.Field()

    pass


# import scrapy

# class DmozItem(scrapy.Item):
#     title = scrapy.Field()
#     link = scrapy.Field()
#     desc = scrapy.Field()


