# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

# -*- coding: utf-8 -*-

import scrapy
import re  
import sys
from scrapy.selector import Selector  
from mzd.items import BooksItem   


class VerseItem(scrapy.Spider):
    name = 'douban'
    allowed_domains = ["book.douban.com"]  
    start_urls = ['https://book.douban.com/tag/%E5%8E%86%E5%8F%B2']   
    def parse(self, response): 
        print '+++++++++++++++++++++++++++++++++++++++++++begin'
        sel = Selector(response)  
        book_list = sel.css('#subject_list > ul > li')  
        for book in book_list:  
            item = BooksItem()  
            try:  
                item['book_name'] = book.xpath('div[@class="info"]/h2/a/text()').extract()[0].strip()  
                item['book_star'] = book.xpath("div[@class='info']/div[2]/span[@class='rating_nums']/text()").extract()[0].strip()  
                item['book_pl'] = book.xpath("div[@class='info']/div[2]/span[@class='pl']/text()").extract()[0].strip()  
                item['image_urls'] = book.xpath('div[@class="pic"]/a/img/@src').extract()
                pub = book.xpath('div[@class="info"]/div[@class="pub"]/text()').extract()[0].strip().split('/')  
                item['book_price'] = pub.pop()  
                item['book_date'] = pub.pop()  
                item['book_publish'] = pub.pop()  
                item['book_author'] = '/'.join(pub)   

                yield item  
            except:  
                pass  

        print '+++++++++++++++++++++++++++++++++++++++++++end'
 