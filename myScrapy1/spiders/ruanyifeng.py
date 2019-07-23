# -*- coding: utf-8 -*-
import scrapy


class RuanyifengSpider(scrapy.Spider):
    name = 'ruanyifeng'
    allowed_domains = ['www.ruanyifeng.com']
    start_urls = ['http://www.ruanyifeng.com/blog/']

    def parse(self, response):
        for each in response.xpath("//li[@class='module-list-item']"):
            print(each.xpath("a/text()").extract()[0])
