# -*- coding: utf-8 -*-
import scrapy
from movie_top.items import MovieTopItem

class MovieSpider(scrapy.Spider):
	name = 'movie'
	allowed_domains = ['movie.com']
	start_urls = ['https://movie.douban.com/top250']

	def parse(self, response):
		print("++++++++++++++++++begin++++++++++++++++++");
		diva = response.xpath('//ol[@class="grid_view"]') 
		# motto = diva.xpath('li//div[@class="bd"]/p[@class="quote"]/span/text()').extract();
		# name = diva.xpath('li//div[@class="hd"]/a/span/text()').extract();
		# print (name);
		a = 0;
		for subdiv in diva.xpath('li'):
			a += 1;
			name = subdiv.xpath('div/div[2]/div/a/span/text()').extract();
			motto = subdiv.xpath('div/div[2]/div[2]/p[2]/span/text()').extract();
			grader = subdiv.xpath('div/div[2]/div[2]/div/span/text()').extract();
			image_url = subdiv.xpath('div/div/a/img/@src').extract();
			print (image_url[0]);

 
			item = MovieTopItem();
			try:
				item['name'] = name;
				item['motto'] = motto;
				item['grader'] = grader;
				item['image_url'] = image_url[0];

				yield item;
			except:
				pass

		# for subname in name:
		# 	print("name:",subname);


		# for substr in motto:
		# 	print ("str:",substr); 

