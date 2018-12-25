# -*- coding: utf-8 -*-
import scrapy
  
import json  
class BilispiderSpider(scrapy.Spider):
    name = 'bilispider'
    allowed_domains = ['bilispider.com']
    start_urls = [
    # 'https://www.bilibili.com'
    # 'https://www.bilibili.com/v/kichiku/?spm_id_from=333.334.primary_menu.60'
    # 'https://www.bilibili.com/v/douga/?spm_id_from=333.334.primary_menu.2'
    'https://api.live.bilibili.com/room/v1/RoomRecommend/biliIndexRecList?callback=liveXhrDone&_=1533718491966'
    ]

    def parse(self, response):
        print ("++++++++++++++++++++++begin+++++++++++++++++++++");
        # print (response.xpath('//title/text()').extract);
        # adiv = response.xpath('//div[@id="home_popularize"]');
        # bdiv = adiv.xpath('div[@class="l-con"]/div[@class="storey-box clearfix"]')
        # cdiv = bdiv.xpath('div');
        # ddiv = response.xpath('//div[@class="storey-box clearfix"]');
        # img = response.xpath('//*[@id="chief_recommend"]/div[2]/div[4]/a/div/p[1]');
        print('✅divB:__',response); 
        stra = str(response.body);
        typea = type(response.body); 
        print(stra);
        # jsona = json.loads(response.body);
        # com = jsona['liveXhrDone'];
        # print (com.dumps);
#         jsobj = json.loads(response.body)
# comment = jsobj['comment']
# print(comment)

        # for subimg in ddiv:
        	# print('图片地址',subimg.xpath('div/a/text()'));
















